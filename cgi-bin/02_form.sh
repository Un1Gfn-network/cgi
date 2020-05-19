#!/bin/bash

# https://codereview.stackexchange.com/questions/79549/bash-cgi-upload-file

source 00_rc
P

echo "Please use python"
exit 0

# echo "\$REQUEST_URI = '$REQUEST_URI'"
# echo
# echo "\$QUERY_STRING = '$QUERY_STRING'"
# echo

# https://stackoverflow.com/a/3919908
# saveIFS=$IFS
# IFS='=&'
# parm=($QUERY_STRING)
# IFS=$saveIFS
# for i in $(seq 0 $((${#parm[@]}-1))); do
#   echo "parm[$i] = '${parm[$i]}'"
# done

# echo "\$1 = '$1'"
# echo "\$2 = '$2'"
# echo "\$3 = '$3'"

# read QUERY_STRING
# eval $(echo "$QUERY_STRING"|awk -F'&' '{for(i=1;i<=NF;i++){print $i}}')
# tmp=`httpd -d $Text_Field`
# echo "Text_Field=$tmp"
# tmp=`httpd -d $Radio_Button`
# echo "Radio_Button=$tmp"
# tmp=`httpd -d $Text_Area`
# echo "Text_Area=$tmp"
