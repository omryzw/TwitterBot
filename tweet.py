# This will tweet ZimbabweLivesMatter every 30 seconds
from config import create_api
import tweepy
import random
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import string
import logging

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

api = create_api()


def publictweet():
    n = random.randint(1, 10)
    final = "#ZimbabweanLivesMatter " * n
    p = random.choice(string.ascii_letters)
    # Adding a random character at the end ensures that we do not get Duplicate Tweet Error
    # Adding the text zimbabweans Lives Matter at the end ensures that Twitter algorithm won't disregard the tweet as spam,
    # Twitter algorithm only counts hashtags if there is extra text on it
    final = final + " " + p + " Zimbabweans Lives Matter"
    api.update_status(final)

scheduler = BlockingScheduler()
scheduler.add_job(publictweet, 'interval', seconds=30)
scheduler.start()
