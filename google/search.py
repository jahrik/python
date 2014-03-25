#!/usr/bin/env python2
#
# Perform a google search using python.
import urllib
import mechanize
from bs4 import BeautifulSoup as BS
import re

#function that takes the input word.
def getGoogleLinks(link):
    # create a browser and change user agent so it thinks we're a person, not a machine.
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome')]

    # replace any spaces in the search term with +.
    term = link.replace(" ","+")
    # append the search term to the url.
    query = "https://www.google.com/search?q="+term
    htmltext = br.open(query).read()
    soup = BS(htmltext)
    search = soup.findAll('div',attrs={'id':'search'})
    searchtext = str(search[0])
    soup1 = BS(searchtext)
    list_items = soup1.findAll('li')
    regex = "q(?!.*q).*?&amp"
    pattern = re.compile(regex)

    results_array = []

    for li in list_items:
        soup2 = BS(str(li))
        links = soup2.findAll('a')
        source_link = links[0]
        source_url = re.findall(pattern,str(source_link))
        if len(source_url)>0:
            results_array.append(str(source_url[0].replace("q=","").replace("&amp","")))
    return results_array

