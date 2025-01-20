# Wiper
Utility to wipe a hard disk / Flash Drive
This Program builds only on a system with GNU make.
It makes a standalone executable name wiper which can be run on a system without any other external dependencies.
The command to build the executable is :
    make
The command to install the executable is :
    make install

# Usage after installation
With admin/root privileges, run:
wipe -d <device file> -b <block_size>
examples:
    The following are examples for wiping an entire drive.
    wipe -d /dev/sda -b 500K
    wipe -d /dev/nvme0n1 -b 4M

    The following are examples for wiping just a partition.
    wipe -d /dev/sda1 -b 1M
    wipe -d /dev/nvme0n1p1 -b 2M

