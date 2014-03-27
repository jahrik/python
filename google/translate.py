#!/usr/bin/env python2
# translate.py
# python translator

import urllib
import mechanize
from bs4 import BeautifulSoup as BS
import re


# def translate(home_language,target_language,text):
#     text = text.replace(" ","%20")
#     get_url = "http://translate.google.com/translate_a/t?client=t&sl="+home_language+"&tl="+target_language+"&hl="+home_language+"&sc=2&ie=UTF-8&oe=UTF-8&prev=btn&ssel=5&tsel=5&q="+text
#     browser = mechanize.Browser()
#     browser.set_handle_robots(False)
#     browser.addheaders = [('User-agent','Chrome')]
#     translate_text = browser.open(get_url).read().decode('UTF-8')
#     translate_text = translate_text.split("]]")
#     return translate_text[0].replace("[[[","").replace('"','').split(",")[0]

### Here I want to pull the languages off of the list and format it into a list of available languages printed out to the screen.
# def getGoogleLanguages():
#     br = mechanize.Browser()
#     br.set_handle_robots(False)
#     br.addheaders = [('User-agent','chrome')]
#     get_lang = "https://sites.google.com/site/opti365/translate_codes"
#     languages = br.open(get_lang).read()
#     soup = BS(languages)
#     langList = soup.findAll('table',attrs={'id':'sites-canvas-main-content'})
#     langText = str(langList[0])
#     return langText
#     languages  languages.split("")
#     print languages[]
def post_request(home_language,target_language,text):
    post_url = "http://translate.google.com/translate_a/t?"
    parameters = {
        'client':'t',
        'text':text,
        'sl':home_language,
        'tl':target_language,
        'hl':home_language,
        'ie':'UTF-8',
        'oe':'UTF-8',
        'prev':'btn',
        'rom':'1',
        'ssel':'0',
        'tsel':'0'
        }
    try:
        data = urllib.urlencode(parameters)
    except:
        print "error encoding parameters!!!"

    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent','Chrome')]
    response = browser.open(post_url,data).read().decode('UTF-8')
    translate_array = response.replace("[[[","").replace('["',"$$$").replace('"]',"$$$").split("$$$")
    trans_string = ""
    for block in translate_array:
        trans_string +=block.split('","')[0]
    
    return trans_string.split("]")[0].replace(",","")[1:]

