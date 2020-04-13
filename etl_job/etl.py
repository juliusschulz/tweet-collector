"""
Etl-job: Extract tweets from the MongoDB cleans preprocess it and stores
them in an SQL Database
"""

import time
import pymongo
from sqlalchemy import create_engine
from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


def extract_new_tweets():
    """
    - compare #entries to last run
    - look at the keys/ids of documents
    - look at timestamps
    """
    client = pymongo.MongoClient(host="mongodb", port=27017)
    tweet = client.tweet
    tweets = tweet.tweet
    tweet_list = [tweet for tweet in tweets.find({"tweet_location": {"$exists":
                  "true", "$ne": []}})]
    tweets.drop()
    return tweet_list


def transform_data(tweet):
    """
    - extract the text
    - run the sentiment analysis
    - refine by more keywords / doc size / sentiment
    """
    s = SentimentIntensityAnalyzer(emoji_lexicon='emoji_utf8_lexicon.txt')
    time_list = []
    text_list = []
    vscore_list = []
    longitude_list = []
    latitude_list = []

    for i in range(len(tweet)):
        time = pd.to_datetime(tweet[i]['tweet_created_at'])
        text = tweet[i]['text']
        vscore = s.polarity_scores(tweet[i]['text'])

        longitude = tweet[i]['tweet_location'][1][0][0][0]
        latitude = tweet[i]['tweet_location'][1][0][0][1]
        time_list.append(time)
        text_list.append(text)
        vscore_list.append(vscore['compound'])
        longitude_list.append(longitude)
        latitude_list.append(latitude)
    df = pd.DataFrame(list(zip(time_list, text_list,
                           vscore_list, longitude_list, latitude_list)),
                      columns=['time', 'text', 'v_score',
                               'longitude', 'latitude'])
    return df


def write_to_sql(x):
    """
    - store refined tweets in SQL
    - add a timestamp
    """
    pg = create_engine("postgres://postgres:postgres@postgresdb:5432/tweetdb")
    x.to_sql('tweets', con=pg, if_exists='append')  # check append mode


while True:
    pg = create_engine("postgres://postgres:postgres@postgresdb:5432/tweetdb")
    x = extract_new_tweets()
    time.sleep(10)
    x = transform_data(x)
    write_to_sql(x)
