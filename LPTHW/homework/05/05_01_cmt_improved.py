#!/usr/bin/env python2

class contest(object):
    
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class 








def how_much():
    much = ammount * 10
    first = winnings
    second = winnings / 2
    third = winnings / 4
    return much, first, second, third

def get_words():
    print """
        Contest management tool:
        Lets get started,
        I'm going to need some information first.
        """
    ammount = int(raw_input("How many people competed in the contest? "))
    name01 = raw_input("Who won first place? ")
    name02 = raw_input("Who won second place? ")
    name03 = raw_input("Who won third place? ")
    winnings = int(raw_input("How much does first place win? "))
    return ammount, name01, name02, name03, winnings

if __name__ == "__main__":
    ammount, name01, name02, name03, winnings = get_words()
    much, first, second, third = how_much()
    print """
        %s wins: $%d
        %s wins: $%d
        %s wins: $%d
        """ % (name01, first, name02, second, name03, third) 
    print """
        The contest raised $%d 
        after paying the winners.
        """ % (much - first - second - third) 
