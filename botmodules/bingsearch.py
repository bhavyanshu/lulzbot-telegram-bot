#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import random

from config import config

api_key = config['bingsearch']['API_KEY']

def bingsearch(query, search_type):
    query = urllib.quote(query)
    user_agent = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330'
    credentials = (':%s' % api_key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=5&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request) 
    response_data = response.read()
    json_result = json.loads(response_data)
    result = json_result['d']['results'][0]['MediaUrl']
    return result
