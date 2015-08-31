import tweepy, sys, time, requests, os
import urllib
import json as m_json
 
def tweet():
    google_query = "janita chalam"
    google_query = urllib.urlencode({'q' : google_query})
    response = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + google_query).read()
    json = m_json.loads(response)
    results = json['responseData']['results']
    for result in results:
        title = result['title']
        url = result['url'] 
        print (url)
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_key = os.environ['ACCESS_KEY']
    access_secret = os.environ['ACCESS_SECRET']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    query = "node"
    response = api.search(q=query,rpp=1,count=1)
    # api.update_status(status=response[0].text)
    
if __name__ == "__main__":
    tweet()