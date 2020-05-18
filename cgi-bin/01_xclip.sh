#!/bin/bash

source 00_rc

A

echo '[PRIMARY]'
echo
# https://stackoverflow.com/a/35040213
env DISPLAY=:0.0 xclip -o -selection primary | recode ascii..html
echo
echo

echo '[CLIPBOARD]'
echo
env DISPLAY=:0.0 xclip -o -selection clipboard | recode ascii..html
echo
echo

B
