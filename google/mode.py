#!/env/bin/python2

import urllib
import mechanize
from bs4 import BeautifulSoup as BS
import re

# google translate
def translate(home_language,target_language,text):
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

# google search 
def search(link):
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

