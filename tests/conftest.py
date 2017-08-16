import ConfigParser
import pytest

from foxpuppet import FoxPuppet


@pytest.fixture
def browser(foxpuppet):
    """Initial Firefox browser window."""
    return foxpuppet.browser


@pytest.fixture()
def conf():
    config = ConfigParser.ConfigParser()
    config.read('prefs.ini')
    return config


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.binary = '/Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin' # noqa
    firefox_options.add_argument('-foreground')
    firefox_options.set_preference('browser.anchor_color', '#FF0000')
    return firefox_options
