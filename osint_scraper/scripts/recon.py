"""Data gathering module."""
from __future__ import print_function

from bs4 import BeautifulSoup

import pypwned

import requests


def social_soup(url):
    """Return social soup."""
    r = requests.get(url, headers={'User-agent': 'Wayne Mazerati'})
    return BeautifulSoup(r.content, 'lxml')


def twitter_recon(user_name):
    """Use requests and BS to find public twitter profile and harvest information from HTML."""
    if not user_name:
        return None
    try:
        url = 'https://www.twitter.com/{}'.format(user_name)
        soup = social_soup(url)
        name = soup.find('h1').contents[1].text
        try:
            location = soup.find('span', class_='ProfileHeaderCard-locationText u-dir').contents[1].text
        except:
            location = None
        description = soup.find('div', class_='ProfileHeaderCard').contents[5].text
        created_at = soup.find('div', class_='ProfileHeaderCard-joinDate').contents[3].text
        avatar = soup.find('div', class_='ProfileAvatar').find('img', class_='ProfileAvatar-image').get('src')
        try:
            recent_tweet = soup.find('div', class_='content').find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
        except:
            recent_tweet = None
    except:
        return {'site': 'Twitter',
                'empty': 'No Twitter account with that username'
                }
    return {'site': 'Twitter',
            'name': name,
            'location': location,
            'description': description,
            'created_at': created_at,
            'avatar': avatar,
            'recent_tweet': recent_tweet,
            'url': url
            }


def pwned_recon(email):
    """Check HIBP if email has been compromised."""
    if not email:
        return None
    results = pypwned.getAllBreachesForAccount(email=email)
    if '404' in results:
        return {'site': 'Have I been pwnded',
                'empty': 'Email has not been compromised.'}
    return {'site': 'Have I been pwned.',
            'results': results
            }


def github_recon(user_name):
    """Github scraper."""
    if not user_name:
        return None
    url = 'https://github.com/{}'.format(user_name)
    try:
        soup = social_soup(url)
        avatar_url = soup.find('img', class_="avatar width-full rounded-2").get('src')
        name = soup.find('span', class_="p-name vcard-fullname d-block").contents[0]
        location = soup.find('span', class_="p-label").contents[0]
        try:
            bio = soup.find('div', class_='p-note user-profile-bio').find('div').contents[0]
        except:
            bio = None
        return {'site': 'GitHub',
                'avatar_url': avatar_url,
                'login': user_name,
                'name': name,
                'location': location,
                'bio': bio,
                'url': url
                }
    except:
        return {'site': 'GitHub',
                'empty': 'No GitHub account with that username.'}


def facebook_recon(email):
    """Find facebook account if linked via email."""
    if not email:
        return None
    return {'site': 'Facebook',
            'url': 'https://www.facebook.com/search/people?q={}'.format(email)
            }


def photobucket_recon(user_name):
    """Check for pb account with user_name."""
    if not user_name:
        return None
    url = 'http://s594.photobucket.com/user/{}/profile/'.format(user_name)
    try:
        soup = social_soup(url)
        avatar = soup.find('img', class_="avatar largeProfile").get('src')
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
    if not user_name:
        return None
    url = 'https://www.youtube.com/user/{}'.format(user_name)
    r = requests.get(url)
    if b'This channel does not exist.' in r.content:
        return {'site': 'YouTube',
                'empty': 'No YouTube account with that username.'
                }
    soup = BeautifulSoup(r.content, 'lxml')
    avatar = soup.find('img', class_='channel-header-profile-image').get('src')
    # avatar = ava.attrs['src']
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
    if not user_name:
        return None
    url = 'https://www.flickr.com/people/{}/'.format(user_name)
    try:
        soup = social_soup(url)
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


