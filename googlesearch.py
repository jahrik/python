#!/usr/bin/python2
#
# Perform a google search using python.
import urllib
import mechanize
from bs4 import BeautifulSoup as BS

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','chrome')]

term = "taco".replace(" ","+")

query = "https://www.google.com/search?q="+term+"&oq="+term

htmltext = br.open(query).read()
print(htmltext)

soup = BS(htmltext)

search = soup.findAll('div',attrs={'id':'search'})

searchtext = str(search[0])

soup1 = BS(searchtext)
list_items = soup1.findAll('li')

print list_items[0]
