from pymongo import MongoClient
from configparser import ConfigParser
import json
from mongoengine import *
from schema.TestSchema import Testdata



config = ConfigParser()
config.read('config/config.ini')
address = config["Mongo"]['address']
port = config["Mongo"]['port']
database = config["Mongo"]['database']

register_connection(host=address, port=int(port), db=database, alias='default')

# test = Testdata(tags="test", num=123)
# test.save()

##client = MongoClient(str(address), int(port))
##db = client[database]
##col = db['newcollection']
##
##mydic = {"test":"test"}
##
##x = col.insert_one(mydic)
