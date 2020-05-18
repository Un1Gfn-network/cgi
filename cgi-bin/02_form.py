#!/bin/env python3

from os import environ
from sys import stderr
from urllib.parse import parse_qsl

print("Content-Type: text/plain; charset=utf-8")
print()

# print('Hello 歡迎')
print("REQUEST_URI  = '%s'" % environ['REQUEST_URI'])
print()

print("QUERY_STRING = '%s'" % environ['QUERY_STRING'])
print()

try:
    p=parse_qsl(
        environ['QUERY_STRING'],
        keep_blank_values=True,
        strict_parsing=True,
        encoding='utf-8',
        errors='strict',
        max_num_fields=None
    )
except ValueError:
    print ("ValueError")
except UnicodeError:
    print ("UnicodeError")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# https://stackoverflow.com/a/15860483
# https://docs.python.org/3/library/functions.html#print
def eprint(x):
    print(x,file=stderr)
eprint('\n')
eprint(p)
eprint('\n')
# for i in p:
#     print

# https://stackoverflow.com/q/5574702
# https://stackoverflow.com/a/37376668
# from os import write
# write(2,b"\n")
# write(2,p[0][0].encode())
# write(2,b"\n")
# write(2,p[0][1].encode())
# write(2,b"\n")
# write(2,b"\n")

print('OK')
print()

# for i in p:

