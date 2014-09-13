# set variable x. It's a string with a %d formatter set to 10
x = "There are %d types of people." % 10
# set variable binary to a string "binary"
binary = "binary"
# set variable do_not to a string "don't"
do_not = "don't"
# set variable y to a string. Place 2 strings inside it.
y = "Those who know %s and those who %s." % (binary, do_not)

# print some stuff
print x
print y

# print some more stuff.
print "I said: %r." % x
print "I also said: '%s'." % y

# set variable hilarious to a boolean value
hilarious = False
# set variable joke_evaluation to a string.
joke_evaluation = "Isn't that joke so funny?! %r"

# print some more stuff.
print joke_evaluation % hilarious

# set variable w to a string.
w = "This is the left side of..."
# set variable e to a string.
e = "a string with a right side."

# print stuff
print w + e
