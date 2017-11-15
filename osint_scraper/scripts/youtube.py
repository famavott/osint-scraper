"""."""
import os
from urllib2 import urlopen
import json


def youtube_recon(username):
    """Use tweepy to access user data if name found."""
    youtube_key = os.environ.get('YOUTUBE_KEY')
    baseurl = 'https://www.googleapis.com/youtube/v3/'
    url = '{0}search?part=snippet&q={1}&key={2}'.format(baseurl,
                                                        username,
                                                        youtube_key)
    try:
        rawres = urlopen(url)
        res = rawres.read()
        response = json.loads(res)
        # response['items'][0]
    except:
        return None
    return response
