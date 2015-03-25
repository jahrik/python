#!/usr/bin/env python2
# translate.py
# python translator

import urllib
import mechanize

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

