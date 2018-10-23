
import tweepy
import csv
from sqlalchemy import create_engine
import pandas as pd

tweetData = pd.read_csv('tweet.csv')
userData = pd.read_csv('user.csv')
engine = create_engine('sqlite:///:memory:')

tweetData.to_sql('tweet_table', engine)
res1 = pd.read_sql_query('SELECT * FROM tweet_table', engine)
print('Result 1')
print(res1)
print('')

userData.to_sql('user_table', engine)
res1 = pd.read_sql_query('SELECT * FROM user_table', engine)
print('Result 1')
print(res1)
print('')
