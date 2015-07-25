#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mstranslator import Translator

from config import config

client_id = config['microsoft']['CLIENT_ID']
client_secret = config['microsoft']['CLIENT_SECRET']

def btranslate(text_message,langfrom,langto):

  translator = Translator(client_id, client_secret)
  phrase_translated = translator.translate(text_message, lang_from=langfrom, lang_to=langto)
  #print phrase_translated
  return phrase_translated.encode('utf8')