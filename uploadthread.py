#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
import time
import os.path

import telegram

class UploadThread(Thread):
    def __init__(self, bot, chat_id, link, caption=None):
        '''
        bot = Telegram bot object
        chat_id = chat id to which send the file to
        link = URL to fetch the file from
        caption = (Optional) Used with sendPhoto.
        '''
 
        Thread.__init__(self)
        self.bot = bot
        self.chat_id = chat_id
        self.link = link
        self.caption = caption
 
    def run(self):
        extension = os.path.splitext(self.link)[1][1:]
        print extension
        IMAGE_TYPES = ('jpg','jpeg','bmp','png')
        if extension.lower() in IMAGE_TYPES:
            #Use sendPhoto to upload jpeg/png
            self.bot.sendPhoto(chat_id=self.chat_id, photo=self.link.encode('utf-8'),caption=self.caption)
        else:
            #Use sendDocument to upload other files
            self.bot.sendDocument(chat_id=self.chat_id, document=self.link.encode('utf-8'))