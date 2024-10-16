from requests_oauthlib import OAuth1Session

class XPostFinanceFeatures:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        # Initialisation avec les clés OAuth
        self.oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )
        
    def __str__(self) -> str:
        # Décrire l'état de la classe
        return "Classe XPostFinanceFeatures pour interagir avec X (Twitter) via l'API"

    def post_tweet(self, text):
        """Publier un tweet"""
        url = "https://api.twitter.com/2/tweets"
        payload = {"text": text}
        
        response = self.oauth.post(url, json=payload)
        
        if response.status_code != 201:
            raise Exception(f"Erreur lors de la publication du tweet: {response.status_code} {response.text}")
        
        return response.json()

    def retweet(self, tweet_id):
        """Retweeter un tweet spécifique"""
        url = f"https://api.twitter.com/2/users/{self.get_user_id()}/retweets"
        payload = {"tweet_id": tweet_id}
        
        response = self.oauth.post(url, json=payload)
        
        if response.status_code != 200:
            raise Exception(f"Erreur lors du retweet: {response.status_code} {response.text}")
        
        return response.json()

    def reply_to_tweet(self, text, tweet_id):
        """Répondre à un tweet spécifique"""
        url = "https://api.twitter.com/2/tweets"
        payload = {
            "text": text,
            "reply": {"in_reply_to_tweet_id": tweet_id}
        }
        
        response = self.oauth.post(url, json=payload)
        
        if response.status_code != 201:
            raise Exception(f"Erreur lors de la réponse: {response.status_code} {response.text}")
        
        return response.json()

    def like_tweet(self, tweet_id):
        """Aimer un tweet spécifique"""
        url = f"https://api.twitter.com/2/users/{self.get_user_id()}/likes"
        payload = {"tweet_id": tweet_id}
        
        response = self.oauth.post(url, json=payload)
        
        if response.status_code != 200:
            raise Exception(f"Erreur lors de l'ajout du like: {response.status_code} {response.text}")
        
        return response.json()

    def delete_tweet(self, tweet_id):
        """Supprimer un tweet spécifique"""
        url = f"https://api.twitter.com/2/tweets/{tweet_id}"
        
        response = self.oauth.delete(url)
        
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la suppression du tweet: {response.status_code} {response.text}")
        
        return response.json()

    def get_user_id(self, username="self"):
        """Obtenir l'ID de l'utilisateur authentifié ou d'un autre utilisateur"""
        if username == "self":
            url = "https://api.twitter.com/2/users/me"
        else:
            url = f"https://api.twitter.com/2/users/by/username/{username}"
        
        response = self.oauth.get(url)
        
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la récupération de l'ID utilisateur: {response.status_code} {response.text}")
        
        user_info = response.json()
        return user_info['data']['id']
