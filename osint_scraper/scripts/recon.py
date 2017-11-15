"""Data gathering module."""
from __future__ import print_function

import os

from bs4 import BeautifulSoup

from github import GitHub

import pypwned

import requests

import tweepy

from urllib2 import urlopen

import json


def twitter_recon(username):
    """Use tweepy to access user data if name found."""
    twitter_con_key = os.environ.get('TWITTER_CON_KEY')
    twitter_con_secret = os.environ.get('TWITTER_CON_SECRET')
    twitter_token = os.environ.get('TWITTER_TOKEN')
    twitter_token_secret = os.environ.get('TWITTER_TOKEN_SECRET')
    auth = tweepy.OAuthHandler(twitter_con_key, twitter_con_secret)
    auth.set_access_token(twitter_token, twitter_token_secret)

    api = tweepy.API(auth)
    try:
        user = api.get_user(username)
    except:
        return None
    return user._json


def pwned_recon(email):
    """Check HIBP if email has been compromised."""
    results = pypwned.getAllBreachesForAccount(email=email)
    return results


def github_recon(user_name):
    """Github scraper."""
    gh = GitHub()
    try:
        ghuser = gh.users(user_name).get()
    except:
        return None
    return ghuser


def facebook_recon(email):
    """Find facebook account if linked via email."""
    try:
        r = requests.get('https://www.facebook.com/search/people?q={}'.format(email))
        return r.url
    except:
        r = None


def photobucket_recon(user_name):
    """Check for pb account with user_name."""
    r = requests.get('http://s594.photobucket.com/user/{}/profile/'
                     .format(user_name))
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "lxml")
        return soup.find('input', 'linkcopy').attrs['value']
    else:
        return None

    # friends_count
    # followers_count
    # location
    # screen_name
    # id
    # description
    # geo_enabled
    # statuses_count
    # profile_image_url
    # profile_image_url_https
    # lang
    # created_at
    # url


def youtube_recon(username):
    """Use tweepy to access user data if name found."""
    youtube_key = os.environ.get('YOUTUBE_KEY')
    baseurl = 'https://www.googleapis.com/youtube/v3/'
    url = '{0}search?part=snippet&q={1}&key={2}'.format(baseurl, username, youtube_key)

    try:
        rawres = urlopen(url)
        res = rawres.read()
        response = json.loads(res)
        # response['items'][0]
        return response
    except:
        return None
