#!/usr/bin/python

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

# test code
car1 = Vehicle()
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.0
car1.name = "Fer"

car2 = Vehicle()
car2.color = "blue"
car2.kind = "van"
car2.name = "Jump"
car2.value = 10000.0

print car1.description()
print car2.description()