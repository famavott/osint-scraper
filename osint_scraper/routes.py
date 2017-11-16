"""OSInt scraper routes."""


def includeme(config):
    """Include me for routes."""
    config.add_static_view('static', 'static', cache_max_age=100)
    config.add_route('home', '/')
    config.add_route('results', '/results')
