#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser 
import urllib2
from urllib2 import Request

def gitfeed(username):
	returnval = ''
	username = username.replace(' ', '')

	url = "https://github.com/"+username+".atom"

	try:
		#check if url returns 404
		a=urllib2.urlopen(url)
		feed = feedparser.parse(url)["entries"]
		for i in xrange(1,5):
			returnval +='['+str(i)+' '+feed[i].title+' - '+feed[i].link+' ]\n'

		return returnval

	except urllib2.HTTPError as e:
		if e.code == 404:
			error = 'Either user does not exist or you gave invalid username'
			return error
        	
