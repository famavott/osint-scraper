"""Data gathering module."""
from __future__ import print_function

import os

from bs4 import BeautifulSoup

from github import GitHub

import pypwned

import requests

import tweepy


def twitter_recon(username):
    """Use requests and BS to find public twitter profile and harvest information from HTML."""
    twitter_con_key = os.environ.get('TWITTER_CON_KEY')
    twitter_con_secret = os.environ.get('TWITTER_CON_SECRET')
    twitter_token = os.environ.get('TWITTER_TOKEN')
    twitter_token_secret = os.environ.get('TWITTER_TOKEN_SECRET')
    auth = tweepy.OAuthHandler(twitter_con_key, twitter_con_secret)
    auth.set_access_token(twitter_token, twitter_token_secret)

    api = tweepy.API(auth)
    try:
        user = api.get_user(username)
        return {'site': 'Twitter',
                'results': user._json
                }
    except:
        return {'site': 'Twitter',
                'empty': 'No Twitter account with that username.'}


def pwned_recon(email):
    """Check HIBP if email has been compromised."""
    results = pypwned.getAllBreachesForAccount(email=email)
    return {'site': 'Have I been pwned.',
            'results': results
            }


def github_recon(user_name):
    """Github scraper."""
    gh = GitHub()
    try:
        ghuser = gh.users(user_name).get()
        return {'site': 'GitHub',
                'results': ghuser
                }
    except:
        return {'site': 'GitHub',
                'empty': 'No GitHub account with that username.'}


def facebook_recon(email):
    """Find facebook account if linked via email."""
    r = requests.get('https://www.facebook.com/search/people?q={}'
                     .format(email))
    return {'site': 'Facebook',
            'url': r.url
            }


def photobucket_recon(user_name):
    """Check for pb account with user_name."""
    r = requests.get('http://s594.photobucket.com/user/{}/profile/'
                     .format(user_name))
    try:
        soup = BeautifulSoup(r.content, "lxml")
        url = soup.find('input', 'linkcopy').attrs['value']
        avatar = soup.find('img', class_="avatar largeProfile").attrs['src']
        bio = soup.find('p', class_="description").contents[0].strip()
        return {'site': 'Photobucket',
                'url': url,
                'avatar': avatar,
                'bio': bio
                }
    except:
        return {'site': 'Photobucket',
                'empty': 'No Photobucket account with that name.'}


def youtube_recon(user_name):
    """Use tweepy to access user data if name found."""
    url = 'https://www.youtube.com/user/{}'.format(user_name)
    r = requests.get(url)
    if b'This channel does not exist.' in r.content:
        return {'site': 'YouTube',
                'empty': 'No YouTube account with that username.'
                }
    soup = BeautifulSoup(r.content, 'lxml')
    ava = soup.find('img', class_='channel-header-profile-image')
    avatar = ava.attrs['src']
    try:
        title = soup.find('span', id='channel-title').contents
    except:
        title = None
    return {'site': 'YouTube',
            'avatar': avatar,
            'title': title,
            'url': url
            }


def flickr_recon(user_name):
    """Check for flickr account with user_name."""
    url = 'https://www.flickr.com/people/{}/'.format(user_name)
    r = requests.get(url)
    try:
        soup = BeautifulSoup(r.content, "lxml")
        title = soup.find('h1').contents[0].strip()
        av_div = soup.find('div', class_='avatar').attrs['style']
        avatar = 'https:' + av_div.split(' ')[1][4:-2]
        location = soup.find('p', class_='cp-location').contents[0]
        return {'avatar': avatar,
                'title': title,
                'user_name': user_name,
                'url': url,
                'location': location,
                'site': 'Flickr'
                }
    except:
        return {'site': 'Flickr',
                'empty': 'No Flickr account with that username.'
                }


def hacker_recon(user_name):
    """Check for hackernews account with user_name."""
    url = 'https://news.ycombinator.com/user?id={}'.format(user_name)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    try:
        tds = soup.find_all('td')
        about = tds[4].find_all('td')[7].contents[0].strip()
        return {'site': 'Hackernews',
                'about': about,
                'url': url
                }
    except:
        return {'site': 'Hackernews',
                'empty': 'No Hackernews account with that username.'
                }


