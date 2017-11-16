"""Fixture and request setup for test."""

import os

from pyramid.config import Configurator

from pyramid.testing import DummyRequest

from pyramid import testing

import pytest

from osint_scraper.scripts.recon_handler import recon_handler

from osint_scraper.scripts.recon import (facebook_recon,
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


def main(global_config, **settings):
    """Function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    # config.include('.vendor')
    config.include('.models')
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
