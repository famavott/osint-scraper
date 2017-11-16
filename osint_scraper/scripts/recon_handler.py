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
        ghuser = []
        twit = []
        yout = []
        imgur = []
        wiki = []
        steam = []
        lleak = []
        p_bucket = []
        flickr = []
        hacker = []
        for user in user_name:
            ghuser.append(github_recon(user))
            twit.append(twitter_recon(user))
            yout.append(youtube_recon(user))
            imgur.append(imgur_recon(user))
            wiki.append(wikipedia_recon(user))
            steam.append(steam_recon(user))
            lleak.append(liveleak_recon(user))
            p_bucket.append(photobucket_recon(user))
            flickr.append(flickr_recon(user))
            hacker.append(hacker_recon(user))
    else:
        ghuser = twit = yout = imgur = wiki = lleak = steam = p_bucket = flickr = hacker = None
    if email:
        pwned = []
        facebook = []
        hacked_emails = []
        for item in email:
            pwned.append(pwned_recon(email))
            facebook.append(facebook_recon(email))
            hacked_emails.append(hacked_email_recon(email))
    else:
        pwned = facebook = hacked_emails = None
    return {'facebook': facebook,
            'twit': twit,
            'yout': yout,
            'lleak': lleak,
            'ghuser': ghuser,
            'steam': steam,
            'imgur': imgur,
            'p_bucket': p_bucket,
            'flickr': flickr,
            'hacker': hacker,
            'wiki': wiki,
            'pwned': pwned,
            'hacked_emails': hacked_emails
            }
