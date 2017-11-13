"""File to retreive information from Twitter API using tweepy."""
from __future__ import print_function

import tweepy


def twitter_recon(username):
    """Use tweepy to access user data if name found."""
    auth = tweepy.OAuthHandler('Fo6Cb2s8N8VrQpUgNlK5sAq8E', 'WdswCbCKB3Sxf6DSiqdfbKSSHUL13cBfaMwspRnVbEdpYx06XL')
    auth.set_access_token('930148182306185216-1pWbHMuEmA4p8f5qAmIqLAo9xMihppT', 'OxvbfBshhjv6ZL5lwvttJHDGEAlCAaBWbLjpTBU5Yb2yI')

    api = tweepy.API(auth)
    user = api.get_user(username)
    return user








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