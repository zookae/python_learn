print "you enter a dark room with two doors. do you take door #1 or #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "the bear eats your face"
    elif bear == "2":
        print "the bear eats your legs"
    else:
        print "well, doing %s is probably better. bear runs away" % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "your body survives powered by a mind of jello."
    else:
        print "the insanity rots your eyes into a pool of muck"

else:
    print "you stumble around and fall on a knife and die"
