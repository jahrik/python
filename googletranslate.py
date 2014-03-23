#!/usr/bin/python2
# googletranslate.py
# python translator

import urllib
import mechanize


get_url = "http://translate.google.com/translate_a/t?client=t&sl=en&tl=es&hl=en&sc=2&ie=UTF-8&oe=UTF-8&prev=btn&ssel=5&tsel=5&q=flower"

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent','Chrome')]


translate_text = browser.open(get_url).read().decode('UTF-8')
translate_text = translate_text.split("]]")

print translate_text[0].replace("[[[","").replace('"','').split(",")[0]
