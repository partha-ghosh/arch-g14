import os


def exec_cmd(cmd):
    print("\n>>> " + cmd)
    #input("Press Enter")
    os.system(cmd)

removable = False
format_home = False
format_efi = False
efi = "/dev/nvme0n1p1"
root = "/dev/nvme0n1p2"
home = "/dev/nvme0n1p3"

# cpu = "intel"
cpu = "amd"

hostname = "jarvis"
username = "partha"

services = [
    "acpid.service",
    "NetworkManager.service",
    "avahi-daemon.service",
    # "gdm.service",
    "bluetooth.service",
    "lightdm.service",
    "cups.service",
    "fstrim.timer",
    "nvidia-suspend.service",
    "nvidia-resume.service",
    "nvidia-hibernate.service"

]

packages = [
    # bootloader
    # ==========
    "grub",
    "efibootmgr",
    "os-prober",

    # network manager
    # ===============
    "networkmanager",
    # "network-manager-applet",

    # console programs
    # ================
    "bash-completion",
    #"ranger",
    "p7zip",

    # file sharing
    # ==================================
    "grsync",
    "wget",
    # "aria2",
    "youtube-dl",
    "uget",
    # "filezilla",
    # "deluge",
    # "python-cairo",

    # xorg
    # ====
    "xorg",
    # "xorg-xinit",
    # "xorg-server",
    # "xorg-xbacklight",

    # window managers
    # ===============
    # BSPWM
    # =====
    # "bspwm",
    # "sxhkd",
    # "feh",
    # "lightdm",
    # "lightdm-gtk-greeter",
    # "xclip",
    # "rxvt-unicode",
    # "pcmanfm",
    # "xarchiver",
    # "kupfer",

    # desktop environments
    # ====================
    # GNOME
    # =====
    # "gnome",
    # "gnome-extra",
    # XFCE
    # ====
    "xfce4",
    "xfce4-goodies",
    "xarchiver",
    "caja",
    "network-manager-applet",
    "lightdm",
    "lightdm-gtk-greeter",
    # MATE
    # ====
    # "mate",
    # "mate-extra",
    # "lightdm",
    # "lightdm-gtk-greeter",
    # KDE
    # ===
    # "plasma",
    # "kde-applications",
    # "sddm",
    # "packagekit-qt5",


    # video drivers
    # =============
    "xf86-video-amdgpu",
    "nvidia-dkms", 
    "nvidia-utils", 
    "nvidia-settings", 
    "nvidia-prime",
    # "xf86-video-intel",
    # "xf86-video-ati",

    # sound server
    # ============
    "pulseaudio",
    "pulseaudio-alsa",
    # "pulseaudio-bluetooth",
    # "alsa-utils",
    # "alsa-plugins",

    # file systems
    # ============
    "dosfstools",
    "mtools",
    "mtpfs",
    "ntfs-3g",
    "gvfs",

    # text editors
    # ============
    # "nano",
    # "neovim",
    "emacs",
    # "code",
    # "atom",

    # web browsers
    # ============
    # "w3m",
    "firefox",
    # "vivaldi",
    # "chromium",

    # audio/video players
    # ===================
    "mplayer",
    "vlc",

    # fonts
    # =====
    "fontconfig",
    # "ttf-dejavu",
    # "ttf-inconsolata", "ttf-fira-mono", "ttf-fira-code", "ttf-dejavu",
    # "ttf-roboto", "noto-fonts", "ttf-ubuntu-font-family", "gnu-free-fonts",
    # "adobe-source-code-pro-fonts", "ttf-linux-libertine",

    # graphics tools
    # ==============
    "inkscape",
    "gimp",
    "blender",
    "krita",
    "obs-studio",

    # doc tools
    # =========
    "texlive-most",
    "pandoc",
    "calibre",
    "texmacs",
    "libreoffice-fresh", "libreoffice-extension-writer2latex",
    # "zathura", "zathura-pdf-poppler", "zathura-djvu", "zathura-ps",
    # "okular",
    "evince",
    "xournalpp",

    # misc
    # ====
    # "nodejs",
    # "npm",
    # "python-pynvim",
    # "redshift",
    "synapse",
    "python-virtualenv",
    "keepassxc",
    "gparted",
    
    "acpid",
    "bluez",
    "bluez-utils",
    "cups",
    "asusctl",
    "archlinux-keyring",
    "arch-install-scripts"
]

aur = [
    "google-chrome",
    "write_stylus",
    "spotify",
    "zoom",
    "anki",
    "miniconda3",
    "visual-studio-code-bin",
]
