import tweepy
import csv
import pandas as pd
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

hashtags = ['h1b', 'visa']

for hashtag in hashtags:
    csvFile = open(hashtag+'.csv', 'a', encoding='utf-8') 
    csvWriter = csv.writer(csvFile)

    searched_tweets = [status for status in tweepy.Cursor(api.search, q='#'+hashtag, lang="en", since='2018-10-20', until='2018-10-21').items()]

#	---ONLY FOR NEW FILE --
#    csvWriter.writerow(['tweet_id','retweeted','tweet_text','tweet_created_at','tweet_retweet_count','tweet_favorite_count',
#        'user_id','user_name','user_location','user_friends_count',
#        'place_type','place_full_name','country'])

for tweet in searched_tweets:
    if tweet.place is not None:
        csvWriter.writerow([tweet.id, tweet.retweeted, tweet.text.encode("utf-8"), tweet.created_at, tweet.retweet_count, tweet.favorite_count,
        tweet.user.id, tweet.user.name, tweet.user.location, tweet.user.friends_count,
        tweet.place.place_type, tweet.place.full_name, tweet.place.country])
    else:
        csvWriter.writerow([tweet.id, tweet.retweeted, tweet.text.encode("utf-8"), tweet.created_at, tweet.retweet_count, tweet.favorite_count,
        tweet.user.id, tweet.user.name, tweet.user.location, tweet.user.friends_count])