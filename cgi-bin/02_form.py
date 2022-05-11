#!/bin/env python3

from os import environ
from sys import stdin,stderr
from urllib.parse import parse_qsl
import sys


print("Content-Type: text/plain; charset=utf-8")
print()


print('Hello 歡迎')
print()

print("REQUEST_URI  = '%s'" % environ['REQUEST_URI'])
print()

print("QUERY_STRING = '%s'" % environ['QUERY_STRING'])
print()

# https://docs.python.org/3/tutorial/errors.html
try:
    p=parse_qsl(
        # https://stackoverflow.com/questions/4906977
        environ['QUERY_STRING'],
        keep_blank_values=True,
        strict_parsing=True,
        encoding='utf-8',
        errors='strict',
        max_num_fields=None
    )
except ValueError:
    print("ValueError")
except UnicodeError:
    print("UnicodeError")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# https://stackoverflow.com/a/15860483
# https://docs.python.org/3/library/functions.html#print
# https://docs.python.org/3/glossary.html#keyword-only-parameter
def eprint(*x):
    print(*x,file=stderr)
eprint()
for i in p:
    eprint("[%s]"%i[0])
    eprint()
    eprint(i[1])
    eprint()
    eprint()

# https://stackoverflow.com/q/5574702
# https://stackoverflow.com/a/37376668
# from os import write
# write(2,b"\n")
# write(2,p[0][0].encode())
# write(2,b"\n")
# write(2,p[0][1].encode())
# write(2,b"\n")
# write(2,b"\n")

print('OK. Please check busybox httpd console.')
print()

# for i in p:

