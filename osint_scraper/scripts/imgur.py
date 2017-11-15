"""Find imgur account information if username match is found."""

from bs4 import BeautifulSoup

import requests


def imgur_recon(user_name):
    """Check for imgur account with user_name."""
    url = 'https://imgur.com/user/{}'.format(user_name)
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        bio = soup.find('div', id='account-bio').contents[0]
        acct_date = soup.find('div', class_='textbox bold').contents[2].split('\n')[1].strip()
        return {'acct_date': acct_date,
                'bio': bio,
                'link': 'https://imgur.com/user/{}'.format(user_name),
                'site': 'Imgur'
                }
    else:
        return None
