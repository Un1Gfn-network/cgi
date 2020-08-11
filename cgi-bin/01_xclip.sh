#!/bin/bash

source 00_rc

P

export XAUTHORITY=/home/darren/.Xauthority
export DISPLAY=:0.0

echo '[CLIPBOARD]'
echo
echo
xclip -o -selection clipboard
echo
echo

echo
echo
echo

echo '[PRIMARY]'
echo
echo
# https://stackoverflow.com/a/35040213
# env DISPLAY=:0.0 xclip -o -selection primary | recode ascii..html
# https://stackoverflow.com/a/13161719
# env DISPLAY=:0.0 xclip -o -selection primary | perl -MHTML::Entities -pe 'decode_entities($_);'
# https://stackoverflow.com/a/56491238
# http://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139540960
xclip -o -selection primary
echo
echo

# B
