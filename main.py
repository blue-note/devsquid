import tweepy, sys, time
import requests
 
def tweet():
    consumer_key = 'AThMTxBQ3TUxAWQ5iN1gZ0JKj'
    consumer_secret = 'pQdvykOviv7U197tGVkAyBneIOQPBk7l1cVcLv4T7sB3n5SCG8'
    access_key = '3386176895-g0yaSvp1fZKW9mJs67iyzSMYXmoa1jCFhAgonau'
    access_secret = 'IWGXdN7D9hk1agu5eepaFOF7PZ6MlMyJHlGK5tMYESfFs'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    query = "tech"
    response = api.search(q=query,rpp=1,count=1)
    api.update_status(status=response[0].text)
    while true: 
        a=2

if __name__ == "__main__":
    tweet()