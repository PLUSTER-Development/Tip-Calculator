meal = raw_input("What is your name?")
tax = raw_input("What is your quest?")
tip = raw_input("What is your favorite color?")

print "Ah, so your meal is %s, your tax is %s, " \
"and your favorite tip is %s." % (meal, tax, tip)

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
