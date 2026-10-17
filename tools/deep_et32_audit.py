#!/usr/bin/env python3
"""ET32 APK and native-service decompilation, static only, no extracted code committed."""
import json,os,re,subprocess,zipfile,hashlib,xml.etree.ElementTree as ET
from pathlib import Path
OUT=Path("analysis/ET32/deep")
OUT.mkdir(parents=True,exist_ok=True)
TMP=Path("/tmp/et32-research")
TMP.mkdir(exist_ok=True)
IMG={"s":"/tmp/et32-system.ext4","v":"/tmp/et32-vendor.ext4"}
APPS={
"AutoFocus3":("s","/system/priv-app/AutoFocus3"),
"ZYSetting":("s","/system/priv-app/ZYSetting"),
"TvSettingsPlus":("s","/system/priv-app/TvSettingsPlus"),
"NLHotkeyService":("s","/system/app/NLHotkeyService"),
"ZYCustomUI":("s","/system/app/ZYCustomUI"),
"ZYYTBLauncher":("s","/system/app/ZYYTBLauncher"),
"NLTvTestingTools":("s","/system/app/NLTvTestingTools"),
"NLAutoTest":("s","/system/app/NLAutoTest"),
"Arbitratorservice":("s","/system/priv-app/Arbitratorservice"),
"NewLinkService":("s","/system/priv-app/NewLinkService"),
"ZYHBStore":("s","/system/app/ZYHBStore"),
"HBCastNew":("s","/system/app/HBCastNew"),
"MtkNetworkMonitorService":("s","/system/app/MtkNetworkMonitorService"),
"PowerService":("s","/system/app/PowerService"),
"WTProvision":("s","/system/app/WTProvision"),
"AutoPair":("s","/system/app/AutoPair"),
"BootAppSplashScreen":("s","/system/app/BootAppSplashScreen")}
DEEP=["AutoFocus3","ZYSetting","TvSettingsPlus","NLHotkeyService","ZYCustomUI","Arbitratorservice","NewLinkService","ZYHBStore","HBCastNew","MtkNetworkMonitorService","PowerService","ZYYTBLauncher"]
NATIVE=["trapezoidServer","trapezoidTest","trapezoid_save.sh","boa","cmdsrv","MtkRmServer","gpio_spi_read","gpio_spi_write"]
PATTERNS={
"focus":r"auto.?focus|keystone|trapezoid|motor|lens|camera",
"remote":r"KeyEvent|onKeyDown|onKeyUp|KEYCODE_|InputManager",
"device":r"/dev/|/sys/|/proc/|gpio|i2c|ioctl",
"privileged":r"Runtime.getRuntime|ProcessBuilder|su\b|setprop|SystemProperties|Settings.Global|Settings.Secure|ServiceManager",
"jni":r"System.loadLibrary|native\s+\w+\s*\(|JNI",
"network":r"HttpURLConnection|OkHttp|WebView|Socket\(|https?://|Retrofit",
"weak_security":r"setJavaScriptEnabled\(true\)|addJavascriptInterface|onReceivedSslError|handler.proceed\(|ALLOW_ALL_HOSTNAME_VERIFIER|StrictMode.permitAll",
"catch":r"catch\s*\("}
NS="{http://schemas.android.com/apk/res/android}"
PRIVATE=re.compile(r"password|passwd|credential|secret|token|authorization|private.?key|serial.?number|ssid",re.I)
URL=re.compile(r"https?://[\w.:-]+[^\s\"']*")
def run(cmd,timeout=120):
    try:
        r=subprocess.run(cmd,text=True,capture_output=True,timeout=timeout,errors="replace")
        return r.returncode,r.stdout,r.stderr
    except Exception as ex:return -1,"",str(ex)
