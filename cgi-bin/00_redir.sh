#!/bin/bash

# D="$(dirname $PWD)"
# D=/home/darren/http/httpd.sh

# https://stackoverflow.com/a/13864829
if [ -n "${GATEWAY_INTERFACE+x}" ]; then
  source 00_rc
  A
  # echo sdf >garbage
  # cat garbage
  tree -H '.' --charset utf-8 -o ../index.html ..
  echo "$?"
  B
else
  tree -H '.' --charset utf-8 -o index.html .
fi
