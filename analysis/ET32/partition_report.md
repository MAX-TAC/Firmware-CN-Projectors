# ET32 partition and filesystem inspection

BIN: 2453516320 bytes, 33 load segments

- sboot: 0x4000 + 0x2eb70 (0 MiB)  
- mboot: 0x33000 + 0x30e000 (3 MiB) -> MBOOT 
- mboot: 0x342000 + 0x800000 (8 MiB) -> tvcertificate 
- tvconfig: 0xb43000 + 0x2000000 (32 MiB) -> tvconfig 
- recovery: 0x2b44000 + 0x14ad000 (20 MiB) -> recovery 
- boot: 0x3ff2000 + 0xd8b800 (13 MiB) -> boot 
- optee: 0x4d7e000 + 0x1e39f0 (1 MiB) -> optee 
- optee: 0x4f62000 + 0xe460 (0 MiB) -> armfw 
- optee: 0x4f71000 + 0x10000 (0 MiB) -> RTPM 
- dtb: 0x4f82000 + 0x536d (0 MiB) -> dtb 
- dtb: 0x4f88000 + 0x8d010 (0 MiB) -> frc 
- linux_rootfs_a: 0x5016000 + 0x193b000 (25 MiB) -> linux_rootfs_a squashfs
- linux_rootfs_a: 0x6952000 + 0x14c0000 (20 MiB)  squashfs
- linux_rootfs_a: 0x7e13000 + 0x1e00000 (30 MiB)  
- system: 0x9c14000 + 0x95d63ac (149 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x131eb000 + 0x95ff36c (149 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x1c7eb000 + 0x928d61c (146 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x25a79000 + 0x95ff858 (149 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x2f079000 + 0x90b0114 (144 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x3812a000 + 0x95ff174 (149 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x4172a000 + 0x95ff0cc (149 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x4ad2a000 + 0x9391408 (147 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x540bc000 + 0x86e3440 (134 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x5c7a0000 + 0x934114c (147 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x65ae2000 + 0x95ff334 (149 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x6f0e2000 + 0x95ff174 (149 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x786e2000 + 0xfee07c (15 MiB) -> system sparse=1.0 logical=2524 MiB
- system: 0x796d1000 + 0xe0c4 (0 MiB) -> cache sparse=1.0 logical=100 MiB
- vendor: 0x796e0000 + 0x95ff3d0 (149 MiB) -> vendor sparse=1.0 logical=350 MiB
- vendor: 0x82ce0000 + 0x64d5044 (100 MiB) -> vendor sparse=1.0 logical=350 MiB
- vendor: 0x891b6000 + 0x8c00000 (140 MiB) -> tvservice 
- vendor: 0x91db7000 + 0x500000 (5 MiB) -> factory_a 
- userdata: 0x922b8000 + 0x1221a4 (1 MiB) -> userdata sparse=1.0 logical=4182 MiB

## SquashFS root file systems

image 0 label linux_rootfs_a: unsquashfs exit 0; listing saved
  filesystem extraction result: 0
  regular files: 1007
image 1 label linux_rootfs_a: unsquashfs exit 0; listing saved
  filesystem extraction result: 0
  regular files: 66

## Android sparse fragments
system: 13 fragments, 1786 MiB stored, 32812 MiB logical
system first sparse conversion: 0 
  raw first fragment: 2524 MiB
  debugfs root listing status: 0
vendor: 2 fragments, 250 MiB stored, 700 MiB logical
vendor first sparse conversion: 0 
  raw first fragment: 350 MiB
  debugfs root listing status: 0
