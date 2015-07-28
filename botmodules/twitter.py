#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import tweepy
import configparser

from config import config


ckey = config['twitter']['client_key']
csecret = config['twitter']['client_secret']
atoken = config['twitter']['access_token']
asecret = config['twitter']['access_secret']

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

def twitter(screenName):

	if ' ' in screenName:
		screenName = screenName.replace(' ', '')

	returnval=""
	item_count = 0

	try:
		for status in tweepy.Cursor(api.user_timeline,id=screenName).items(4):
			item_count += 1
			returnval += '\n'+str(item_count)+':'+status.text+' '+'https://twitter.com/'+screenName+'/status/'+status.id_str+'\n'

		return returnval	

	except tweepy.TweepError as e:
		error="Either the username does not exist or the service is unavailable."
		return error

def twittersearch(keyword):

	returnval=""
	item_count = 0

	try:
		for status in tweepy.Cursor(api.search, q=keyword, show_user=True).items(4):
			u = api.get_user(status.user.id)
			item_count += 1
			returnval += '\n'+str(item_count)+':'+status.text+' '+'https://twitter.com/'+u.screen_name+'/status/'+status.id_str+'\n'
		return returnval

	except tweepy.TweepError as e:
		error="The service is unavailable."
		return error

def twittertrends(place):
	
	trends = ""
	item_count = 0
	woeid = getWoeid(place)
	if not woeid:
		return 'Invalid country name provided. Try /tt country'
	else:
		try:
			trends1 = api.trends_place(id=woeid)
			for trend in trends1[0]['trends']:
				trends += trend['name']+'\n'
			return 'Trending on twitter:\n'+trends
		except tweepy.TweepError as e:
			error='Invalid country name provided or the service is not available right now.'
			return error

def getWoeid(placename):
	CONSUMER_KEY = config['yahoo']['CONSUMER_KEY']
	location = placename

	if not location:
	    print 'no location provided'

	url = 'http://where.yahooapis.com/v1/places.q(\'%s\')?appid=%s&format=json' % (
	    location, CONSUMER_KEY
	)
	r = requests.get(url)
	json = r.json()
	places = json['places']
	#print places
	if not places['count']:
	    print 'found nothing'
	place = places['place'][0]

	return place['woeid']