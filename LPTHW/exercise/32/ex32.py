#!/usr/bin/env python2

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# loops
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "I got %r" % i

# start with an empty list
elements = []

for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

for i in elements:
    print "Element was: %d" % i

if __name__ == "__main__":


#####
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine

#####
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
