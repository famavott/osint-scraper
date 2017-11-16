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
    # import pdb; pdb.set_trace()
    if not request:
        return {}
    user_name = request.params['handle'].split()  # pragma: no cover
    email = request.params['email'].split()  # pragma: no cover
    return recon_handler(user_name, email)  # pragma: no cover


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Result view."""
    return {
    }
