import json
from twython import Twython
import random

# load creds.json
with open('creds.json') as infile:
    creds = json.load(infile)

APP_KEY = creds['APP_KEY']
APP_SECRET = creds["APP_SECRET"]
OAUTH_TOKEN = creds["OAUTH_TOKEN"]
OAUTH_TOKEN_SECRET = creds["OAUTH_TOKEN_SECRET"]
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def postTweet(phrase):
    twitter.update_status(status=phrase)
    

def main():
    postTweet('Hello World')

if __name__ == '__main__':
    main()

