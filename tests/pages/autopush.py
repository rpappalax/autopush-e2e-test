from pypom import Page
from selenium.webdriver.common.by import By


class AutopushTestPage(Page):

    URL_TEMPLATE = 'http://localhost:8201'

    _dnt_signal_locator = (By.ID, 'dnt-on')
    _first_party_locator = (By.ID, 'whitelisted-loaded')
    _third_party_locator = (By.ID, 'blacklisted-blocked')

    @property
    def third_party_loads_correctly(self):
        return self.is_element_displayed(*self._third_party_locator)

    @property
    def first_party_loads_correctly(self):
        return self.is_element_displayed(*self._first_party_locator)

    @property
    def dnt_signal_correctly_sent(self):
        return self.is_element_displayed(*self._dnt_signal_locator)
