"""."""
from bs4 import BeautifulSoup

import requests


def hacker_recon(user_name):
    """Check for hackernews account with user_name."""
    url = 'https://news.ycombinator.com/user?id={}'.format(user_name)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    if b'No such user.' in r.content:
        return {'site': 'Hackernews',
                'empty': 'No hackernews account with that user name.'
                }
    try:
        tds = soup.find_all('td')
        about = tds[4].find_all('td')[7].contents[0].strip()
        return {'site': 'Hackernews',
                'about': about
                }
    except:
        return {'site': 'Hackernews',
                'empty': 'No hackernews account with that user name.'
                }
