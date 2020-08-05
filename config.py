import tweepy
import logging
import os

logger = logging.getLogger()

# You can get these details from Twiter Developers account
def create_api() :
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
