# import tweepy
import json
import os
from dotenv import load_dotenv
from api import *

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

def getDataFromTxtFile(path="knowledge/", filename=None):
    if path and filename:
        with open(path + filename) as file:
            return [ data.strip() for data in file.readlines()]
    else : raise ValueError("Vérifier le chemin et le nom du fichier à lire") 

def getHistoricalData(path="knowledge/", filename=None):
    if path and filename and os.path.exists(path + filename):
        with open(path + filename) as file:
            return json.load(file)
    else : raise ValueError("Vérifier le chemin et le nom du fichier à lire") 

if __name__ == "__main__":

    service = XPostFinanceFeatures(consumer_key=CONSUMER_KEY,
                                   consumer_secret=CONSUMER_SECRET,
                                   access_token=ACCESS_TOKEN,
                                   access_token_secret=ACCESS_TOKEN_SECRET)
    
    service.post_tweet("Bonjour Le binks")

'''    usernames = getDataFromTxtFile(filename="user.txt")
    print(usernames)'''

'''    res = service.get_user_id(username="InvestInAssets")
    print(res)
    followers = service.get_followers(res)

    print(followers)
'''

'''    history_data = getHistoricalData(filename="")

    # Charger l'historique existant s'il y en a un
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history_data = json.load(f)

    for username in usernames:
        try:
            latest_tweet_id, user_id = get_latest_tweet_id(username)
            if latest_tweet_id is None:
                print(f"{username} n'a pas de tweets récents.")
                continue

            # Vérifier si le tweet a déjà été retweeté
            if str(user_id) in history_data and history_data[str(user_id)] == latest_tweet_id:
                print(f"Le dernier tweet de {username} a déjà été retweeté.")
                continue

            # Retweeter le dernier tweet
            retweet(latest_tweet_id)
            print(f"Retweet réussi pour {username} - Tweet ID: {latest_tweet_id}")

        # Enregistrer dans l'historique
            history_data[str(user_id)] = latest_tweet_id

        except Exception as e:
            print(f"Erreur pour {username}: {e}")

    # Enregistrer l'historique mis à jour
    with open(history_file, 'w') as f:
        json.dump(history_data, f, indent=4)

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