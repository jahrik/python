#!/usr/bin/env python2

class Other(object):

    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def altered(self):
        print "Other altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "Child override()"

    def altered(self):
        print "Child, before other altered()"
        self.other.altered()
        print "Child, after other altered()"

def main():
    son = Child()
    son.implicit()
    son.override()
    son.altered()

if __name__ == "__main__":
    main()
