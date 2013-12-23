#!/usr/bin/env python

import sys

def fibonacci():
    previous, current = 1, 1
    while 1:
       if current > 100:
           break
       yield previous
       previous, current = current, current + previous

separator = ""
for sequence in fibonacci():
    sys.stdout.write("%s%s" % (separator, sequence))
    separator = ", "
print
