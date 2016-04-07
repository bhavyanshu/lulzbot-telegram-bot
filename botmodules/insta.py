#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError

from config import config

CLIENT_KEY = config['instagram']['client_key']
CLIENT_SECRET = config['instagram']['client_secret']
ACCESS_TOKEN = config['instagram']['access_token']

def insta(search_term):
	returnval=''

	api = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)

	try:
		username = search_term
		#print username
		if ' ' in username:
			username = username.replace(' ', '')

		if not api.user_search(username, 1):
			return "No user by that name was found."
		else:
			userid = api.user_search(username, 1)[0].id
			recent_media, next_ = api.user_recent_media(user_id=userid,count=5)
			for media in recent_media:
			   #text = media.caption.text
			   link = media.link
			   returnval += '~'+link+'\n'

			return returnval

	except InstagramAPIError as e:
	   if (e.status_code == 400):
	      return "Cannot retrieve data. User is set to private."
	   if (e.status_code == 404):
	   	  return "Content not found."

def insta_hon():
	returnval=''

	api = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)

	try:
		#if ' ' in search_term:
		#	search_term = search_term.replace(' ', '')
		search_term = 'selfie'
		if not api.tag_search(search_term, 1):
			print "No result found. :("
		else:
			recent_media, next_ = api.tag_recent_media(1, 20, search_term)
			for media in recent_media:
			   link = media.link
			   returnval += ' '+link+' \n'

			return returnval

	except InstagramAPIError as e:
	   if (e.status_code == 400):
	      return "Cannot retrieve data. User is set to private."
	   if (e.status_code == 404):
	   	  return "Content not found."

def insta_tag(search_tag):
	returnval=''

	api = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)

	try:
		#if ' ' in search_term:
		#	search_term = search_term.replace(' ', '')
		search_term = search_tag
		if not api.tag_search(search_term, 1):
			print "No result found. :("
		else:
			recent_media, next_ = api.tag_recent_media(1, 20, search_term)
			for media in recent_media:
			   link = media.link
			   returnval += ' '+link+' \n'

			return returnval

	except InstagramAPIError as e:
	   if (e.status_code == 400):
	      return "Cannot retrieve data. User is set to private."
	   if (e.status_code == 404):
	   	  return "Content not found."