def imgur_recon(user_name):
    """Check for imgur account with user_name."""
    url = 'https://imgur.com/user/{}'.format(user_name)
    r = requests.get(url)
    try:
        soup = BeautifulSoup(r.content, 'html.parser')
        bio = soup.find('div', id='account-bio').contents[0]
        a_date = soup.find('div', class_='textbox bold')
        acct_date = a_date.contents[2].split('\n')[1].strip()
        return {'acct_date': acct_date,
                'bio': bio,
                'url': url,
                'site': 'Imgur'
                }
    except:
        return {'site': 'Imgur',
                'empty': 'No Imgur account with that username.'
                }


def hacked_email_recon(email):
    """Check if email matches possible hacked emails from various breaches."""
    url = 'https://hacked-emails.com/api?q={}'.format(email)
    r = requests.get(url)
    to_dict = dict(r.json())
    return {
        'hack_dict': to_dict,
        'site': 'Hacked Emails'
    }


def wikipedia_recon(user_name):
    """Check for pb account with user_name."""
    url = 'https://en.wikipedia.org/wiki/User:{}'.format(user_name)
    r = requests.get(url)
    if r.status_code == 404:
        return {'site': 'Wikipedia',
                'empty': 'No Wikipedia account with that username.'
                }
    else:
        return {'site': 'Wikipedia',
                'url': url
                }


def steam_recon(user_name):
    """Check for steam account with user_name."""
    url = 'https://steamcommunity.com/id/{}'.format(user_name)
    r = requests.get(url)
    if 'Sorry!' in r.text:
        return {'site': 'Steam',
                'empty': 'No Steam account with that username.'
                }
    if 'This profile is private.' in r.text:
        soup = BeautifulSoup(r.content, 'lxml')
        ava = soup.find('div', class_="playerAvatarAutoSizeInner")
        avatar = ava.find('img').attrs['src']
        real_name = soup.find('span', class_='actual_persona_name').contents[0]
        return {'site': 'Steam',
                'avatar': avatar,
                'real_name': real_name,
                'location': 'Private account',
                'bio': 'Private account'
                }
    else:
        soup = BeautifulSoup(r.content, 'lxml')
        ava = soup.find('div', class_="playerAvatarAutoSizeInner")
        avatar = ava.find('img').attrs['src']
        real_name = soup.find('span', class_='actual_persona_name').contents[0]
        loc = soup.find('div', class_='header_real_name ellipsis')
        location = loc.contents[-1].strip()
        bio = soup.find('div', class_='profile_summary').contents[0].strip()
        return {'site': 'Steam',
                'avatar': avatar,
                'real_name': real_name,
                'location': location,
                'bio': bio
                }


def liveleak_recon(user_name):
    """Check for liveleak account with user_name."""
    url = 'https://www.liveleak.com/c/{}'.format(user_name)
    r = requests.get(url)
    if 'Channel cannot be found!' in r.text:
        return {'site': 'LiveLeak',
                'empty': 'No LiveLeak account with that username.'
                }
    else:
        soup = BeautifulSoup(r.content, 'lxml')
        loc = soup.find('h1').next_sibling.next_sibling.next_sibling
        location = loc.next_sibling.find('span').contents[0]
        memb = soup.find('h1').next_sibling.next_sibling.next_sibling.\
            next_sibling.next_sibling.next_sibling.find('span').contents[0]
        return {'site': 'LiveLeak',
                'location': location,
                'memb_since': memb,
                'url': url
                }


def reddit_recon(user_name):
    """Check for reddit account information."""
    url = 'https://www.reddit.com/user/{}'.format(user_name)
    r = requests.get(url, headers={'User-agent': 'Wayne Mazerati'})
    try:
        soup = BeautifulSoup(r.content, 'lxml')
        sub_list = []
        for i in soup.find_all('a', class_='subreddit hover'):
            sub_list.append(i.contents[0])
        age = soup.find('span', class_='age').contents[1].contents[0]
        return {
            'site': 'reddit',
            'url': url,
            'sub_list': sub_list,
            'age': age
        }
    except:
        return {
            'site': 'reddit',
            'empty': 'No reddit account with this username.'
        }
