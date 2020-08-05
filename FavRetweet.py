# this app likes and retweets tweets containing specified keywords
from config import create_api
import tweepy
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FavRetweetListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet with id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error liking tweet", exc_info=True)
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error liking and retweeting", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, is_async=True)
	
	

if __name__ == "__main__":
    # Specify any keywords
    main(["#ZimbabweanLivesMatter"])  
