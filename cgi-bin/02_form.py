#!/bin/env python3

from os import environ
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
print(p)
print()

