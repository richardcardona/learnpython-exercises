#!/usr/bin/env python

def repeater(old_function):
    def new_function(*args, **kwds): #See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) #we run the old function
        old_function(*args, **kwds) #we do it twice
    return new_function #we have to return the new_function, or it wouldn't reassign it to the value

@repeater
def Multiply(num1, num2):
    print num1*num2

Multiply(2, 3)

def type_check(correct_type):
    def check(arg):
       if not isinstance(arg, correct_type):
           print "Bad Type!"
    return check

@type_check(int)
def times2(num):
    return num*2

print times2(2)
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print first_letter('Hello World')
first_letter(['Not', 'A', 'String'])
