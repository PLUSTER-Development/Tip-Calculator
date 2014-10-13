meal = raw_input("What is your meal cost?")
tax = raw_input("What is your tax percent as a decimal?")
tip = raw_input("What is your tip as a percent?")

print "Ah, so your meal is %s, your tax is %s, " \
"and your favorite tip is %s." % (meal, tax, tip)

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