def imgur_recon(user_name):
    """Check for imgur account with user_name."""
    if not user_name:
        return None
    url = 'https://imgur.com/user/{}'.format(user_name)
    try:
        soup = social_soup(url)
        try:
            bio = soup.find('div', id='account-bio').contents[0]
        except:
            bio = None
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
    if not email:
        return None
    url = 'https://hacked-emails.com/api?q={}'.format(email)
    r = requests.get(url)
    to_dict = dict(r.json())
    if to_dict['results'] == 0:
        return {'site': 'Hacked Emails',
                'empty': 'Email has not been compromised.'}
    return {
        'hack_dict': to_dict,
        'site': 'Hacked Emails'
    }


def wikipedia_recon(user_name):
    """Check for pb account with user_name."""
    if not user_name:
        user_name is None
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
    if not user_name:
        return None
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
                'bio': 'Private account',
                'url': url
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
                'bio': bio,
                'url': url
                }


def liveleak_recon(user_name):
    """Check for liveleak account with user_name."""
    if not user_name:
        return None
    url = 'https://www.liveleak.com/c/{}'.format(user_name)
    r = requests.get(url)
    if 'Channel cannot be found!' in r.text:
        return {'site': 'LiveLeak',
                'empty': 'No LiveLeak account with that username.'
                }
    else:
        soup = BeautifulSoup(r.content, 'lxml')
        loc = soup.find('h1').next_sibling.next_sibling.next_sibling
        try:
            location = loc.next_sibling.find('span').contents[0]
        except:
            location = None
        memb = soup.find('h1').next_sibling.next_sibling.next_sibling.\
            next_sibling.next_sibling.next_sibling.find('span').contents[0]
        return {'site': 'LiveLeak',
                'location': location,
                'memb_since': memb,
                'url': url
                }


def reddit_recon(user_name):
    """Check for reddit account information."""
    if not user_name:
        return None
    url = 'https://www.reddit.com/user/{}'.format(user_name)
    try:
        soup = social_soup(url)
        sub_list = []
        for i in soup.find_all('a', class_='subreddit hover'):
            sub_list.append(i.contents[0])
        sub_list = list(set(sub_list))
        age = soup.find('span', class_='age').contents[1].contents[0]
        return {
            'site': 'Reddit',
            'url': url,
            'sub_list': sub_list,
            'age': age
        }
    except:
        return {
            'site': 'reddit',
            'empty': 'No reddit account with this username.'
        }


def pinterest_recon(user_name):
    """Pinterest scraper."""
    if not user_name:
        return None
    url = 'https://www.pinterest.com/{}/'.format(user_name)
    try:
        soup = social_soup(url)
        name = soup.find('h3').contents[0]
        avatar = soup.find('img', class_="_mi _3i _2h _3u").get('src')
        return {'site': 'Pinterest',
                'name': name,
                'avatar': avatar,
                'url': url
                }
    except:
        return {'site': 'Pinterest',
                'empty': 'No Pinterest with that username.'
                }


def medium_recon(user_name):
    """Grab data for Medium if it exists."""
    if not user_name:
        return None
    url = 'https://www.medium.com/@{}/'.format(user_name)
    try:
        soup = social_soup(url)
        name = soup.find('h1').text
        avatar = soup.find('div', class_='hero-avatar').find('img')['src']
        article = soup.find('div', class_='compressedPostListItem-title').text
        return {'site': 'Medium',
                'name': name,
                'avatar': avatar,
                'article': article,
                'url': url
                }
    except:
        return {'site': 'Medium',
                'empty': 'No Medium with that username.'
                }


def trip_recon(user_name):
    """Tripadvisor scraper."""
    if not user_name:
        return None
    url = 'https://www.tripadvisor.com/members/{}'.format(user_name)
    try:
        soup = social_soup(url)
        name = soup.find('span', class_='nameText').contents[0]
        avatar = soup.find('img', class_="avatarUrl").get('src')
        try:
            location = soup.find('div', class_="hometown").contents[0].contents[0]
        except:
            location = None
        return {'site': 'Tripadvisor',
                'name': name,
                'avatar': avatar,
                'url': url,
                'location': location
                }
    except:
        return {'site': 'Tripadvisor',
                'empty': 'No Tripadvisor with that username.'
                }
