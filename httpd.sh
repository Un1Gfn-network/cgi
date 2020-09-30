#!/bin/bash

cd /home/darren/cgi

if [ -e index.html ]; then
  echo
  echo -n "  overwrite index.html? "
  read -r
fi

./cgi-bin/00_redir.sh

echo -e "\033]0;httpd\007"

sudo busybox httpd -f -vv -p 80 -u darren:darren -h /home/darren/cgi -c /etc/httpd.conf

echo -e "\033]0;Alacritty\007"
