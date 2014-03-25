#!/usr/bin/env python2
# googletranslate.py
# python translator

import urllib
import mechanize
from bs4 import BeautifulSoup as BS
import re


def translate(home_language,target_language,text):
    text = text.replace(" ","%20")
    get_url = "http://translate.google.com/translate_a/t?client=t&sl="+home_language+"&tl="+target_language+"&hl="+home_language+"&sc=2&ie=UTF-8&oe=UTF-8&prev=btn&ssel=5&tsel=5&q="+text
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent','Chrome')]
    translate_text = browser.open(get_url).read().decode('UTF-8')
    translate_text = translate_text.split("]]")
    return translate_text[0].replace("[[[","").replace('"','').split(",")[0]

### Here I want to pull the languages off of the list and format it into a list of available languages printed out to the screen.
def getGoogleLanguages():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome')]
    get_lang = "https://sites.google.com/site/opti365/translate_codes"
    languages = br.open(get_lang).read()
    soup = BS(languages)
    langList = soup.findAll('table',attrs={'id':'sites-canvas-main-content'})
    langText = str(langList[0])
    return langText
    # languages  languages.split("")
    # print languages[]

if __name__ == "__main__":
    print "Languages"
    print "en = English, es = Spanish, ja = Japanese"
#    print getGoogleLanguages()
    home_language = raw_input("Home language: ")
    target_language = raw_input("Target language: ")
    text = raw_input("Translate: ")
    print translate(home_language,target_language,text)
