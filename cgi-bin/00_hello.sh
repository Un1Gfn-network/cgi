#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Hello World</title>'
echo '</head>'
echo '<body>'

echo '<br>'

echo 'Hello World<br>'
echo '<br>'

uname -a; echo '<br>'
echo '<br>'

date; echo '<br>'
echo '<br>'

echo '</body>'
echo '</html>'

exit 0
