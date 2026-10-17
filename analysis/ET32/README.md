# Touyinger ET32 firmware research

Static inspection of **YG_6M046.zip**, containing **YG_6M046.bin** from the ET32 firmware discussion.
This is a modified MStar update image, not necessarily the original factory firmware.

## Recovered Android images

Download from [Touyinger-ET32-unpacked](https://github.com/MAX-TAC/Firmware-CN-Projectors/releases/tag/Touyinger-ET32-unpacked):

- ET32-system.ext4.zst — complete reassembled Android system image (logical size 2,646,605,824 bytes).
- ET32-vendor.ext4.zst — complete reassembled vendor image (logical size 367,001,600 bytes).
- SHA256SUMS.txt — hashes of the compressed assets.

The images were reconstructed by overlaying the RAW and FILL blocks from all Android sparse fragments at their logical offsets. They are **analysis-only images**, not ready-to-flash update files.

On Linux:

    sha256sum -c SHA256SUMS.txt
    zstd -d ET32-system.ext4.zst -o ET32-system.ext4
    zstd -d ET32-vendor.ext4.zst -o ET32-vendor.ext4
    sudo mkdir -p /mnt/et32-system /mnt/et32-vendor
    sudo mount -o loop,ro ET32-system.ext4 /mnt/et32-system
    sudo mount -o loop,ro ET32-vendor.ext4 /mnt/et32-vendor

Unmount after browsing. Do not flash these images to another projector.

## Reports

- [firmware_report.md](firmware_report.md) — original ZIP, BIN hashes, detected signatures.
- [partition_report.md](partition_report.md) — bootloader commands, image offsets, SquashFS extraction, sparse fragments.
- [partition_map.json](partition_map.json) — machine-readable MStar partition mapping.
- [android_audit.md](android_audit.md) — reassembled Android image inspection and build properties.
- [mstar_upgrade_commands.txt](mstar_upgrade_commands.txt) — text update script embedded at offset zero.
- listing_*.txt — read-only filesystem directory listings.
- [vendor_hal_manifest.xml](vendor_hal_manifest.xml) — device HAL declarations.

## Key observations

- Android 9, API 28; security patch level 2021-01-05; build 2025-03-07.
- Build type is userdebug with dev-keys. The reported build fingerprint disagrees with the Android 9 build.
- vendor/build.prop contains ro.adb.secure=0; update boot arguments request androidboot.selinux=permissive.
- Firmware references mt5862_bga_1g and reports model NL_MTK9255_D1E8. Neither string alone proves the physical SoC.
- Vendor and system contain MediaTek/MStar TV components, proprietary projector applications, and assorted Google/streaming components.
- Signatures of proprietary DRM HALs in a manifest do not establish certification or Widevine level.

These findings do **not** prove the D11 Master uses compatible hardware or firmware. Do not flash ET32 firmware to FlixTone D11.

## Reproduction

The repository includes read-only GitHub Actions tools:

- tools/analyze_et32.py
- tools/extract_et32.py
- tools/reassemble_et32.py

The workflows retrieve the original release asset, verify its SHA-256, then inspect the image without executing its binaries. Large reconstructed images are stored in GitHub Releases, not committed into Git history.
