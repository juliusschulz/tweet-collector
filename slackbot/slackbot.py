import slack
from sqlalchemy import create_engine
import time
#from passwords import SLACK_TOKEN

# oauth_token = SLACK_TOKEN
oauth_token = "xoxb-892207304208-960672730260-i65JRK74l36YAQYJDQvQ72bk"


def slack_text(slack_message):
    client = slack.WebClient(token=oauth_token)
    response = client.chat_postMessage(channel='#test_room', text=slack_message)
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
    for tweet in result:
        print(tweet)
    return tweet[0]


while True:
    time.sleep(40)
    slack_message = get_text()
    slack_text(slack_message)
    time.sleep(30)
