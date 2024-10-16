# import tweepy
import time
import os
from dotenv import load_dotenv
from api import *

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


if __name__ == "__main__":

    print("Consumer Key:", CONSUMER_KEY)
    print("Consumer Secret:", CONSUMER_SECRET)
    print("Access Token:", ACCESS_TOKEN)
    print("Access Token Secret:", ACCESS_TOKEN_SECRET)

    service = XPostFinanceFeatures(consumer_key=CONSUMER_KEY,
                                   consumer_secret=CONSUMER_SECRET,
                                   access_token=ACCESS_TOKEN,
                                   access_token_secret=ACCESS_TOKEN_SECRET)
    



    '''
    # Authentification avec les clés d'API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #
    api = tweepy.API(auth)

    def unsubscribe_from_all():
        # 
        subscriptions = api.get_friend_ids(count=20)
        print("Il y'a actuellement : ", len(subscriptions), "following")
        #
        #
        for user in subscriptions:
            #api.destroy_friendship(user_id = user)
            print(f"Vous vous êtes désabonné de {user}")
            time.sleep(1)

    # 
    unsubscribe_from_all()
    '''