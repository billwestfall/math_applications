# -*- coding: utf-8 -*-

import tweepy

consumer_key = ''
consumer_secret = ''

access_token_key = ''
access_token_secret = ''

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token_key, access_token_secret)

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
        print 'Ok, this is actually running'


l = StreamListener()
streamer = tweepy.Stream(auth=auth1, listener=l)
#setTerms = ['hello', 'goodbye', 'goodnight', 'good morning']
setTerms = ['twitter']
streamer.filter(track = setTerms)
