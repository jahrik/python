#!/usr/bin/env python2

from __future__ import print_function

def get_words():
    print("Select words to be used in your mad-lib")
    exclamation = raw_input("Exclamation >> ")
    adverb = raw_input("Adverb >> ")
    noun = raw_input("Noun >> ")
    adjective = raw_input("Adjective >> ")
    return exclamation, adverb, noun, adjective

def print_a_line(word, f):
    print(word, f.readline(), end="")

if __name__ == "__main__":
    f = open('test.txt', 'r')  # mad lib file

    exclamation, adverb, noun, adjective = get_words()

    for word in exclamation, adverb, noun, adjective:
        print_a_line(word, f)
