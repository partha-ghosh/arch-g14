# arch-g14

## Configs
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
   <const>hintslight</const>
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
 <dir>~/.fonts</dir>
</fontconfig>
```
Write the above to ~/.config/fontconfig/fonts.conf

Turns off hinting, and sets the lcddefault filter style.
