import tweepy
import time
from decouple import config

# Configurez les clés d'API
consumer_key = config('C_KEY')
consumer_secret = config('C_SECRET')
access_token = config('A_TOKEN')
access_token_secret = config('A_TOKEN_SECRET')

# Authentification avec les clés d'API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Créez une instance de l'API Twitter
api = tweepy.API(auth)

def unsubscribe_from_all():
    # Récupérer la liste des abonnements
    subscriptions = api.get_friend_ids(count=5000)
    print("Il y'a actuellement : ", len(subscriptions), "following")
    # Se désabonner de chaque compte
    for user in subscriptions:
        api.destroy_friendship(user_id = user)
        print(f"Vous vous êtes désabonné de {user}")
        time.sleep(1)

# Exécuter la fonction pour se désabonner de tous les comptes
unsubscribe_from_all()
