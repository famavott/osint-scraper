"""OSInt scraper views."""

from pyramid.view import view_config

from ..scripts.recon_handler import recon_handler


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    """Home view."""
    return {}


@view_config(route_name='results', renderer='../templates/results.jinja2')
def results_view(request):
    """Result view."""
    user_name = request.params['handle']
    email = request.params['email']
    return recon_handler(user_name, email)


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Result view."""
    return {
    }
