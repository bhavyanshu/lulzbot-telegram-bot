#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Bhavyanshu Parasher"
__license__ = "GPL"
__version__ = "0.0.4"
__credits__ = ['fukouda']

"""bot.py - Main entry point. This handles all bot functions."""

# -- Standard Lib Imports -- #
import time
import json
import re
import math
import pickle
import os
import shlex
import random

# -- Third Party Imports -- #
import telegram
import emoji
from BeautifulSoup import BeautifulSoup
import urllib2
from urllib2 import Request
import urllib
import xmltodict
import traceback
import configparser
import giphypop
from giphypop import translate

# -- Local Imports -- #
from config import config
from uploadthread import UploadThread

from botmodules.google import google
from botmodules.wiki import wiki
from botmodules.weather import weather
from botmodules.youtube import youtube
from botmodules.twitter import twitter,twittertrends,twittersearch
from botmodules.bingsearch import bingsearch
from botmodules.github import gitfeed
from botmodules.translate import btranslate
from botmodules.calculate import calculate
from botmodules.imgur import imgur_hon

cat_API_key = config['thecatapi']['API_KEY']
grabtoken = config['telegram']['token']

bot = telegram.Bot(token=grabtoken.encode('utf8'))

help="""lulzbot is a bot created by @bhavyanshu - https://github.com/bhavyanshu/lulzbot-telegram-bot
\n
1 /help Displays list of Commands /help \n
2 /google keyword Google search by keyword /google terminator \n
3 /wiki keyword Lookup for wikipedia article /wiki Anaconda \n
4 /github username Get recent activity of user /github bhavyanshu \n
5 /translate from to "strng" Microsoft translate /translate en hi "I'm good" \n
6 /hon Get random Instagram post and start HotOrNot /hon or /hotornot \n
7 /tw username Get tweets of twitter user /tw nasa \n
8 /tt countryname , get trending topics by country, ex /tt india \n
9 /ts #hashtag , get latest tweets by hashtag. ex /ts #Privacy \n
10 /yt keyword string Search youtube for video /yt Iron Maiden \n
11 /cats Get a random cat pic /cats \n
12 /weather city,state Get weather update for city /weather paris \n
13 /giphy keyword Get gif from giphy /gif awesome \n
14 /img string, Get relevant image, /img give that man a cookie \n
15 /calc expression Calculate math expressions /calc 2+2"""

try:
    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
except IndexError:
    LAST_UPDATE_ID = None

