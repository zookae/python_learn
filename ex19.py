def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheeses" % cheese_count
    print "you have %d crackers" % boxes_of_crackers
    print "that's enough for a party!\n"

print "we can just give the function numbers directly"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

input_cheese = int(raw_input("how many cheeses?: "))
cheese_and_crackers(input_cheese, 0)
