#!/usr/bin/env python3
"""Read-only structural inspection of a projector firmware ZIP and its payloads."""
import collections
import hashlib
import json
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import time
import zipfile

archive = Path(sys.argv[1]).resolve()
out = Path("analysis/ET32")
dest = Path("/tmp/et32-unpacked")
out.mkdir(parents=True, exist_ok=True)
dest.mkdir(parents=True, exist_ok=True)
max_uncompressed = 12 * 1024**3
ascii_strings = re.compile(rb"[\x20-\x7e]{8,240}")
interesting = re.compile(rb"android|ro\.build|ro\.product|mstar|mediatek|mt9269|mt9660|u-boot|mboot|squashfs|busybox|selinux|recovery|bootloader|rootfs|hdmi|keystone|update|upgrade|partition|vendor|system", re.I)
magic = {
    b"hsqs": "SquashFS LE", b"sqsh": "SquashFS BE",
    b"UBI#": "UBI", b"ANDROID!": "Android boot",
    b"\x3a\xff\x26\xed": "Android sparse",
    b"\xd0\x0d\xfe\xed": "DTB", b"\x1f\x8b\x08": "gzip",
    b"\x7fELF": "ELF", b"PK\x03\x04": "ZIP",
}
def hsh(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8*1024**2), b""):
            h.update(chunk)
    return h.hexdigest()
def size(n):
    return "%.1f MiB" % (n / 1024**2)
def command(args, timeout=120):
    try:
        p = subprocess.run(args, capture_output=True, text=True, errors="replace", timeout=timeout)
        return ("exit=%s\n%s%s" % (p.returncode, p.stdout, p.stderr))[:200000]
    except Exception as ex:
        return "ERROR: %s" % ex
def signatures(path):
    offsets = {label: [] for label in magic.values()}
    strings = collections.OrderedDict()
    overlap = b""
    offset = 0
    with path.open("rb") as f:
        while True:
            block = f.read(4 * 1024**2)
            if not block:
                break
            data = overlap + block
            base = offset - len(overlap)
            for marker, label in magic.items():
                pos = 0
                while len(offsets[label]) < 30:
                    pos = data.find(marker, pos)
                    if pos == -1:
                        break
                    actual = base + pos
                    if actual >= 0 and actual not in offsets[label]:
                        offsets[label].append(actual)
                    pos += 1
            if len(strings) < 500:
                for m in ascii_strings.finditer(data):
                    value = m.group()
                    if interesting.search(value):
                        s = value.decode("ascii", errors="replace")
                        strings.setdefault(s, base + m.start())
                        if len(strings) >= 500:
                            break
            overlap = data[-256:]
            offset += len(block)
    return offsets, strings

report = ["# Touyinger ET32 — static firmware triage",
          "Run UTC: " + time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "Archive: %s; size %s; sha256 %s" % (archive.name, size(archive.stat().st_size), hsh(archive))]
with zipfile.ZipFile(archive) as z:
    items = z.infolist()
    total = sum(i.file_size for i in items)
    report.append("ZIP members: %d, declared uncompressed size: %s" % (len(items), size(total)))
    if len(items) > 30000 or total > max_uncompressed:
        raise ValueError("ZIP exceeds extraction safety limits")
    manifest = []
    for i in items:
        p = Path(i.filename)
        if p.is_absolute() or ".." in p.parts or "\\" in i.filename:
            raise ValueError("Unsafe path in ZIP: " + i.filename)
        if stat.S_IFMT(i.external_attr >> 16) == stat.S_IFLNK:
            raise ValueError("ZIP symlink rejected: " + i.filename)
        manifest.append({"name": i.filename, "size": i.file_size, "compressed": i.compress_size, "crc": hex(i.CRC)})
    (out / "zip_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    for i in items:
        target = dest / i.filename
        if i.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        with z.open(i) as source, target.open("wb") as sink:
            shutil.copyfileobj(source, sink, 1024 * 1024)

files = sorted((f for f in dest.rglob("*") if f.is_file()), key=lambda f: -f.stat().st_size)
report += ["", "## Extracted archive files"]
for f in files[:200]:
    report.append("- %s: %s" % (f.relative_to(dest), size(f.stat().st_size)))
for f in files:
    if f.stat().st_size < 65536:
        continue
    name = re.sub("[^a-zA-Z0-9_.-]", "_", f.name)
    report += ["", "## " + str(f.relative_to(dest)),
               "Size: %s; sha256 %s" % (size(f.stat().st_size), hsh(f))]
    report.append("file: " + command(["file", "-k", str(f)], 30))
    with f.open("rb") as stream:
        header = stream.read(256)
    (out / ("header_" + name + ".hex")).write_text(header.hex(" ") + "\n", encoding="ascii")
    if f.stat().st_size <= 5 * 1024**3:
        hits, words = signatures(f)
        visible = {k: [hex(p) for p in v] for k, v in hits.items() if v}
        report.append("Signatures: " + json.dumps(visible))
        (out / ("strings_" + name + ".txt")).write_text(
            "\n".join("0x%x  %s" % (offset, word) for word, offset in words.items()), encoding="utf-8")
    if f.stat().st_size > 16 * 1024**2:
        (out / ("binwalk_" + name + ".txt")).write_text(command(["binwalk", str(f)], 360), encoding="utf-8")
        report.append("Binwalk report saved separately")
(out / "firmware_report.md").write_text("\n\n".join(report) + "\n", encoding="utf-8")
print("\n".join(report)[:25000])
