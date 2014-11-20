#!/usr/bin/env python2

class Parent(object):

    def override(self):
        print "Parent override()"

    def implicit(self):
        print "Parent implicit()"

    def altered(self):
        print "Parent altered()"



class Child(Parent):

    def override(self):
        print "Child override()"

    def altered(self):
        print "Child, before parent altered()"
        super(Child, self).altered()
        print "Child, After parent altered()"

def main():
    dad = Parent()
    son = Child()

    dad.implicit()
    son.implicit()

    dad.override()
    son.override()

    dad.altered()
    son.altered()

if __name__ == "__main__":
    main()