def d(part,cmd):return run(["debugfs","-R",cmd,IMG[part]],60)
def listdir(part,path):
    rc,s,e=d(part,"ls -p "+path)
    return [f[5] for f in (line.split("/") for line in s.splitlines()) if len(f)>5 and f[5] not in ("",".","..")]
def copy(part,remote,target):
    rc,s,e=d(part,"dump -p "+remote+" "+str(target))
    return rc==0 and target.is_file()
def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
    return h.hexdigest()
def manifest(path):
    try:r=ET.parse(path).getroot()
    except Exception as e:return {"error":str(e)}
    app=r.find("application")
    obj={"package":r.get("package"),"permissions":[],"components":{},"flags":{},"shared_user_id":r.get(NS+"sharedUserId")}
    for e in r.findall("uses-permission"):
        if e.get(NS+"name"):obj["permissions"].append(e.get(NS+"name"))
    if app is not None:
        obj["flags"]={k:app.get(NS+k) for k in ("debuggable","allowBackup","usesCleartextTraffic","networkSecurityConfig") if app.get(NS+k)!=None}
        for kind in ("activity","service","receiver","provider"):
            obj["components"][kind]=[]
            for e in app.findall(kind):
                obj["components"][kind].append({"name":e.get(NS+"name"),"exported":e.get(NS+"exported"),"permission":e.get(NS+"permission"),"filters":len(e.findall("intent-filter"))})
    return obj
def java_scan(root):
    found={k:{"count":0,"sample":[]} for k in PATTERNS}
    urls=set()
    files=list(root.rglob("*.java")) if root.exists() else []
    for p in files:
        try:content=p.read_text(errors="replace")
        except Exception:continue
        for idx,line in enumerate(content.splitlines(),1):
            for k,rx in PATTERNS.items():
                if re.search(rx,line,re.I):
                    found[k]["count"]+=1
                    if len(found[k]["sample"])<12 and not PRIVATE.search(line):
                        excerpt=URL.sub("[URL]",line.strip())[:220]
                        found[k]["sample"].append({"file":str(p.relative_to(root)),"line":idx,"code":excerpt})
            for u in URL.findall(line):
                try:urls.add(u.split("/")[2].lower().split("?")[0][:100])
                except:pass
    return {"files":len(files),"patterns":found,"url_domains":sorted(urls)[:80]}
results={"apps":{},"native":{}}
for name,(part,folder) in APPS.items():
    apks=[x for x in listdir(part,folder) if x.endswith(".apk")]
    obj={"source":folder}
    if not apks:
        obj["error"]="APK not found"
        results["apps"][name]=obj;continue
    apk=TMP/(name+".apk")
    if not copy(part,folder+"/"+apks[0],apk):
        obj["error"]="APK extract failed";results["apps"][name]=obj;continue
    obj["sha256"]=sha(apk);obj["size"]=apk.stat().st_size
    rc,s,e=run(["aapt","dump","badging",str(apk)])
    for k,rx in {"package":r"package: name='([^']+)'","min_sdk":r"sdkVersion:'([^']+)'","target_sdk":r"targetSdkVersion:'([^']+)'"}.items():
        m=re.search(rx,s)
        if m:obj[k]=m[1]
    with zipfile.ZipFile(apk) as z:obj["libraries"]=[x for x in z.namelist() if x.endswith(".so")][:60]
    manifest_dir=TMP/("manifest_"+name)
    rc,s,e=run(["apktool","d","-f","-s",str(apk),"-o",str(manifest_dir)],90)
    if rc==0:obj["manifest"]=manifest(manifest_dir/"AndroidManifest.xml")
    else:obj["manifest_error"]=(s+e)[-500:]
    if name in DEEP:
        src=TMP/("java_"+name)
        rc,s,e=run(["/opt/jadx/bin/jadx","--no-res","--no-imports","--threads-count","2","-d",str(src),str(apk)],170)
        obj["jadx_status"]=rc;obj["jadx_output"]=(s+e)[-350:]
        obj["java"]=java_scan(src/"sources")
    results["apps"][name]=obj
    print("APK",name,obj.get("package"),obj.get("jadx_status"),flush=True)
