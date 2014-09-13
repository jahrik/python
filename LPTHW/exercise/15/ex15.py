# import argv from module sys
from sys import argv

# set variable argv
script, filename = argv

# make a variable named txt = to the value of filename
txt = open(filename)

# print the raw data associated with filename
print "Here's your file %r:" % filename
# print what is read from variable text
print txt.read()

# print
print "Type the filename again:"
# set variable file_again to user input.
file_again = raw_input("> ")

# set another variable txt_again = the contents of file_again
txt_again = open(file_again)

# read the value of txt_again
print txt_again.read()
