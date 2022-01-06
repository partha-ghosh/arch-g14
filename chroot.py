import re
import os

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
exec_cmd(f"cd /tmp && sudo -u {username} git clone https://aur.archlinux.org/yay.git && cd yay && sudo -u {username} makepkg -si")
exec_cmd(f"sudo -u {username} yay -S " + " ".join(aur))

exec_cmd("asusctl -c 60")

exec_cmd(
    "grub-install --target=x86_64-efi --bootloader-id=GRUB --efi-directory=/boot" + (' --removable --recheck' if removable else '') 
)
with open("/etc/default/grub", "a") as f:
    f.write("\nGRUB_DISABLE_OS_PROBER=false")
exec_cmd("grub-mkconfig -o /boot/grub/grub.cfg") 

exec_cmd("systemctl enable " + " ".join(services))

if removable:
    exec_cmd("mkdir /etc/systemd/journald.conf.d")
    with open("/etc/systemd/journald.conf.d/external.conf", "w") as f:
        f.write('''[Journal]
Storage=volatile
RuntimeMaxUse=30M
''')

# swapfile
if not os.path.exists(f'/home/{username}/swapfile'):
    os.system(f'dd if=/dev/zero of=/home/{username}/swapfile bs=1M count={16*1024} status=progress')
    os.system(f'chmod 600 /home/{username}/swapfile')
os.system(f'mkswap /home/{username}/swapfile')
os.system(f'swapon /home/{username}/swapfile')
with open('/etc/fstab', 'a') as f:
    f.write(f'\n/home/{username}/swapfile none swap defaults 0 0')

exec_cmd("exit")
