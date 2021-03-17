import tweepy
import glob
import os
import time
import threading
import random
import secrets
from credentials import *
from quoteArray import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# user = api.me()

WAIT_SECONDS = 1200


def tweetImage():
    try:
        quote = secrets.choice(quotes)
        tweet = quote + " " + \
            '#javascript #python #softwareengineer #dataengineer #nodejs #reactjs #100DaysOfCode'

        data = os.listdir('/home/pi/Code/twitterPicsQuotes-python/Images')

        image = data[random.randint(0, len(data))-1]

        upload_result = api.media_upload(
            '/home/pi/Code/twitterPicsQuotes-python/Images/' + image)
        api.update_status(status=tweet, media_ids=[
            upload_result.media_id_string], tweet_mode='extended')
        print(time.ctime())
        threading.Timer(WAIT_SECONDS, tweetImage).start()
        pass
    except Exception as e:
        pass


tweetImage()
