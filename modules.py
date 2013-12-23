#!/usr/bin/python

import re

# Your code goes here
findfunctions = []
for function in dir(re):
    if ("find" in function):
        findfunctions.append(function)

# print findfunctions
print sorted(findfunctions)