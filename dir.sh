#!/bin/bash

function quit {
  echo
  rm -fv index.html
}

if [ -e index.html ]; then
  echo
  echo -n "  overwrite index.html? "; read -r
  echo
  R="$?"
  [ "$R" -eq 0 ] || return "$R"
fi

tree -H '.' --noreport --charset utf-8 >index.html
trap quit SIGINT

sudo busybox httpd -f -vv -p 80 -h . -c ./httpd.conf
