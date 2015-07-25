#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import configparser

from config import config

def twitter(screenName):

	ckey = config['twitter']['client_key']
	csecret = config['twitter']['client_secret']
	atoken = config['twitter']['access_token']
	asecret = config['twitter']['access_secret']

	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	api = tweepy.API(auth)

	if ' ' in screenName:
		screenName = screenName.replace(' ', '')

	returnval=""
	item_count = 0

	try:
		for status in tweepy.Cursor(api.user_timeline,id=screenName).items(4):
			item_count += 1
			returnval += '\n'+str(item_count)+':'+status.text+'\n'

		return returnval	

	except tweepy.TweepError as e:
		error="Either the username does not exist or the service is unavailable."
		return error

def error():
	return "There was some error fetching results. Try later."

if __name__ == "__main__":
	try:
		twitter(username)
	except HttpError, e:
		print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
		error()