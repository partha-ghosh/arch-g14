# create a partition in the disk using "cfdisk /dev/sda" before running the script

from config import *

exec_cmd("timedatectl set-ntp true")

# format partitions
exec_cmd("mkfs.fat -F32 " + efi)
exec_cmd("mkfs.ext4 " + ('-O "^has_journal" ' if removable else "") + root)
if format_home:
    exec_cmd("mkfs.ext4 " + ('-O "^has_journal" ' if removable else "") +home)

# mount partitions
exec_cmd("mount " + root + " /mnt")
exec_cmd("mkdir -p /mnt/boot")
exec_cmd("mount " + efi + " /mnt/boot")
if home:
    exec_cmd("mkdir /mnt/home")
    exec_cmd("mount " + home + " /mnt/home")

exec_cmd('''cat >> /etc/pacman.conf <<EOF
[g14]
SigLevel = DatabaseNever Optional TrustAll
Server = https://arch.asus-linux.org
EOF
''')

exec_cmd(
    "pacstrap -i /mnt base base-devel linux-g14 linux-g14-headers linux-firmware python git sudo pacman-contrib nano "
    + cpu + "-ucode")

exec_cmd("genfstab -U /mnt >> /mnt/etc/fstab")

exec_cmd("cp /etc/pacman.conf /mnt/etc/pacman.conf")
if removable:
    exec_cmd("mv mkinitcpio_removable.conf /mnt/etc/mkinitcpio.conf")
else:
    exec_cmd("mv mkinitcpio.conf /mnt/etc/mkinitcpio.conf")
exec_cmd("mv chroot.py /mnt")
exec_cmd("mv config.py /mnt")
exec_cmd("arch-chroot /mnt python ./chroot.py")
exec_cmd("umount -R /mnt")
exec_cmd("reboot")
