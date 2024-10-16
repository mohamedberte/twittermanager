from requests_oauthlib import OAuth1Session
import os
import json

# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'

consumer_key = "E0Djg0zKSGUWIjLF5bBotWn7n"
consumer_secret = "eXLhp4w7R8p9bTWMJN4x9ddfOMNGA2S58ZnmXKBKbR9O2RQKSG"

# Be sure to add replace the text of the with the text you wish to Tweet. You can also add parameters to post polls, quote Tweets, Tweet with reply settings, and Tweet to Super Followers in addition to other features.
access_token = "932728661182214144-yE0ketG6xn2iLlM9vyq4zyV4uwUQlms"
access_token_secret = "JQ1EURUcEKJt3A0WUCMeCBG4AhflwnUDoqfKGMDGpmOXU"

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

payload = {"text": "Hello world!"}

# Making the request
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))