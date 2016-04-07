#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import random
from imgurpython import ImgurClient
#import configparser

from config import config


ckey = config.get('imgur','client_id')
csecret = config.get('imgur','client_secret')

def imgur_hon():
    client = ImgurClient(ckey, csecret)
    window_list = ['month','year','all']
    item_select = random.randint(0,10)
    items = client.subreddit_gallery('models', sort='top', window=random.choice(window_list), page=random.randint(0,5))
    image = items[item_select].link
    return image