for name in NATIVE:
    remote="/bin/"+name;path=TMP/("native_"+name)
    if not copy("v",remote,path):continue
    rc,s,e=run(["file",str(path)])
    rc,libraries,e=run(["readelf","-d",str(path)])
    rc,strings,e=run(["strings","-a","-n","7",str(path)])
    x=[x[:180] for x in strings.splitlines() if re.search(r"focus|trapezoid|keystone|motor|gpio|http|listen|bind|/dev/|/sys/|/proc/|ota|i2c|port|remote|keycode",x,re.I) and not PRIVATE.search(x)]
    results["native"][name]={"size":path.stat().st_size,"type":s.strip(),"sha256":sha(path),
     "needed":re.findall(r"Shared library: \[([^\]]+)\]",libraries),"matched_strings":x[:80]}
    print("BIN",name,flush=True)
(OUT/"static_analysis.json").write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf8")
lines=["# ET32 detailed read-only APK and service analysis",
       "A static decompilation of the modified ET32 firmware; observed references are not proof of execution.",
       "","## Overview","",
       "| App | Package | Target SDK | Permissions | Exported / total components | Java files |",
       "|---|---|---:|---:|---:|---:|"]
for name,obj in results["apps"].items():
    m=obj.get("manifest",{})
    comp=[x for xs in m.get("components",{}).values() for x in xs]
    export=sum(1 for x in comp if x.get("exported")=="true")
    lines.append("| "+name+" | "+str(obj.get("package","?"))+" | "+str(obj.get("target_sdk","?"))+" | "+str(len(m.get("permissions",[])))+" | "+str(export)+"/"+str(len(comp))+" | "+str(obj.get("java",{}).get("files",0))+" |")
lines+=["","## Per-app detail"]
for name,obj in results["apps"].items():
    lines+=["","### "+name,"Package: "+str(obj.get("package","?"))]
    m=obj.get("manifest",{})
    lines+=["Android flags: "+str(m.get("flags",{})),"Shared user: "+str(m.get("shared_user_id")),
            "Permissions: "+", ".join(m.get("permissions",[]))[:1300]]
    for kind in ("service","receiver","provider"):
        names=[x.get("name","") for x in m.get("components",{}).get(kind,[])]
        if names:lines.append(kind+": "+", ".join(names)[:1100])
    exposed=[kind+":"+str(x["name"]) for kind,xs in m.get("components",{}).items() for x in xs if x.get("exported")=="true" and not x.get("permission")]
    if exposed:lines.append("Exported with no component permission (verify intent validation): "+", ".join(exposed)[:1000])
    j=obj.get("java",{})
    if j:
        lines.append("JADX status "+str(obj.get("jadx_status"))+"; classes/files "+str(j.get("files",0)))
        lines.append("Matched patterns "+json.dumps({k:v["count"] for k,v in j.get("patterns",{}).items()}))
        lines.append("URL hostnames "+", ".join(j.get("url_domains",[]))[:700])
        for k in ("focus","remote","device","privileged","jni","weak_security"):
            samples=j.get("patterns",{}).get(k,{}).get("sample",[])[:4]
            for ex in samples:lines.append(k+" "+ex["file"]+":"+str(ex["line"])+" "+ex["code"].replace("\n"," "))
lines+=["","## Native service binaries"]
for name,info in results["native"].items():
    lines+=["","### "+name,"Type: "+info["type"],"Linked: "+", ".join(info["needed"])]
    for ln in info["matched_strings"][:30]:lines.append("- "+ln.replace("<","(").replace("> ",") "))
(OUT/"static_analysis.md").write_text("\n".join(lines)+"\n",encoding="utf8")
print("FINISHED",len(results["apps"]),len(results["native"]),flush=True)
