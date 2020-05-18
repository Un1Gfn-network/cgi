#!/bin/bash

if [ -e index.html ]; then
  echo
  echo -n "  overwrite index.html? "; read -r
  echo
  R="$?"
  [ "$R" -eq 0 ] || exit "$R"
fi

function quit {
  echo
  rm -fv index.html
}

trap quit SIGINT

./cgi-bin/00_redir.sh

sudo busybox httpd -f -vv -p 80 -u darren:darren -h . -c ./httpd.conf
