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

    def recon_handler(user_name=None, email=None):
        """Recon function handler."""
        if user_name:
            ghuser = _thread.start_new_thread(github_recon, (user_name,))
            twit = _thread.start_new_thread(twitter_recon, (user_name,))
            yout = _thread.start_new_thread(youtube_recon, (user_name,))
            imgur = _thread.start_new_thread(imgur_recon, (user_name,))
            wiki = _thread.start_new_thread(wikipedia_recon, (user_name,))
            steam = _thread.start_new_thread(steam_recon, (user_name,))
            lleak = _thread.start_new_thread(liveleak_recon, (user_name,))
            p_bucket = _thread.start_new_thread(photobucket_recon, (user_name,))
            flickr = _thread.start_new_thread(flickr_recon, (user_name,))
            hacker = _thread.start_new_thread(hacker_recon, (user_name,))
            reddit = _thread.start_new_thread(reddit_recon, (user_name,))
        else:
            ghuser = twit = yout = imgur = wiki = lleak = steam = p_bucket = flickr = hacker = reddit = None
        if email:
            pwned = _thread.start_new_thread(pwned_recon, (email,))
            facebook = _thread.start_new_thread(facebook_recon, (email,))
            hacked_emails = _thread.start_new_thread(hacked_email_recon, (email,))
        else:
            pwned = facebook = hacked_emails = None
        return {'facebook': facebook,
                'twit': twit,
                'yout': yout,
                'lleak': lleak,
                'ghuser': ghuser,
                'reddit': reddit,
                'steam': steam,
                'imgur': imgur,
                'p_bucket': p_bucket,
                'flickr': flickr,
                'hacker': hacker,
                'wiki': wiki,
                'pwned': pwned,
                'hacked_emails': hacked_emails
                }


def recon_handler(user_name=None, email=None):
    """Recon function handler."""
    if user_name:
        startTime = time.time()
        ghuser = github_recon(user_name)
        print('git', startTime - time.time())
        startTime = time.time()
        twit = twitter_recon(user_name)
        print('twit',startTime - time.time())
        startTime = time.time()
        yout = youtube_recon(user_name)
        print('you', startTime - time.time())
        startTime = time.time()
        imgur = imgur_recon(user_name)
        print('imgur', startTime - time.time())
        startTime = time.time()
        wiki = wikipedia_recon(user_name)
        print('wiki', startTime - time.time())
        startTime = time.time()
        steam = steam_recon(user_name)
        print('steam', startTime - time.time())
        startTime = time.time()
        lleak = liveleak_recon(user_name)
        print('lleak', startTime - time.time())
        startTime = time.time()
        p_bucket = photobucket_recon(user_name)
        print('pbucket', startTime - time.time())
        startTime = time.time()
        flickr = flickr_recon(user_name)
        print('flkr', startTime - time.time())
        startTime = time.time()
        hacker = hacker_recon(user_name)
        print('hacknews', startTime - time.time())
        startTime = time.time()
        reddit = reddit_recon(user_name)
        print('reddit', startTime - time.time())
        startTime = time.time()
    else:
        ghuser = twit = yout = imgur = wiki = lleak = steam = p_bucket = flickr = hacker = reddit = None
    if email:
        pwned = pwned_recon(email)
        print('pwnd', startTime - time.time())
        startTime = time.time()
        facebook = facebook_recon(email)
        print('facebook', startTime - time.time())
        startTime = time.time()
        hacked_emails = hacked_email_recon(email)
        print('hackmail', startTime - time.time())
        startTime = time.time()
    else:
        pwned = facebook = hacked_emails = None
    return {'facebook': facebook,
            'twit': twit,
            'yout': yout,
            'lleak': lleak,
            'ghuser': ghuser,
            'reddit': reddit,
            'steam': steam,
            'imgur': imgur,
            'p_bucket': p_bucket,
            'flickr': flickr,
            'hacker': hacker,
            'wiki': wiki,
            'pwned': pwned,
            'hacked_emails': hacked_emails
            }