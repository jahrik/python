#!/usr/bin/python2
# googletranslate.py
# python translator

import urllib
import mechanize


def translate(home_language,target_language,text):
    text = text.replace(" ","%20")
    get_url = "http://translate.google.com/translate_a/t?client=t&sl="+home_language+"&tl="+target_language+"&hl="+home_language+"&sc=2&ie=UTF-8&oe=UTF-8&prev=btn&ssel=5&tsel=5&q="+text
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent','Chrome')]
    translate_text = browser.open(get_url).read().decode('UTF-8')
    translate_text = translate_text.split("]]")
    return translate_text[0].replace("[[[","").replace('"','').split(",")[0]

print "Languages:"
print "en = English, es = Spanish"
home_language = raw_input("Home language: ")
target_language = raw_input("Target language: ")
text = raw_input("Translate: ")

print translate(home_language,target_language,text)
