"""OSInt scraper views."""

from pyramid.view import view_config
from github import GitHub
from ..models import GHModel


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    """Home view."""
    return {}


@view_config(route_name='results', renderer='../templates/results.jinja2')
def results_view(request):
    """Result view."""
    gh = GitHub()
    ghuser = gh.users(request.params['handle']).get()
    # res = GHModel(
    #     id=ghuser.id,
    #     login=ghuser.login,
    #     avatar_url=ghuser.avatar_url,
    #     location=ghuser.location,
    #     bio=ghuser.bio,
    #     )
    # import pdb; pdb.set_trace()
    return {'user': ghuser}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Result view."""
    return {
    }
