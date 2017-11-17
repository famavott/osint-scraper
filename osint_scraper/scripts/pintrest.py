"""."""
import requests

from bs4 import BeautifulSoup


def pinterest_recon(user_name):
    """Pinterest scraper."""
    url = 'https://www.pinterest.com/{}/'.format(user_name)
    r = requests.get(url)
    try:
        soup = BeautifulSoup(r.content, 'lxml')
        name = soup.find('h3').contents[0]
        avatar = soup.find('img', class_="_mi _3i _2h _3u").attrs['src']
        return {'site': 'Pinterest',
                'name': name,
                'avatar': avatar,
                'url': url
                }
    except:
        return {'site': 'Pinterest',
                'empty': 'No Pinterest with that username.'
        }
