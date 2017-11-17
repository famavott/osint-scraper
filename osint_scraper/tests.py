"""OSInt tests."""

from pyramid import testing

from pyramid.response import Response

from osint_scraper.views.default import results_view

from osint_scraper.views.default import home_view


def test_home_view_returns_response():
    """Test_home_view_returns_response."""
    request = testing.DummyRequest()
    response = home_view(request)
    assert isinstance(response, dict)


def test_result_view_returns_response():
    """Test_result_view_returns_response."""
    request = {}
    response = results_view(request)
    assert response == {}


def test_recon_handler_with_username(name_example):
    """Test_recon_handler_with_username."""
    assert isinstance(name_example, dict)


def test_recon_handler_with_email(email_example):
    """Test_recon_handler_with_email."""
    assert isinstance(email_example, dict)


def test_recon_handler_with_non_username(non_name_example):
    """Test_recon_handler_with_non_username."""
    assert isinstance(non_name_example, dict)


def test_recon_handler_with_non_email(non_email_example):
    """Test_recon_handler_with_non_email."""
    assert isinstance(non_email_example, dict)


def test_name_for_twit_in_results(name_example):
    """Check twitter dict returning expected result when supplied with username."""
    assert name_example['twit']['name'] == 'Wayne Maserati'


def test_name_for_github_in_results(name_example):
    """Check github dict returning expected location when supplied with username."""
    assert name_example['ghuser']['location'] == 'Jacksonville FL'


def test_name_for_imgur_in_results(name_example):
    """Check imgur dict returning expected results when supplied with username."""
    assert name_example['imgur']['bio'] == 'Guns, booze, and hookers.'


def test_name_for_photobucket_in_results(name_example):
    """Check photobucket dict returning expected results when supplied with username."""
    assert name_example['p_bucket']['url'] == 'http://s36.photobucket.com/user/wmaserati76/profile/'


def test_name_for_pinterest_in_results(name_example):
    """Check pinterest dict returning expected results when supplied with username."""
    assert name_example['pinterest']['url'] == 'https://www.pinterest.com/wmaserati76/'


def test_name_for_wikipedia_in_results(name_example):
    """Check wikipedia dict returning expected results when supplied with username."""
    assert name_example['wiki']['url'] == 'https://en.wikipedia.org/wiki/User:wmaserati76'


def test_email_for_facebook_account(email_example):
    """Check facebook dict to ensure correct link returned when supplied with email."""
    assert email_example['facebook']['url'] == 'https://www.facebook.com/search/people?q=wmaserati76@gmail.com'


def test_name_for_m_account(m_name_example):
    """Check test name m to up coverage."""
    assert m_name_example


def test_name_for_jf_account(jf_name_example):
    """Check test name jf to up coverage."""
    assert jf_name_example


def test_name_for_matt_account(matt_name_example):
    """Check steam private account."""
    assert matt_name_example
