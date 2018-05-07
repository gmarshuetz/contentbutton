import sys
sys.path.append('C:\Python\Scripts\Twitter')

import tweepy

accessToken = '969229294831587328-psw3eaoaSJps8DNSQ0WODbCXMym3TP4'
accessTokenSecret = 'rxmKqSNwUeJeNCuezfPABbxEMJOSSXai8iJaJ1SQ3CmXu'
consumerKey = 'FhWxphnymVyLOjzH62CCcNaco'
consumerSecret = 'HyHs8HcjQZhT58ybYoFPNEYe4PN1xzN6Un7SOtq8AkRtWFg2qv'


auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
   

