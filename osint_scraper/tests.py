"""OSInt tests."""

from pyramid import testing

from pyramid.response import Response

from osint_scraper.scripts.recon_handler import recon_handler


def test_home_view_returns_response():
    """."""
    from osint_scraper.views.default import home_view
    request = testing.DummyRequest()
    response = home_view(request)
    assert isinstance(response, dict)


def test_result_view_returns_response():
    """."""
    from osint_scraper.views.default import results_view
    request = {}
    response = results_view(request)
    assert response == {}


def test_detail_view_returns_response():
    """."""
    from osint_scraper.views.default import detail_view
    request = testing.DummyRequest()
    response = detail_view(request)
    assert isinstance(response, dict)


def test_recon_handler_with_username(name_example):
    """."""
    assert isinstance(name_example, dict)


def test_recon_handler_with_email(email_example):
    """."""
    assert isinstance(email_example, dict)


def test_recon_handler_with_non_username(non_name_example):
    """."""
    assert isinstance(non_name_example, dict)


def test_recon_handler_with_non_email(non_email_example):
    """."""
    assert isinstance(non_email_example, dict)
