#!/usr/bin/env python2
# reddit.py
# login to reddit and add a friend to your friends list.

import urllib
import mechanize
import sys

# Login to reddit.  Username and password should be set in cfg.txt
def login(br, user, password):
    url = "https://www.reddit.com"
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36')]
    br.open(url)
    br.select_form(nr=1)
    br.form["user"] = user
    br.form["passwd"] = password
    page = br.submit()
    print page.code
    print page.geturl()
    return br

def add_friend(name):
    post_url = "https://ssl.reddit.com/api/friend"
    parameters = {
        'action':'add',
        'container':'t2_fw9kg',
        'type':'friend',
        'name':name,
        'id':'#friend',
        'uh':'q99jyoxk1t92ab40dac423543c27467b9cb913aef2f6939cbd',
        'renderstyle':'html'
        }
    try:
        data = urllib.urlencode(parameters)
    except:
        print "error encoding parameters!!!"
    add = br.open(post_url,data)    

if __name__ == "__main__":
    # set user and password
    f = open('cfg.txt', 'r')
    credentials = f.read().splitlines()

    # username on first line of file
    user = credentials[0]

    # password on second line of file
    password = credentials[1]
    br = login(mechanize.Browser(), user, password)
    # ask user to input name to be added to list
    name = raw_input("Friend: ")
    add_friend(name)
