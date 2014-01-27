#!/usr/bin/env python

apples = raw_input("How many apples do you have? ")
oranges = raw_input("How many oranges do you have? ")
bananas = raw_input("How many bananas do you have? ")

apples = int(apples)
oranges = int(oranges)
bananas = int(bananas)

if apples < oranges:
	print "There are more oranges than apples."
elif apples > oranges:
	print "There are more apples than oranges."
else:
	print "There are equal amounts of apples and oranges."

if bananas > apples:
	print "There are more bananas than apples."

if apples == 10:
	print "There are 10 apples."
elif apples == 100:
	print "There are 100 apples."

if apples <= 10:
	print "There are not enough apples."