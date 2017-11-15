"""Handle the recon functions."""
from .recon import (facebook_recon,
                    github_recon,
                    hacked_email_recon,
                    imgur_recon,
                    pwned_recon,
                    twitter_recon,
                    youtube_recon)


def recon_handler(user_name=None, email=None):
    """Recon function handler."""
    if user_name:
        ghuser = github_recon(user_name)
        twit = twitter_recon(user_name)
        yout = youtube_recon(user_name)
        imgur = imgur_recon(user_name)
    else:
        ghuser = twit = yout = imgur = None
    if email:
        pwned = pwned_recon(email)
        facebook = facebook_recon(email)
        hacked_emails = hacked_email_recon(email)
    else:
        pwned = facebook = None
    return {'ghuser': ghuser,
            'twit': twit,
            'yout': yout,
            'pwned': pwned,
            'facebook': facebook,
            'imgur': imgur,
            'hacked_emails': hacked_emails
            }
