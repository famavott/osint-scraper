"""OSInt scraper views."""


from pyramid.view import view_config

from ..scripts.recon import facebook_recon, github_recon, pwned_recon, twitter_recon


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    """Home view."""
    return {}


@view_config(route_name='results', renderer='../templates/results.jinja2')
def results_view(request):
    """Result view."""
    user_name = request.params['handle']
    email = request.params['email']
    if user_name:
        ghuser = github_recon(user_name)
        twit = twitter_recon(user_name)
    else:
        ghuser = twit = None

    if email:
        pwned = pwned_recon(email)
        facebook = facebook_recon(email)
    else:
        pwned = None
        facebook = None
    return {'ghuser': ghuser,
            'twit': twit,
            'pwned': pwned,
            'facebook': facebook
            }


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Result view."""
    return {
    }
