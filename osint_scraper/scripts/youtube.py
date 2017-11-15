"""."""
import json


def youtube_recon(user_name):
    """Use tweepy to access user data if name found."""
    # youtube_key = os.environ.get('YOUTUBE_KEY')
    # baseurl = 'https://www.googleapis.com/youtube/v3/'
    # url = '{0}search?part=snippet&q={1}&key={2}'.format(baseurl,
    #                                                     user_name,
    #                                                     youtube_key)
    url = 'https://www.youtube.com/user/{}'.format(user_name)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    avatar = soup.find('img', class_='channel-header-profile-image').attrs['src']
    title = soup.find('span', id='channel-title').contents
    return r
    # try:
    #     rawres = requests.get(url)
    #     res = rawres.read()
    #     response = json.loads(res)
    #     return {'site': 'YouTube',
    #             'results': response
    #             }
    # except:
    #     return {'site': 'YouTube',
    #             'empty': 'No YouTube account with that username.'
    #             }