# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
import re

def wiki(term): # /wiki <search term>
    
    main_page = 'http://en.wikipedia.org/wiki/Main_Page'
    
    articles = ['a', 'an', 'of', 'the', 'is']
    wlink = title_except(term,articles) 
    if 1 == len(wlink):
        response = main_page
    else:
        search_term = wlink[1].lstrip().replace(' ', '_')
        search_term = wlink.replace(' ', '_')
        #print search_term

        if len(search_term) < 1:
            response = main_page
        else:
            response = 'http://en.wikipedia.org/wiki/' + search_term

    response = response + '      ' + get_para(response)

    return response.encode('utf-8')

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)

def get_para(wlink):
    'Gets the first paragraph from a wiki link'

    msg = ''
    try:
        page_request = urllib2.Request(wlink)
        page_request.add_header('User-agent', 'Mozilla/5.0')
        page = urllib2.urlopen(page_request)
    except IOError:
        msg = 'Cannot acces link!'
    else:

        soup = BeautifulSoup(page)
        msg = ''.join(soup.find('div', { 'id' : 'bodyContent'}).p.findAll(text=True))

        while 460 < len(msg):
            pos = msg.rfind('.')
            msg = msg[:pos]

    return msg

if __name__ == "__main__":
    wiki(search_term)