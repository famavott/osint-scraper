"""Handle the recon functions."""
from .recon import (facebook_recon,
                    flickr_recon,
                    github_recon,
                    hacked_email_recon,
                    imgur_recon,
                    liveleak_recon,
                    medium_recon,
                    photobucket_recon,
                    pinterest_recon,
                    pwned_recon,
                    reddit_recon,
                    steam_recon,
                    trip_recon,
                    twitter_recon,
                    wikipedia_recon,
                    youtube_recon,)


def recon_handler(user_name=None, email=None, checks=None):
    """Recon function handler."""
    results = {}
    for check in checks:
        recon = eval(check + "_recon")
        if check in ['pwned', 'facebook', 'hacked_email']:
            results[check] = recon(email)
        else:
            results[check] = recon(user_name)
    return results
