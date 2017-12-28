"""Handle the recon functions."""
import asyncio

import aiohttp

from .recon import (facebook_recon,
                    flickr_recon,
                    github_recon,
                    hacked_email_recon,
                    imgur_recon,
                    liveleak_recon,
                    medium_recon,
                    photobucket_recon,
                    pinterest_recon,
                    # pwned_recon,
                    reddit_recon,
                    steam_recon,
                    trip_recon,
                    twitter_recon,
                    wikipedia_recon,
                    youtube_recon,)

return_dict = {}


async def get_parsed_soups(key_name, function, email_username, url):
    """."""
    if email_username:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={'User-agent': 'Wayne Mazerati'}) as resp:
                text = await resp.read()
        return_dict[key_name] = function(text.decode('utf-8'), url)
    else:
        return_dict[key_name] = None


def recon_handler(user_name=None, email=None):
    """Recon function handler."""
    params = [('ghuser', github_recon, user_name,
               'https://github.com/{}'.format(user_name)),
              ('twit', twitter_recon, user_name,
               'https://www.twitter.com/{}'.format(user_name)),
              ('yout', youtube_recon, user_name,
               'https://www.youtube.com/user/{}'.format(user_name)),
              ('imgur', imgur_recon, user_name,
               'https://imgur.com/user/{}'.format(user_name)),
              ('wiki', wikipedia_recon, user_name,
               'https://en.wikipedia.org/wiki/User:{}'.format(user_name)),
              ('steam', steam_recon, user_name,
               'https://steamcommunity.com/id/{}'.format(user_name)),
              ('lleak', liveleak_recon, user_name,
               'https://www.liveleak.com/c/{}'.format(user_name)),
              ('p_bucket', photobucket_recon, user_name,
               'http://s594.photobucket.com/user/{}/profile/'.format(user_name)),
              ('flickr', flickr_recon, user_name,
               'https://www.flickr.com/people/{}/'.format(user_name)),
              ('reddit', reddit_recon, user_name,
               'https://www.reddit.com/user/{}'.format(user_name)),
              ('pinterest', pinterest_recon, user_name,
               'https://www.pinterest.com/{}/'.format(user_name)),
              ('medium', medium_recon, user_name,
               'https://www.medium.com/@{}/'.format(user_name)),
              ('trip', trip_recon, user_name,
               'https://www.tripadvisor.com/members/{}'.format(user_name)),
              ('facebook', facebook_recon, email,
               'https://www.facebook.com/search/people?q={}'.format(email)),
              # ('pwned', pwned_recon, None, None),
              ('hacked_emails', hacked_email_recon, email,
               'https://hacked-emails.com/api?q={}'.format(email))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(
            *(get_parsed_soups(*args) for args in params)
        )
    )
    return return_dict
