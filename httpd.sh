#!/bin/bash

sudo /bin/true
cd /home/darren/cgi

if [ -e index.html ]; then
  echo
  echo -n "  overwrite index.html? "
  read -r
fi

./cgi-bin/00_redir.sh

echo -e "\033]0;httpd\007"

# https://unix.stackexchange.com/questions/87468/is-there-an-easy-way-to-programmatically-extract-ip-address
ADDR="$(ip -4 address show wlp2s0 | grep -Po 'inet \K[\d.]+')"
URL="http://$ADDR/index.html"

echo
echo "  (1) Turn off proxy"
echo "  (2) Visit $URL"

echo
qrencode -tUTF8 "$URL"

echo
sudo busybox httpd -f -vv -p 80 -u darren:darren -h /home/darren/cgi -c /etc/httpd.conf

echo -e "\033]0;Alacritty\007"
