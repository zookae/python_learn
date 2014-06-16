i = 0
numbers = []

while i < 6:
    print "at the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "numbers now: ", numbers
    print "at the bottom i is %d" % i

print "the numbers: "
for num in numbers:
    print num


def loop_fn(max_i, incr):
    i = 0
    numbers = []

    while i < max_i:
        print "at the top i is %d" % i
        numbers.append(i)
    
        i = i + incr
        print "numbers now: ", numbers
        print "at the bottom i is %d" % i
    
    print "the numbers: "
    for num in numbers:
        print num

def loop_fn_for(max_i, incr):
    numbers = []
    for i in range(0, max_i, incr):
        print "at the top i is %d" % i
        numbers.append(i)
    
#        i = i + incr
        print "numbers now: ", numbers
        print "at the bottom i is %d" % i
    
    print "the numbers: "
    for num in numbers:
        print num
