import tweepy
import time
import os

# 
consumer_key = os.getenv('C_KEY')
consumer_secret = os.getenv('C_SECRET')
access_token = os.getenv('A_TOKEN')
access_token_secret = os.getenv('A_TOKEN_SECRET')

# Authentification avec les clés d'API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#
api = tweepy.API(auth)

def unsubscribe_from_all():
    # 
    subscriptions = api.get_friend_ids(count=5000)
    print("Il y'a actuellement : ", len(subscriptions), "following")
    #
    #
    for user in subscriptions:
        api.destroy_friendship(user_id = user)
        print(f"Vous vous êtes désabonné de {user}")
        time.sleep(1)

# 
unsubscribe_from_all()
