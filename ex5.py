my_name = 'Alex Zook'
my_age = 27
my_height = 69 # inches
my_weight = 120 # lbs
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Blonde'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

escape_test = "test's"
print "test escaped: %s" % escape_test
print "test escaped: %r" % escape_test
