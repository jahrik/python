#!/usr/bin/env python2.7
''' doc string goes here '''
import mode

def do_stuff():
    ''' doc string goes here '''
    print("""
          Would you like to:
          1. Translate
          2. Search
          """)
    choice = raw_input(">> ")
#    while choice != "":
    choice = int(choice)
    if choice == 1:
        print("Languages")
        print("""
              en = English 
              es = Spanish 
              ja = Japanese
              """)
        home_language = raw_input("Home language: ")
        target_language = raw_input("Target language: ")
        text = raw_input("Translate: ")
        print(mode.translate(home_language, target_language, text))
    elif choice == 2:
        print("Search Google for:")
        link = raw_input(">> ")
        print(mode.search(link))
    else:
        print("choose a number from the list")
if __name__ == "__main__":
    do_stuff()
