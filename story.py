#!/usr/bin/env python

print "You are invited to attend Pearl Hacks where you can meet other girls, make awesome projects and get a bunch of free food and swag. However, you had signed up for dance marathon a few months ago for that weekend..."

event = raw_input("Do you,  A) Attend Pearl Hacks, B) Attend Dance Marathon, C) Both, go big or go home!")

if event == "A":
	print "Congratulations, you end the weekend feeling inspired and excited about you major, classes, and friends who have similar interests to yours. Not to mention the stack of recruiter business cards in your back pocket."
	win = raw_input("Did you win the competition? y/n")
	if win == "y":
		print "You go girl! Make sure to write about your project on your resume and post it all on your GitHub account so recruiters and developers can check it out!"
	elif win == "n":
		print "Yes you did! Everyone at Pearl Hacks is a winner!"
	else:
		print "Invalid input."

if event == "B":
	print "By the end of the weekend you are in a pit of depression about your lack of confidence in JOMC 583 and start thinking about switching your major because you will never be good enough to get a job in the tech industry."
	senior = raw_input("Are you a senior? y/n")
	if senior == "y":
		print "Too bad, you missed out on an awesome event, but its okay, tech companies love women in computer science and if you took Professor King's classes they will all hire you."
	elif senior == "n":
		print "Don't despair, you can attend Pearl Hacks next year!"
	else:
		print "Invalid input."

if event == "C":
	awake = raw_input("Are you still awake? y/n")
	if awake == "y":
		print "Go to sleep!"
	elif awake == "n":
		print "Good, you earned it!"
	else:
		print "Invalid input."