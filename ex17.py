from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

# open(to_file, 'w').write(open(from_file).read()) # one-liner version

in_file = open(from_file)
in_data = in_file.read()

print "the input file is %d bytes long" % len(in_data)

print "does the output file exist? %r" % exists(to_file)
print "ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "alright, all done."

out_file.close()
in_file.close()


