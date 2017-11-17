"""Handle the recon functions."""
from .recon import (facebook_recon,
                    flickr_recon,
                    github_recon,
                    hacked_email_recon,
                    # hacker_recon,
                    imgur_recon,
                    liveleak_recon,
                    medium_recon,
                    photobucket_recon,
                    pinterest_recon,
                    pwned_recon,
                    steam_recon,
                    twitter_recon,
                    wikipedia_recon,
                    youtube_recon,
                    reddit_recon)


def recon_handler(user_name=None, email=None):
    """Recon function handler."""
    if user_name:
        ghuser = github_recon(user_name)
        twit = twitter_recon(user_name)
        yout = youtube_recon(user_name)
        imgur = imgur_recon(user_name)
        wiki = wikipedia_recon(user_name)
        steam = steam_recon(user_name)
        lleak = liveleak_recon(user_name)
        p_bucket = photobucket_recon(user_name)
        flickr = flickr_recon(user_name)
        # hacker = hacker_recon(user_name)
        reddit = reddit_recon(user_name)
        pinterest = pinterest_recon(user_name)
        medium = medium_recon(user_name)
    else:
        ghuser = twit = yout = imgur = wiki = lleak = steam = p_bucket = flickr = reddit = pinterest = medium = None
    if email:
        pwned = pwned_recon(email)
        facebook = facebook_recon(email)
        hacked_emails = hacked_email_recon(email)
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
            # 'hacker': hacker,
            'wiki': wiki,
            'pwned': pwned,
            'hacked_emails': hacked_emails,
            'pinterest': pinterest,
            'medium': medium
            }
