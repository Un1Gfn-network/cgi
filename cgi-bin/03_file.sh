#!/bin/bash

source 00_rc
P

[ "$REQUEST_METHOD" = "POST" ] || {
  echo 'Wrong $REQUEST_METHOD'
  exit 1
}

TMPOUT=/tmp/post
cat >$TMPOUT

ls -lh "$TMPOUT"

# echo OK

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
