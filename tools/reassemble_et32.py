#!/usr/bin/env python3
"""Overlay MStar sparse_write fragments into full read-only Android ext4 images."""
import json
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import zipfile

archive = Path(sys.argv[1])
out = Path("analysis/ET32")
out.mkdir(parents=True,exist_ok=True)
parts = json.loads((out/"partition_map.json").read_text())
original = Path("/tmp/et32-reassemble.bin")
with zipfile.ZipFile(archive) as z:
    with z.open(z.namelist()[0]) as src, original.open("wb") as dst:
        shutil.copyfileobj(src,dst,4*1024*1024)
summary=["# Reassembled ET32 Android images", ""]
def command(args,seconds=240):
    p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,errors="replace",timeout=seconds)
    return p.returncode,p.stdout,p.stderr
def rebuild(label):
    chunks=[x for x in parts if x.get("write_target")==label and "sparse" in x]
    if not chunks: raise ValueError("No sparse segments for "+label)
    full_len=chunks[0]["sparse"]["logical_bytes"]
    if full_len>5*1024**3: raise ValueError("too large")
    target=Path("/tmp/et32-"+label+".ext4")
    with target.open("wb") as dst: dst.truncate(full_len)
    counters={"raw":0,"fill":0,"skip":0,"crc":0}
    written=0
    with original.open("rb") as source, target.open("r+b") as dst:
        for segment in chunks:
            source.seek(segment["offset"])
            head=source.read(28)
            magic,major,minor,fh,ch,blksz,total_blks,num_chunks,crc=struct.unpack("<IHHHHIIII",head)
            if magic!=0xED26FF3A or major!=1 or ch<12 or fh<28:
                raise ValueError("bad sparse header at "+hex(segment["offset"]))
            if total_blks*blksz!=full_len:
                raise ValueError("inconsistent sparse disk size")
            source.seek(segment["offset"]+fh)
            cursor=0
            for n in range(num_chunks):
                chunk=source.read(ch)
                if len(chunk)!=ch: raise ValueError("truncated chunk header")
                typ,reserved,num_blks,total_size=struct.unpack("<HHII",chunk[:12])
                data_len=total_size-ch
                logical=num_blks*blksz
                if typ==0xCAC1:
                    if data_len!=logical: raise ValueError("RAW wrong size")
                    dst.seek(cursor)
                    todo=logical
                    while todo:
                        data=source.read(min(todo,4*1024**2))
                        if not data: raise ValueError("short RAW")
                        dst.write(data);todo-=len(data)
                    counters["raw"]+=1;written+=logical
                elif typ==0xCAC2:
                    if data_len!=4:raise ValueError("bad FILL")
                    pattern=source.read(4)
                    if pattern!=b"\0\0\0\0":
                        dst.seek(cursor)
                        repeat=pattern*min(1048576,logical//4)
                        todo=logical
                        while todo:
                            block=repeat[:min(todo,len(repeat))]
                            dst.write(block);todo-=len(block)
                        written+=logical
                    counters["fill"]+=1
                elif typ==0xCAC3:
                    if data_len: raise ValueError("skip chunk carries data")
                    counters["skip"]+=1
                elif typ==0xCAC4:
                    if data_len!=4:raise ValueError("CRC wrong size")
                    source.read(4);counters["crc"]+=1
                else:raise ValueError("unknown chunk type %x"%typ)
                if typ!=0xCAC4: cursor+=logical
            if cursor!=full_len: raise ValueError("incomplete logical span")
    return target,counters,written

for label in ("system","vendor"):
    image,counts,written=rebuild(label)
    code,stat,_=command(["debugfs","-R","stats",str(image)])
    summary.append("## "+label)
    summary.append("Logical image bytes: %d, populated bytes processed: %d" % (image.stat().st_size,written))
    summary.append("Sparse chunks: "+json.dumps(counts))
    summary.append("debugfs stats status: %s" % code)
    (out/("ext4_stats_"+label+".txt")).write_text(stat,encoding="utf-8")
    paths=(["/","/system","/system/app","/system/priv-app","/system/framework",
            "/system/etc","/system/bin","/system/lib","/system/lib64",
            "/system/media","/system/xbin"] if label=="system" else
           ["/","/app","/etc","/etc/init","/etc/permissions","/etc/vintf",
            "/firmware","/lib","/lib64","/bin","/tvconfig"])
    for p in paths:
        rc,data,err=command(["debugfs","-R","ls -p "+p,str(image)],120)
        if rc==0 and data.strip():
            name="listing_"+label+"_"+p.strip("/").replace("/","_")
            if not p.strip("/"):name="listing_"+label+"_root"
            (out/(name+".txt")).write_text(data[:300000],encoding="utf-8")
            summary.append("- Directory "+p+": "+str(len(data.splitlines()))+" entries")
    prop_path="/system/build.prop" if label=="system" else "/build.prop"
    rc,prop,err=command(["debugfs","-R","cat "+prop_path,str(image)],90)
    props={}
    allow={"ro.build.version.release","ro.build.version.sdk","ro.build.version.security_patch",
           "ro.build.fingerprint","ro.build.type","ro.build.tags","ro.build.date",
           "ro.product.model","ro.product.manufacturer","ro.product.device",
           "ro.product.brand","ro.hardware","ro.debuggable","ro.secure",
           "ro.adb.secure","ro.build.display.id"}
    for line in prop.splitlines():
        if "=" in line:
            key,value=line.split("=",1)
            if key.strip() in allow: props[key.strip()]=value.strip()
    summary.append("- Build properties: "+json.dumps(props,ensure_ascii=False))
    (out/("public_build_props_"+label+".json")).write_text(
        json.dumps(props,ensure_ascii=False,indent=2),encoding="utf-8")
    if label=="vendor":
        rc,xml,err=command(["debugfs","-R","cat /manifest.xml",str(image)],90)
        if rc==0:
            (out/"vendor_hal_manifest.xml").write_text(xml[:300000],encoding="utf-8")
summary.append("")
(out/"android_audit.md").write_text("\n".join(summary)+"\n",encoding="utf-8")
print("\n".join(summary))
