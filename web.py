#/usr/bin/env python2

from google import search, translate

if __name__ == "__main__":
#   print translate.getGoogleLanguages()
    print "Languages"
    print "en = English, es = Spanish, ja = Japanese"
    home_language = raw_input("Home language: ")
    target_language = raw_input("Target language: ")
    text = raw_input("Translate: ")
    print translate.post_request(home_language,target_language,text)
