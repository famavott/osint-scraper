"""Fixture and request setup for test."""


from pyramid.config import Configurator

import pytest

from osint_scraper.scripts.recon_handler import recon_handler


def main(global_config, **settings):
    """Function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()


@pytest.fixture
def name_example(scope="session"):
    """."""
    return recon_handler(user_name='wmaserati76')


@pytest.fixture
def email_example(scope="session"):
    """."""
    return recon_handler(email='wmaserati76@gmail.com')


@pytest.fixture
def non_name_example(scope="session"):
    """."""
    return recon_handler(user_name='dgfhjeldkslksdglkhsl')


@pytest.fixture
def non_email_example(scope="session"):
    """."""
    return recon_handler(email='xnxxn@xnx.com')


@pytest.fixture
def m_name_example(scope="session"):
    """."""
    return recon_handler(user_name='m')


@pytest.fixture
def jf_name_example(scope="session"):
    """."""
    return recon_handler(user_name='jf_112')


@pytest.fixture
def matt_name_example(scope="session"):
    """."""
    return recon_handler(user_name='matt')


@pytest.fixture
def tom_email_example(scope="session"):
    """."""
    return recon_handler(email='tom@gmail.com')
