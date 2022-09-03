# arch-g14

## Configs
### Better Font Rendering
```
<?xml version='1.0'?>
<!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
<fontconfig>
 <match target="font">
  <edit mode="assign" name="rgba">
   <const>rgb</const>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="hinting">
   <bool>false</bool>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="hintstyle">
   <const>hintnone</const>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="antialias">
   <bool>true</bool>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="lcdfilter">
   <const>lcddefault</const>
  </edit>
 </match>
 <match target="font">
    <test name="weight" compare="more">
        <const>medium</const>
    </test>
    <edit name="autohint" mode="assign">
        <bool>false</bool>
    </edit>
 </match>
 <dir>~/.fonts</dir>
</fontconfig>
```
Write the above to ~/.config/fontconfig/fonts.conf

Turns off hinting, and sets the lcddefault filter style.


SSH

serveo
```
import random, string, getpass

password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))
alias = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
! echo root:$password | chpasswd

! apt-get install -qq -o=Dpkg::Use-Pty=0 openssh-server pwgen > /dev/null
! mkdir -p /var/run/sshd
! echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
! echo "LD_LIBRARY_PATH=/usr/lib64-nvidia" >> /root/.bashrc && echo "export LD_LIBRARY_PATH" >> /root/.bashrc
get_ipython().system_raw('/usr/sbin/sshd -D &')

print('sshpass -p {} ssh -o "StrictHostKeyChecking no" -J serveo.net root@{}'.format(password, alias))
! ssh -o "StrictHostKeyChecking no" -R $alias:22:localhost:22 serveo.net
```

ngrok
```
#useradd partha
#passwd partha
#usermod -aG sudo partha
!sudo apt update && sudo apt install -y openssh-server
!echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
!echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
!echo "X11Forwarding yes" >> /etc/ssh/sshd_config
!echo "X11UseLocalhost no" >> /etc/ssh/sshd_config
!passwd root
!sudo service ssh start
!curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
!ngrok config add-authtoken *****************
!ngrok tcp 22 --region=eu
```

teleconsole
