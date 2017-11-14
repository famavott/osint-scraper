"""Data gathering module."""
from __future__ import print_function

import os

from github import GitHub

import pypwned

import requests

import tweepy


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
    ghuser = gh.users(user_name).get()
    return ghuser


def facebook_recon(email):
    """Find facebook account if linked via email."""
    try:
        r = requests.get('https://www.facebook.com/search/people?q={}'.format(email))
        return r.url
    except:
        r = None