def echo():
    global LAST_UPDATE_ID

    # Request updates from last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID):
        if LAST_UPDATE_ID < update.update_id:
            # chat_id is required to reply any message
            chat_id = update.message.chat_id
            message = update.message.text

            if (message):
                if '/start' in message or '/help' in message or '/list' in message or '/commands' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    bot.sendMessage(chat_id=chat_id,text=help.encode('utf8'),disable_web_page_preview=True)

                ##################----- PublicPlugins -----##################

                #Require API keys

                '''Youtube search'''
                if '/yt' in message or '/youtube' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    replacer = {'/youtube':'','/yt':''}
                    search_term = replace_all(message,replacer)
                    if len(search_term)<1:
                       bot.sendMessage(chat_id=chat_id,text='Youtube API calls are costly. Use it like /yt keywords; Ex, /yt Iron Maiden')
                    else:
                       bot.sendMessage(chat_id=chat_id,text=youtube(search_term).encode('utf8'))

                '''Twitter latest tweets of user'''
                if '/twitter' in message or '/tw' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    replacer = {'/twitter':'','/tw':''}
                    username = replace_all(message,replacer)
                    if len(username)<1:
                        bot.sendMessage(chat_id=chat_id,text='Use it like: /tw username; Ex, /tw pytacular')
                    else:
                        bot.sendMessage(chat_id=chat_id,text=twitter(username).encode('utf8'))

                '''Gets twitter trends by country /tt countryname, ex /tt India '''
                if '/tt' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    replacer = {'/tt ':''}
                    place = replace_all(message,replacer)
                    bot.sendMessage(chat_id=chat_id,text=twittertrends(place).encode('utf8'))

                '''Search twitter for top 4 related tweets. /ts #Privacy'''
                if '/ts' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    replacer = {'/ts ':''}
                    search_term = replace_all(message,replacer)
                    bot.sendMessage(chat_id=chat_id,text=twittersearch(search_term).encode('utf8'))

                '''Instagram latest posts of user'''
                if '/insta' in message or '/instagram' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    bot.sendMessage(chat_id=chat_id,text='Instagram has restricted API access. This will not work anymore. Sorry :(')

                '''Game "Hot or Not" '''
                if '/hon' in message or '/hotornot' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    custom_keyboard = [[ telegram.Emoji.THUMBS_UP_SIGN, telegram.Emoji.THUMBS_DOWN_SIGN ]]
                    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True,one_time_keyboard=True)
                    image = imgur_hon()
                    bot.sendMessage(chat_id=chat_id,text='Fetched from Imgur Subreddit r/models : '+image, reply_markup=reply_markup)

                '''Bing Image Search'''
                if '/image' in message or '/img' in message:
                    bot.sendChatAction(chat_id=chat_id,action=telegram.ChatAction.TYPING)
                    replacer = {'/image':'','/img':''}
                    search_term = replace_all(message,replacer)
                    pic_link = bingsearch(search_term,'Image')
                    bot.sendMessage(chat_id=chat_id,text=pic_link)

                '''Microsoft translator'''
                if '/translate' in message:
                    message = message.replace('/translate','').encode('utf8')
                    message_broken = shlex.split(message)
                    error = 'Not enough parameters. Use, /translate en hi "Hello world" or /translate help to know more'
                    if not len(message_broken)<1:
                        if message_broken[0] == 'help':
                            help_string = """ Example, /translate en hi "Hello world"
                                    ar-Arabic | bs-Latn-Bosnian (Latin) | bg-Bulgarian | ca-Catalan | zh-CHS-Chinese Simplified |
                                    zh-CHT-Chinese Traditional|hr-Croatian | cs-Czech | da-Danish | nl-Dutch |en-English | cy-Welsh |
                                    et-Estonian | fi-Finnish | fr-French | de-German | el-Greek | ht-Haitian Creole | he-Hebrew |
                                    hi-Hindi | mww-Hmong Daw | hu-Hungarian | id-Indonesian | it-Italian | ja-Japanese | tlh-Klingon |
                                    tlh - Qaak-Klingon (pIqaD) | ko-Korean | lv-Latvian | lt-Lithuanian | ms-Malay | mt-Maltese |
                                    no-Norwegian | fa-Persian | pl-Polish | pt-Portuguese | otq-Querétaro Otomi | ro-Romanian |
                                    ru-Russian | sr-Cyrl-Serbian (Cyrillic) | sr-Latn-Serbian (Latin) | sk-Slovak | sl-Slovenian |
                                    es-Spanish | sv-Swedish | th-Thai | tr-Turkish | uk-Ukrainian | ur-Urdu | vi-Vietnamese |
                                    """
                            bot.sendMessage(chat_id=chat_id,text=help_string)
                        else:
                            if len(message_broken)<3:
                                bot.sendMessage(chat_id=chat_id,text=error)
                            else:
                                lang_from = message_broken[0]
                                lang_to = message_broken[1]
                                lang_text = message_broken[2]
                                print lang_from+lang_to+lang_text
                                bot.sendMessage(chat_id=chat_id,text=btranslate(lang_text,lang_from,lang_to))
                    else:
                        bot.sendMessage(chat_id=chat_id,text=error)

                '''Random cat pic'''
                if '/cats' in message:
                    bot.sendMessage(chat_id=chat_id,text='Hold on, digging out a random cat pic!')
                    url = "http://thecatapi.com/api/images/get?api_key="+cat_API_key+"&format=xml"
                    xml_src = urllib2.urlopen(url)
                    data = xml_src.read()
                    xml_src.close()
                    data = xmltodict.parse(data)
                    piclink =  data['response']['data']['images']['image']['url']
                    source_url = data['response']['data']['images']['image']['source_url']
                    threadobjcats = UploadThread(bot,chat_id,piclink,caption=source_url)
                    threadobjcats.setName('catsthread')
                    threadobjcats.start()

                # Don't need an API key

                '''Google search'''
                if '/google' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    search_term = message.replace('/google','')
                    if len(search_term)<1:
                        bot.sendMessage(chat_id=chat_id,text='Use it like: /google what is a bot')
                    else:
                        bot.sendMessage(chat_id=chat_id,text=google(search_term))
                '''Wikipedia search'''
                if '/wiki' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    search_term = message.replace('/wiki ','')
                    if len(search_term)<1:
                        bot.sendMessage(chat_id=chat_id,text='Use it like: /wiki Anaconda')
                    else:
                        reply=wiki(search_term)
                        bot.sendMessage(chat_id=chat_id,text=reply)
                        if ("Cannot acces link!" in reply):
                            reply="No wikipedia article on that but got some google results for you \n"+google(message)
                            bot.sendMessage(chat_id=chat_id,text=reply)

                '''Weather by city,state'''
                if '/weather' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    reply=weather(message)
                    bot.sendMessage(chat_id=chat_id,text=reply)

                '''Github public feed of any user'''
                if '/github' in message or '/gh' in message:
                    bot.sendChatAction(chat_id=chat_id,action=telegram.ChatAction.TYPING)
                    replacer = {'/github':'','/gh':''}
                    username = replace_all(message,replacer)
                    if len(username)<1:
                        bot.sendMessage(chat_id=chat_id,text='Use it like: /github username Ex, /github bhavyanshu or /gh bhavyanshu')
                    else:
                        bot.sendMessage(chat_id=chat_id,text=gitfeed(username))

                '''Giphy to search for gif by keyword'''
                if '/giphy' in message or '/gif' in message:
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    replacer = {'/giphy':'','/gif':''}
                    search_term = replace_all(message,replacer)
                    if len(search_term)<1:
                        bot.sendMessage(chat_id=chat_id,text='Use it like: /giphy keyword ; Ex, /giphy cats or /gif cats')
                    else:
                        img = translate(search_term)
                        print img.fixed_height.downsampled.url
                        bot.sendMessage(chat_id=chat_id,text='Hang in there. Fetching gif..-Powered by GIPHY!')
                        bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
                        threadobjgiphy = UploadThread(bot,chat_id,img.fixed_height.downsampled.url.encode('utf-8'))
                        threadobjgiphy.setName('giphythread')
                        threadobjgiphy.start()

                '''Basic calculator'''
                if '/calc' in message:
                    head, sep, tail = message.partition('/')
                    input_nums = tail.replace('calc','')
                    input_nums = input_nums.replace('\'','')
                    finalexp = shlex.split(input_nums)
                    exp = finalexp[0]
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    error = 'You think I can compute apple+mongo? Don\'t add alphabet in between please. Use like, /calc 2+2-5(4+8)'
                    if not exp:
                        bot.sendMessage(chat_id=chat_id,text='Y u no type math expression? >.<')
                    elif re.search('[a-zA-Z]', exp):
                        bot.sendMessage(chat_id=chat_id,text=error)
                    else:
                        bot.sendMessage(chat_id=chat_id,text=calculate(exp))

                # Updates global offset to get the new updates
                LAST_UPDATE_ID = update.update_id


'''
Support Utility methods go below
'''

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def remove_duplicates(l):
    return list(set(l))

''' Main '''

if __name__ == '__main__':
    while True:
        echo()
        time.sleep(3)
