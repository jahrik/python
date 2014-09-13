# This project will take in some user input and return a list of there preferences.

# vars
geek = 0
OS = raw_input ("What is your OS preference?\nMac?\nWindows?\nLinux?\n\t")
GAME = raw_input ("What gaming system do you prefer?\nXbox?\nPlaystation?\nnone\n\t")
PET = raw_input ("Cat or dog?\n\t")
FACE = raw_input ("Do you have facial hair?\nBeard?\nMustache?\nClean?\n\t")

# print preferences
print "You truly are a unique individual :-)\nYou prefer %s.\nYou play %s\nYou like %ss\nAnd you have a %sed face." % (OS, GAME, PET, FACE)

### TOP SECRET!!! DO NOT TOUCH!!! ###
if FACE in ['Beard', 'beard', 'BEARD']:
    geek = geek + 1 

if OS in ['LINUX', 'Linux', 'linux']:
    geek = geek +1

if geek == 2:
    print ("GEEK!!!")
