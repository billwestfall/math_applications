
import tweepy
from tweepy.streaming import StreamListener
import json
import requests
from pymongo import MongoClient

def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):
    mongo_uri = 'mongodb://localhost:27017'
conn = MongoClient(mongo_uri)

class MyStreamListener(StreamListener):
    def __init__(self, api, **kw):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.col = get_mongo_database('tweets', **kw)['tweets']

        def on_data(self, tweet):
            self.col.insert(json.loads(tweet))

        def on_error(self, status):
            return True

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
stream = tweepy.Stream(auth, MyStreamListener(api))

stream.filter(track=['Hype Machine'])
