#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import configparser
import os

from config import config

#confile = os.path.join(os.path.dirname(__file__),'../data','config.ini')
#print confile
#config = configparser.ConfigParser()
#config.read(confile,encoding='utf-8')

DEVELOPER_KEY = config['youtube']['API_SERVER_KEY']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube(search_term):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=search_term,
    part="id,snippet",
    maxResults=5
  ).execute()

  videos = []
  channels = []
  playlists = []
  allinfo = ''
  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],"https://www.youtube.com/watch?v="+search_result["id"]["videoId"]))

  return "\n".join(videos)


def error():
	return "Either service is unavailable or Youtube data API quota limit reached :("

if __name__ == "__main__":
	try:
		youtube(search_term)
	except HttpError, e:
		print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
		error()
