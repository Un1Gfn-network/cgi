#!/bin/bash

function quit {
  sudo killall stunnel
  sudo killall busybox
  exit 1
}

trap quit SIGINT

cd /home/darren/cgi

if [ -e index.html ]; then
  echo
  echo -n "  overwrite index.html? "
  read -r
fi

./cgi-bin/00_redir.sh

echo -e "\033]0;httpd\007"

sudo /bin/true

parallel --line-buffer ::: 'sudo busybox httpd -f -vv -p 127.0.0.1:80 -u darren:darren -h /home/darren/cgi -c /etc/httpd.conf' 'sudo stunnel /etc/stunnel/stunnel.conf'

echo -e "\033]0;Alacritty\007"
