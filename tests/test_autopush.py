import pytest
from pages.autopush import AutopushTestPage 


@pytest.mark.nondestructive
def test_third_party_tracker_loads_correctly(base_url, selenium):
    page = AutopushTestPage(selenium, base_url).open()

    assert page.third_party_loads_correctly


@pytest.mark.nondestructive
def test_first_party_tracker_loads_correctly(base_url, selenium):
    page = AutopushTestPage(selenium, base_url).open()

    assert page.first_party_loads_correctly


@pytest.mark.nondestructive
def test_DNT_signal_correctly_sent(base_url, selenium):
    page = AutopushTestPage(selenium, base_url).open()

    assert page.dnt_signal_correctly_sent
