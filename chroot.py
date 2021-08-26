import re

from config import *

# time zone setup
exec_cmd("ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime")
exec_cmd("hwclock --systohc")

# localization
with open('/etc/locale.gen', 'a') as f:
    f.write('en_US.UTF-8 UTF-8\nen_US ISO-8859-1\n')
exec_cmd("locale-gen")
with open('/etc/locale.conf', 'a') as f:
    f.write('LANG=en_US.UTF-8\n')

# Network configuration
with open('/etc/hostname', 'a') as f:
    f.write(hostname + '\n')
with open('/etc/hosts', 'a') as f:
    f.write("""
127.0.0.1	localhost
::1		localhost
127.0.1.1	""" + hostname + ".localdomain	" + hostname + '\n')

with open("/etc/modprobe.d/g14-prohibited-drivers.conf", "w") as f:
    f.write('''blacklist nouveau
blacklist nvidiafb
blacklist rivafb
blacklist i2c_nvidia_gpu
''')

with open("/etc/modprobe.d/g14-nvidia.conf", "w") as f:
    f.write('''options nvidia "NVreg_DynamicPowerManagement=0x02"
''')
    
# Initramfs
exec_cmd("mkinitcpio -P")

# Root password
exec_cmd("passwd")
exec_cmd(
    "useradd -m -g users -G wheel,video,audio,optical,storage,power -s /bin/bash "
    + username)
exec_cmd("passwd " + username)
exec_cmd("EDITOR=nano visudo")

exec_cmd("pacman -Syyu " + " ".join(packages))

if bootloader == 'grub':
    exec_cmd(
        "grub-install --target=x86_64-efi --bootloader-id=GRUB --efi-directory=/boot"
    )
    exec_cmd("grub-mkconfig -o /boot/grub/grub.cfg") 

exec_cmd("su - " + username)
exec_cmd('export MAKEFLAGS="-j16"')
exec_cmd("mkdir aur && cd aur")
exec_cmd("git clone https://aur.archlinux.org/rog-core.git && cd rog-core && makepkg -si && cd ..")
exec_cmd("sudo systemctl enable rog-core.service")
exec_cmd("git clone https://aur.archlinux.org/asusctl-git.git && cd  asusctl-git && makepkg -si && cd ..")

exec_cmd("systemctl enable " + " ".join(services))

exec_cmd("exit")
