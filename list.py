#!/usr/bin/env python

team = ["Braves", "Yankees", "Nationals"]
wins = [94, 95, 99]
losses = [64, 67, 68]

tempList = []

for number in wins:
	print "Wins=%d" % number

print "The Teams:"
for i in team:
	print i

print "****Winners****"
for i in range(0,2):
	print team[i]