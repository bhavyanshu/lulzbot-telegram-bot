import os
import configparser

confile = os.path.join(os.path.dirname(__file__),'data','config.ini')
config = configparser.ConfigParser()
config.read(confile,encoding='utf-8')
