#!/usr/bin/env python3
"""Read-only focused ET32 configuration/service/APK audit, redact public output."""
from pathlib import Path
import re,json,subprocess
out=Path("analysis/ET32")
images={"system":"/tmp/et32-system.ext4","vendor":"/tmp/et32-vendor.ext4"}
def call(args):
    p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,errors="replace",timeout=100)
    return p.returncode,p.stdout,p.stderr
def cat(part,p):
    rc,s,e=call(["debugfs","-R","cat "+p,images[part]])
    return s if rc==0 and "File not found" not in e else ""
def ls(part,p):
    rc,s,e=call(["debugfs","-R","ls -p "+p,images[part]])
    return [x.split("/")[5] for x in s.splitlines() if len(x.split("/"))>5 and x.split("/")[5] not in (".","..","")]
def selected(s):
    return [x.strip()[:300] for x in s.splitlines() if re.search(r"(trape|keystone|focus|auto.?focus|camera|hot.?key|remote|keycode|key_map|hdmi|gpio|project|display|geometry|angle|usb.*adb|persist|^service |^on |^import )",x,re.I) and not re.search(r"(password|passwd|secret|token|serial|macaddr|private)",x,re.I)][:100]
report=["# ET32 Focus, keystone, remote and service audit",
        "Read-only extracted data. APK code is not executed. This is a modified firmware image."]
paths=["ZYCustom.ini","trapezoidcorrect_points_offset.ini","customer_keymap.ini","hot-key-info.ini","ManualEnterFactory.ini","feature_default.xml","tv-settings-configs.xml","adb_enable_on.ini","adb_enable_off.ini","boot.conf","rc.local","utopia.conf"]
for name in paths:
    s=cat("vendor","/etc/"+name)
    report+=["","## /vendor/etc/"+name,"Bytes: "+str(len(s))]
    lines=selected(s)
    if lines:report+=lines[:50]
    else:report+=["Keys: "+", ".join(x.split("=")[0].strip() for x in s.splitlines()[:20] if "=" in x)]
report+=["","## /vendor/etc/init services"]
rc_files=[n for n in ls("vendor","/etc/init") if n.endswith(".rc")]
report.append("RC files: "+str(len(rc_files)))
for n in rc_files:
    s=cat("vendor","/etc/init/"+n);hits=selected(s)
    if hits:report += ["","### "+n,*hits[:25]]
report+=["","## Relevant Android app packages"]
paths=["/system/priv-app/AutoFocus3","/system/priv-app/ZYSetting","/system/priv-app/TvSettingsPlus",
       "/system/app/ZYCustomUI","/system/app/NLHotkeyService","/system/app/ZYYTBLauncher",
       "/system/app/NLTvTestingTools","/system/app/NLAutoTest","/system/app/ZYFileManager"]
packages={}
for p in paths:
    names=ls("system",p)
    report+=["","### "+p,"Files: "+", ".join(names[:20])]
    for name in names:
        if not name.endswith(".apk"):continue
        dest="/tmp/ET32-"+p.split("/")[-1]+".apk"
        rc,s,e=call(["debugfs","-R","dump -p "+p+"/"+name+" "+dest,images["system"]])
        if rc!=0:continue
        rc,s,e=call(["aapt","dump","badging",dest])
        interesting=[line for line in s.splitlines() if line.startswith(("package:","sdkVersion:","targetSdkVersion:","launchable-activity:","application-label:"))]
        packages[p]=interesting[:15]
        report+=interesting[:15]
(out/"projector_components.md").write_text("\n".join(report)+"\n",encoding="utf-8")
(out/"projector_apk_metadata.json").write_text(json.dumps(packages,indent=2,ensure_ascii=False),encoding="utf-8")
print("\n".join(report)[:18000])
