#!/usr/bin/env python3
"""Second-stage ET32 firmware map and rootfs extraction. Read only."""
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys
import zipfile

zip_path = Path(sys.argv[1]).resolve()
output = Path("analysis/ET32")
output.mkdir(parents=True, exist_ok=True)
bin_path = Path("/tmp/et32-second-stage.bin")
report = ["# ET32 partition and filesystem inspection", ""]
def run(args, timeout=180):
    try:
        p = subprocess.run(args, capture_output=True, text=True, timeout=timeout, errors="replace")
        return p.returncode, (p.stdout+p.stderr)[:200000]
    except Exception as e:
        return -1, str(e)
with zipfile.ZipFile(zip_path) as z:
    name = z.namelist()[0]
    with z.open(name) as src, bin_path.open("wb") as dst:
        shutil.copyfileobj(src, dst, 8*1024**2)
size = bin_path.stat().st_size
with bin_path.open("rb") as f:
    script_bytes = f.read(0x4000)
script = script_bytes.split(b"\x00")[0].decode("latin-1", "replace")
(output / "mstar_upgrade_commands.txt").write_text(script, encoding="utf-8")
commands = []
group = "unknown"
last = None
rx_load = re.compile(r"^filepartload\s+\S+\s+\$\(UpgradeImage\)\s+(0x[0-9a-fA-F]+)\s+(0x[0-9a-fA-F]+)")
rx_target = re.compile(r"^(?:sparse_write\s+mmc\s+\S+|mmc\s+write\.p\s+\S+)\s+([a-zA-Z][a-zA-Z0-9_]+)")
for line in script.splitlines():
    s = line.strip()
    if s.startswith("#"):
        name = s.lstrip("#").strip().lower()
        if re.fullmatch(r"(sboot|mboot|recovery|boot|dtb|linux_rootfs_[ab]|system|vendor|userdata|tvconfig|tee|optee|metadata)", name):
            group = name
    m = rx_load.match(s)
    if m:
        offset, length = int(m[1], 16), int(m[2], 16)
        record = {"offset": offset, "length": length, "label": group, "write_target": ""}
        if offset+length>size:
            record["warning"]="extends beyond BIN"
        commands.append(record)
        last=record
        continue
    if last:
        m = rx_target.match(s)
        if m:
            last["write_target"] = m[1]
            if last["label"] == "unknown":
                last["label"] = m[1]
            last=None
report += ["BIN: %d bytes, %d load segments" % (size,len(commands)), ""]
with bin_path.open("rb") as source:
    for record in commands:
        source.seek(record["offset"])
        head = source.read(128)
        record["magic"] = head[:16].hex()
        if len(head)>=28 and head[:4]==b"\x3a\xff\x26\xed":
            h = struct.unpack_from("<IHHHHIIII", head)
            record["sparse"] = {
                "version":"%d.%d" % (h[1],h[2]),
                "file_header_size":h[3], "chunk_header_size":h[4],
                "block_size":h[5], "total_blocks":h[6], "total_chunks":h[7],
                "logical_bytes":h[5]*h[6]
            }
        if head[:4] in (b"hsqs", b"sqsh"):
            record["filesystem"]="squashfs"
        if head[:8]==b"ANDROID!":
            record["image"]="Android boot image"
        if head[:4] == b"\xd0\x0d\xfe\xed":
            record["image"]="device tree blob"
(output/"partition_map.json").write_text(json.dumps(commands,ensure_ascii=False,indent=2),encoding="utf-8")
for x in commands:
    report.append("- %s: 0x%x + 0x%x (%d MiB) %s %s" % (
        x["label"],x["offset"],x["length"],x["length"]//1024**2,
        "-> "+x["write_target"] if x["write_target"] else "",
        "sparse=%s logical=%d MiB" % (x["sparse"]["version"],x["sparse"]["logical_bytes"]//1024**2) if "sparse" in x else x.get("filesystem","")))
report += ["","## SquashFS root file systems", ""]
rootfs = [x for x in commands if x.get("filesystem")=="squashfs"]
with bin_path.open("rb") as source:
    for idx,x in enumerate(rootfs):
        if x["length"]>256*1024**2:
            continue
        target=Path("/tmp")/("et32-rootfs-%d.squashfs"%idx)
        source.seek(x["offset"])
        with target.open("wb") as dst:
            remaining=x["length"]
            while remaining:
                d=source.read(min(4*1024**2,remaining))
                if not d: break
                dst.write(d); remaining-=len(d)
        code,listing=run(["unsquashfs","-ll",str(target)],120)
        (output/("squashfs_%d_listing.txt"%idx)).write_text(listing[:1000000],encoding="utf-8")
        report.append("image %d label %s: unsquashfs exit %s; listing saved" % (idx,x["label"],code))
        if code==0:
            where=Path("/tmp")/("et32-rootfs-%d-extracted"%idx)
            code,log=run(["unsquashfs","-no-xattrs","-d",str(where),str(target)],180)
            report.append("  filesystem extraction result: %d" % code)
            if code==0:
                allfiles=sorted(str(p.relative_to(where)) for p in where.rglob("*") if p.is_file())
                (output/("squashfs_%d_paths.txt"%idx)).write_text("\n".join(allfiles),encoding="utf-8")
                report.append("  regular files: %d" % len(allfiles))
report += ["", "## Android sparse fragments"]
for label in ("system","vendor"):
    fragments = [x for x in commands if x.get("write_target")==label and "sparse" in x]
    report.append("%s: %d fragments, %d MiB stored, %d MiB logical" % (
        label,len(fragments),sum(x["length"] for x in fragments)//1024**2,
        sum(x["sparse"]["logical_bytes"] for x in fragments)//1024**2))
    if not fragments: continue
    # Do not put huge image files into Git; retain small structural reports only.
    # Carve first fragment to read its filesystem header and EXT4 superblock.
    first = fragments[0]
    source = bin_path.open("rb"); source.seek(first["offset"])
    tmp = Path("/tmp/et32-"+label+"-first.sparse")
    with tmp.open("wb") as dst:
        remaining=first["length"]
        while remaining:
            data=source.read(min(4*1024**2,remaining))
            if not data: break
            dst.write(data); remaining-=len(data)
    source.close()
    raw=Path("/tmp/et32-"+label+"-first.raw")
    code,txt=run(["simg2img",str(tmp),str(raw)],240)
    report.append("%s first sparse conversion: %s %s" % (label,code,txt[:500]))
    if code==0 and raw.exists():
        report.append("  raw first fragment: %d MiB" % (raw.stat().st_size//1024**2))
        code2,out2=run(["debugfs","-R","ls -p /",str(raw)],90)
        (output/("debugfs_"+label+"_first.txt")).write_text(out2,encoding="utf-8")
        report.append("  debugfs root listing status: "+str(code2))
(output/"partition_report.md").write_text("\n".join(report)+"\n",encoding="utf-8")
print("\n".join(report)[:20000])
