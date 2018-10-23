
import tweepy
import csv
import pandas as pd

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvTweet = open('tweet.csv', 'a')
csvTweetWriter = csv.writer(csvTweet)
csvUser = open('user.csv', 'a')
csvUserWriter = csv.writer(csvUser)
csvLocation = open('location.csv', 'a')
csvLocationWriter = csv.writer(csvLocation)

searched_tweets = [status for status in tweepy.Cursor(api.search, q="#h1b").items(1)]

csvTweetWriter.writerow(['id','text','created_at','retweet_count','favorite_count', 'user_id'])
csvUserWriter.writerow(['id','name','location','friends_count'])
csvLocationWriter.writerow(['place_type','full_name','country'])

for tweet in searched_tweets:
    csvTweetWriter.writerow([tweet.id, tweet.text, tweet.created_at, tweet.retweet_count, tweet.favorite_count, tweet.user.id])
    csvUserWriter.writerow([tweet.user.id, tweet.user.name, tweet.user.location, tweet.user.friends_count])
    #csvLocationWriter.writerow([tweet.place.country])
