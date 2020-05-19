#!/usr/bin/python

# https://www.tutorialspoint.com/How-do-we-do-a-file-upload-using-Python-CGI-Programming

from cgi import FieldStorage
from os.path import basename
# from os.path import basename
from cgitb import enable
from sys import stderr

enable()
form = FieldStorage()
fileitem = form['filename']

if fileitem.filename:
   # Mitigate directory traversal attack
   fn = basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())
   # message = 'The file "' + fn + '" was uploaded successfully'
   message = "  '%s' -> '/tmp/%s'" % ( fn, fn )
else:
   message = 'No file was uploaded'

print("Content-Type: text/plain; charset=utf-8")
print()

print()
print(message)
print()

print(file=stderr)
print(message,file=stderr)
print(file=stderr)

# for line in stdin:
#     print(line)
# quit()
