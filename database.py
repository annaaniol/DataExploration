import tweepy
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

# configure Session class with desired options
Session = sessionmaker()

hashtags = ['h1b', 'visa']

for hashtag in hashtags:
    tweetData = pd.read_csv(hashtag+'.csv', usecols=['tweet_id', 'retweeted', 'tweet_text','tweet_created_at','tweet_retweet_count','tweet_favorite_count'])
    userData = pd.read_csv(hashtag+'.csv', usecols=['user_id','user_name','user_location','user_friends_count'])
    placeData = pd.read_csv(hashtag+'.csv', usecols=['place_type','place_full_name','country'])

    engine = create_engine('sqlite:///twitter.db')

    tweetData.to_sql('tweet', engine, if_exists='append')
    userData.to_sql('user', engine, if_exists='append')
    placeData.to_sql('place', engine, if_exists='append')

    res1 = pd.read_sql_query('SELECT DISTINCT * FROM tweet', engine)
    print('SELECT DISTINCT * FROM tweet')
    print(res1)
    print('')

    res2 = pd.read_sql_query('SELECT DISTINCT * FROM user', engine)
    print('SELECT DISTINCT * FROM user')
    print(res2)
    print('')

    res3 = pd.read_sql_query('SELECT * FROM place WHERE place_type is not null', engine)
    print('SELECT * FROM place WHERE place_type is not null')
    print(res3)
    print('')


# associate it with our custom Session class
Session.configure(bind=engine)
# work with the session
session = Session()
