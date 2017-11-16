"""OSInt tests."""

from osint_scraper.scripts.recon_handler import recon_handler

from pyramid import testing

from pyramid.response import Response


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


def test_name_for_twit_in_results(name_example):
    """Check twitter dict returning expected result when supplied with username."""
    assert name_example['twit']['results']['name'] == 'Wayne Maserati'


def test_name_for_github_in_results(name_example):
    """Check github dict returning expected location when supplied with username."""
    assert name_example['ghuser']['results']['location'] == 'Jacksonville FL'


def test_name_for_imgur_in_results(name_example):
    """Check imgur dict returning expected results when supplied with username."""
    assert name_example['imgur']['bio'] == 'Guns, booze, and hookers.'


def test_name_for_photobucket_in_results(name_example):
    """Check photobucket dict returning expected results when supplied with username."""
    assert name_example['p_bucket']['url'] == 'http://s36.photobucket.com/user/wmaserati76/profile/'


def test_name_for_wikipedia_in_results(name_example):
    """Check wikipedia dict returning expected results when supplied with username."""
    assert name_example['wiki']['url'] == 'https://en.wikipedia.org/wiki/User:wmaserati76'


def test_email_for_facebook_account(email_example):
    """Check facebook dict to ensure correct link returned when supplied with email."""
    assert email_example['facebook']['url'] == 'https://www.facebook.com/search/people?q=wmaserati76@gmail.com'
