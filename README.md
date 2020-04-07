# tweet-collector

[![Build Status](https://travis-ci.org/juliusschulz/tweet-collector.svg?branch=master)](https://travis-ci.org/juliusschulz/tweet-collector)

A Dockerized Data Pipeline that analyzes the sentiment of tweets.


![pipeline_structure](pipeline_structure.png)

## Usage
```
docker-compose build

docker-compose up
```

## Main components
1. tweet-collector
     - collect tweets with certain hashtags and store them in a MongoDB
2. etl-job
     - extract tweets from MongoDB
     - add sentiment analysis
     - store cleaned tweets in an SQL Database
3. slackbot
     - grab tweets from SQL Database that can be posted on slack
