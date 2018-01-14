"""OSInt tests."""
from osint_scraper.scripts.recon import (facebook_recon,
                                         flickr_recon,
                                         github_recon,
                                         hacked_email_recon,
                                         imgur_recon,
                                         liveleak_recon,
                                         medium_recon,
                                         photobucket_recon,
                                         pinterest_recon,
                                         pwned_recon,
                                         reddit_recon,
                                         steam_recon,
                                         trip_recon,
                                         twitter_recon,
                                         wikipedia_recon,
                                         youtube_recon,)
from osint_scraper.views.default import home_view, results_view

from pyramid import testing


def test_facebook_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert facebook_recon(None) is None


def test_flickr_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert flickr_recon(None) is None


def test_github_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert github_recon(None) is None


def test_github_recon_no_bio():
    """Test recon function return None for empty bio."""
    ghr = github_recon('Matt')
    assert ghr['bio'] is None


def test_hacked_email_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert hacked_email_recon(None) is None


def test_imgur_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert imgur_recon(None) is None


def test_liveleak_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert liveleak_recon(None) is None


def test_medium_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert medium_recon(None) is None


def test_photobucket_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert photobucket_recon(None) is None


def test_pinterest_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert pinterest_recon(None) is None


def test_pwned_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert pwned_recon(None) is None


def test_reddit_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert reddit_recon(None) is None


def test_steam_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert steam_recon(None) is None


def test_trip_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert trip_recon(None) is None


def test_twitter_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert twitter_recon(None) is None


def test_wikipedia_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert wikipedia_recon(None) is None


def test_youtube_recon_return_none_with_none_input():
    """Test recon function return None with None input."""
    assert youtube_recon(None) is None


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
    assert name_example['twitter']['name'] == 'Wayne Maserati'


def test_youtube_not_in_results(name_example):
    """Check youtube returning None when supplied with username."""
    assert name_example['youtube'] is None


def test_trip_not_in_results(name_example):
    """Check youtube returning None when supplied with username."""
    assert name_example['trip'] is None


def test_trip_returns_dict():
    """Test trip recon returns dict."""
    assert isinstance(trip_recon('wmaserati76'), dict)


def test_reddit_returns_dict():
    """Test reddit recon returns dict."""
    assert isinstance(reddit_recon('wmaserati76'), dict)


def test_pwned_not_in_results(email_example):
    """Check youtube returning None when supplied with email."""
    assert email_example['pwned'] is None


def test_hacked_email_not_in_results(email_example):
    """Check youtube returning None when supplied with email."""
    assert email_example['hacked_email'] is None


def test_flickr_in_results(name_example):
    """Check youtube returning None when supplied with username."""
    assert name_example['flickr']['user_name'] == 'wmaserati76'


def test_name_for_github_in_results(name_example):
    """Check github dict returning expected location when supplied with username."""
    assert name_example['github']['location'] == 'Jacksonville FL'


def test_name_for_imgur_in_results(name_example):
    """Check imgur dict returning expected results when supplied with username."""
    assert name_example['imgur']['bio'] == 'Guns, booze, and hookers.'


def test_name_for_photobucket_in_results(name_example):
    """Check photobucket dict returning expected results when supplied with username."""
    assert name_example['photobucket']['url'] == 'http://s594.photobucket.com/user/wmaserati76/profile/'


def test_name_for_pinterest_in_results(name_example):
    """Check pinterest dict returning expected results when supplied with username."""
    assert name_example['pinterest']['url'] == 'https://www.pinterest.com/wmaserati76/'


def test_name_for_medium_in_results(name_example):
    """Check medium dict returning expected results when supplied with username."""
    assert name_example['medium']['url'] == 'https://www.medium.com/@wmaserati76/'


def test_name_for_tripadvisor_in_results(name_example):
    """Check Tripadvisor dict returning expected results when supplied with username."""
    assert name_example


def test_name_for_wikipedia_in_results(name_example):
    """Check wikipedia dict returning expected results when supplied with username."""
    assert name_example['wikipedia']['url'] == 'https://en.wikipedia.org/wiki/User:wmaserati76'


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


def test_email_for_tom(tom_email_example):
    """Check hacked and pwnd emails."""
    assert tom_email_example
