#!/bin/bash

# D="$(dirname $PWD)"

# https://stackoverflow.com/a/13864829
if [ -n "${GATEWAY_INTERFACE+x}" ]; then

  source 00_rc
  A
  tree -H '.' --charset utf-8 -o ../index.html ..
  echo "$?"
  B

else

  # https://stackoverflow.com/a/46383157
  tree -H '.' --charset utf-8 -o index.html .

fi
