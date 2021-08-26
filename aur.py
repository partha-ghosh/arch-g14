from config import *

exec_cmd('export MAKEFLAGS="-j16"')
exec_cmd("mkdir aur && cd aur")
exec_cmd("git clone https://aur.archlinux.org/rog-core.git && cd rog-core && makepkg -si && cd ..")
exec_cmd("sudo systemctl enable rog-core.service")
exec_cmd("git clone https://aur.archlinux.org/asusctl-git.git && cd  asusctl-git && makepkg -si && cd ..")
exec_cmd("asusctl -c 60")
