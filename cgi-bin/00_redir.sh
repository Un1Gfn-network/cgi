#!/bin/bash

# D="$(dirname $PWD)"
# TREE="tree -C -a -I .git* -H . --charset utf-8 -o "
# TREE="tree -C -a -I .git|.gitignore -H . --charset ascii -o " # Failed by non-ascii filenames

shopt -s expand_aliases
alias tree2="tree -a -I '.git|.gitignore|*_*_*_*.d|.nojekyll|.doctrees|_images|_sources|_static' --charset ascii -C -H . -o "

# https://stackoverflow.com/a/13864829
if [ -n "${GATEWAY_INTERFACE+x}" ]; then

  source 00_rc
  P

  tree2 ../index.html ..
  R="$?"
  if [ "$R" -eq 0 ]; then
    echo "Please go back to index.html and refresh it"
  else
    echo "Error! Please Check busybox httpd output."
  fi

else

  # https://stackoverflow.com/a/46383157
  tree2 index.html .

fi
