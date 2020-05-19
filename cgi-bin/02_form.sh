#!/bin/bash

# https://codereview.stackexchange.com/questions/79549/bash-cgi-upload-file

source 00_rc
P
echo

if [ "$REQUEST_METHOD" = "POST" ]; then
    TMPOUT=/tmp/post
    cat >$TMPOUT

    cat "$TMPOUT"

    echo OK

    # # Get the line count
    # LINES=$(wc -l $TMPOUT | cut -d ' ' -f 1)

    # # Remove the first four lines
    # tail -$((LINES - 4)) $TMPOUT >$TMPOUT.1

    # # Remove the last line
    # head -$((LINES - 5)) $TMPOUT.1 >$TMPOUT

    # # Copy everything but the new last line to a temporary file
    # head -$((LINES - 6)) $TMPOUT >$TMPOUT.1

    # # Copy the new last line but remove trailing \r\n
    # tail -1 $TMPOUT | tr -d '\r\n' >> $TMPOUT.1
fi

# echo "Please use python"

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
