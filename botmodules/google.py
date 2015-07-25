# -*- coding: utf-8 -*-
import urllib
import json as m_json

def google(terms): # google <search term>
    query=terms
    query = urllib.urlencode ( { 'q' : query } )
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    returnval=""
    for result in results:
        title = result['title']
        url = result['url']
        title=title.translate({ord(k):None for k in u'<b>'})
        title=title.translate({ord(k):None for k in u'</b>'})
        returnval += title + ' ; ' + url + '\n'
        
    return returnval.encode('utf-8')
