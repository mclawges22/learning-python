#!/usr/bin/env python
from __future__ import division

age = raw_input("How old are you? ")
height = raw_input("How tall are you in inches? ")
weight = raw_input("How much do you weigh? ")

print "So you are %r years old, %r inches tall and weigh %r pounds." % (age, height, weight)

#convert Strings to ints
age = int(age)
height = int(height)
weight = int(weight)

#BMI FORMULA = (weight in pounds / (height in inches ^ 2)) x 703
bmi = (weight/(height**2)) * 703

print "Your BMI is %d" % bmi