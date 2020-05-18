#!/bin/bash

# D="$(dirname $PWD)"
# TREE="tree -C -a -I .git* -H . --charset utf-8 -o "
TREE="tree -C -a -I .git|.gitignore -H . --charset utf-8 -o "

# https://stackoverflow.com/a/13864829
if [ -n "${GATEWAY_INTERFACE+x}" ]; then

  source 00_rc
  P
  $TREE ../index.html ..
  R="$?"
  if [ "$R" -eq 0 ]; then
    echo "Please go back to index.html and refresh it"
  else
    echo "Error! Please Check busybox httpd output."
  fi

else

  # https://stackoverflow.com/a/46383157
  $TREE index.html .

fi
