tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

vert_cat = "vert \v space!"
form_cat = "form\ffeed"

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print vert_cat
print form_cat
print "bell\abell"
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
