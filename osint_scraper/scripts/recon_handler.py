"""Handle the recon functions."""
from .recon import (facebook_recon,
                    flickr_recon,
                    github_recon,
                    hacked_email_recon,
                    hacker_recon,
                    imgur_recon,
                    liveleak_recon,
                    photobucket_recon,
                    pwned_recon,
                    steam_recon,
                    twitter_recon,
                    wikipedia_recon,
                    youtube_recon)


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
        hacker = hacker_recon(user_name)
    else:
        ghuser = twit = yout = imgur = wiki = lleak = steam = p_bucket = flickr = hacker = None
    if email:
        pwned = pwned_recon(email)
        facebook = facebook_recon(email)
        hacked_emails = hacked_email_recon(email)
    else:
        pwned = facebook = hacked_emails = None
    return {'ghuser': ghuser,
            'twit': twit,
            'yout': yout,
            'pwned': pwned,
            'facebook': facebook,
            'imgur': imgur,
            'hacked_emails': hacked_emails,
            'wiki': wiki,
            'steam': steam,
            'lleak': lleak,
            'p_bucket': p_bucket,
            'flickr': flickr,
            'hacker': hacker
            }
