import slack
from sqlalchemy import create_engine
import time
from passwords import SLACK_TOKEN

oauth_token = SLACK_TOKEN


def slack_text(slack_message):
    client = slack.WebClient(token=oauth_token)
    # def slack_text(slack_message):
    response = client.chat_postMessage(channel='#random', text=slack_message)
    return response


def get_text():
    HOST = 'postgresdb'
    PORT = '5432'
    USERNAME = 'postgres'
    PASSWORD = 'postgres'
    DB = 'tweetdb'
    conn_string = f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'

    engine = create_engine(conn_string)
    query = "SELECT text FROM tweets LIMIT 1;"
    result = engine.execute(query)
    for text in result:
        print(text)
    return text[0]


while True:
    time.sleep(40)
    slack_message = get_text()
    print('slack_message')
    slack_text(slack_message)
    time.sleep(30)
