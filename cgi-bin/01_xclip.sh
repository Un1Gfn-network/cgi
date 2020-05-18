#!/bin/bash

echo "Content-type: text/html"
echo

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Title</title>'
echo '</head>'
echo '<body>'

echo '<pre style="word-wrap: break-word; white-space: pre-wrap;">'
echo

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

echo '</pre>'
echo '</body>'
echo '</html>'

exit 0
