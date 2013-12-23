#!/usr/bin/python

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)

    if options.get("returns") == "first":
        return first

result = bar(1, 2, 3, action = "sum", returns = "first")
print "Result: %d" % result
