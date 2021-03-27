```
———
move existing Un1Gfn-network/cgi to Un1Gfn-network/cgi-legacy
create new Un1Gfn-network/cgi
———
https://github.com/boutell/cgic
https://stackoverflow.com/q/2265038
Makefile pie libcgic.so pkg-config cgic.pc
———
https://github.com/boazsegev/facil.io
https://facil.io/
submit to AUR
———
https://aur.archlinux.org/packages/kore/
https://github.com/jorisvink/kore
https://kore.io/
———
https://aur.archlinux.org/packages/kcgi
https://github.com/kristapsdz/kcgi
https://kristaps.bsd.lv/kcgi
———
https://github.com/search?l=C&o=desc&q=web+framework&s=stars&type=Repositories
https://github.com/search?l=C&o=desc&q=cgi&s=stars&type=Repositories
———
https://developer.mozilla.org/docs/Learn/Forms
———
```

Stunnel

```bash
su -
rm -fv /etc/stunnel/selfsigned*
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/stunnel/selfsigned.key -out /etc/stunnel/selfsigned.crt
ls -l /etc/stunnel/selfsigned*
```

[httpd.conf reference](https://git.busybox.net/busybox/tree/networking/httpd.c)

http://httpbin.org/

```bash
# busybox httpd -f -vv -p 8080 -h /home/darren/ios/
sudo busybox httpd -f -vv -p 80 -h . -c ./httpd.conf
# sudo busybox httpd -f -vv -p 80 -u root:root -h /home/darren/cm-exp01 -c /home/darren/cm-exp01/httpd.conf
```

```bash
dir.sh
```

```bash
function getsrv {
  curl -s --proxy 'socks5://127.0.0.1:1080' -I "$1" | grep -i serv
}
getsrv 'https://www.gnu.org/'     # Apache/2.4.7
getsrv 'https://git.busybox.net/' # Apache
getsrv 'https://www.kernel.org/'  # nginx
getsrv 'https://duckduckgo.org/'  # nginx
```

[http.server](https://docs.python.org/3/library/http.server.html#http-server-cli)
```bash
sudo python -m http.server 80
```

zip -s 50m PacketTracer-7.3.0.zip PacketTracer-7.3.0-win64-setup.exe
zip -P 'CaiXuKun' PacketTracer-7.3.0.zip PacketTracer-7.3.0-win64-setup.exe


[libimobiledevice](http://www.libimobiledevice.org/)
* [cgit](https://cgit.libimobiledevice.org/)
* [ArchWiki](https://wiki.archlinux.org/index.php/IOS)
* [gio mount](https://forums.linuxmint.com/viewtopic.php?t=275682)
* [Debian Wiki](https://wiki.debian.org/iPhone#mount-iphone.sh_script)

Mount
```bash
lsusb -v -d 05ac:12ab
idVendor=$(lsusb -v 2>/dev/null | awk '/idVendor.*Apple/{print $2; exit}')
iSerial=$(lsusb -v -d $idVendor: 2>/dev/null | awk '/iSerial\s+\S+\s+\S/{print $3; exit}')
gio mount afc://$iSerial:1
gio mount afc://$iSerial:3
gio mount -l
```

Transfer
```bash
cp -v <FILE> /run/user/1000/gvfs/!(*port*)/Downloads
```

Unmount
```bash
gio mount -u /run/user/1000/gvfs/'afc:host='*
gio mount -l
```

Details
```bash
gio mount -l
Drive(0): KBG30ZMV256G TOSHIBA
  Type: GProxyDrive (GProxyVolumeMonitorUDisks2)
Volume(0): Documents on iPad
  Type: GProxyVolume (GProxyVolumeMonitorAfc)
  Mount(0): Documents on iPad -> afc://f5e2d8c967e2b00e0bfb20eb7289fa9d25887769:3/
    Type: GProxyShadowMount (GProxyVolumeMonitorAfc)
Mount(1): Documents on iPad -> afc://f5e2d8c967e2b00e0bfb20eb7289fa9d25887769:3/
  Type: GDaemonMount
Mount(2): iPad -> afc://f5e2d8c967e2b00e0bfb20eb7289fa9d25887769/
  Type: GDaemonMount

gio mount -il
[...]

ls -Al /run/user/1000/gvfs/
total 0
drwx------ 1 darren darren 384 Apr  6 03:01 'afc:host=f5e2d8c967e2b00e0bfb20eb7289fa9d25887769'
drwx------ 1 darren darren   0 Jan  1  1970 'afc:host=f5e2d8c967e2b00e0bfb20eb7289fa9d25887769,port=3'

ls -Al /run/user/1000/gvfs/!(*port*)
total 0
drwx------ 1 darren darren 224 Apr 28 13:13 Books
drwx------ 1 darren darren 128 Jan 18 23:48 DCIM
drwx------ 1 darren darren 160 Apr 28 13:10 Downloads
drwx------ 1 darren darren 192 May  1 01:24 MediaAnalysis
drwx------ 1 darren darren 736 May  6 01:00 PhotoData
drwx------ 1 darren darren  96 Apr  6 03:01 PhotoStreamsData
drwx------ 1 darren darren  64 Jan 18 23:48 Photos
drwx------ 1 darren darren  64 Mar 13 10:49 Purchases
drwx------ 1 darren darren 352 Apr  8 14:58 Recordings
drwx------ 1 darren darren  96 Oct  5  2019 iTunes_Control

ls -Al /run/user/1000/gvfs/*port*
total 0
drwx------ 1 darren darren 0 Jan  1  1970 com.cuilingshi.fileextract
drwx------ 1 darren darren 0 Jan  1  1970 com.kingsoft.www.office.wpsoffice
drwx------ 1 darren darren 0 Jan  1  1970 com.microsoft.Office.Powerpoint
drwx------ 1 darren darren 0 Jan  1  1970 org.videolan.vlc-ios
```
