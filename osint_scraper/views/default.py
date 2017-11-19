"""OSInt scraper views."""

from pyramid.view import view_config

from ..scripts.recon_handler import recon_handler

# from ..scripts.dummy_recon import dummy_recon


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    """Home view."""
    return {}


@view_config(route_name='results', renderer='../templates/results.jinja2')
def results_view(request):
    """Result view."""
    if not request:
        return {}
    user_name = request.params['handle']  # pragma: no cover
    email = request.params['email']  # pragma: no cover
    return recon_handler(user_name, email)  # pragma: no cover
    # return dummy_recon(user_name, email)  # pragma: no cover
