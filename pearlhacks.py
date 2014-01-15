#let's run some numbers for Pearl Hacks

college_girls = 150
high_school_girls = 50
sponsor_companies = 10
mentors = sponsor_companies * 2
volunteers = (college_girls + high_school_girls) / 10
total_participants = college_girls + high_school_girls + mentors + volunteers

print "We will have about %d people in attendance at Pearl Hacks." % total_participants

meals_served = 4
avg_cost_per_meal = 10
food_budget = meals_served * total_participants * avg_cost_per_meal

print "Our estimated food costs will be %d." % food_budget

print math.pow(5,18)
