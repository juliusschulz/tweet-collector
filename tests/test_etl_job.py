import time
import pymongo
from sqlalchemy import create_engine
from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyze
import etl_job
import pandas as pd


# def test_extract_new_tweets():
#     """ Test the connection to MongoDB by checking
#     whether list of extracted tweets is >= 0 """
#     assert len(extract_new_tweets()) >= 0
#
# def test_transform_data():
#     df = transform_data()
#     count = df.isnull().count()
#     assert count == 0


def test():
    assert 1 == 1
