from pypom import Page
from pages.base import Base
from selenium.webdriver.common.by import By


class AutopushTestPage(Base):

    URL_TEMPLATE = 'http://localhost:8201'
    REPEAT_TEXT = "7"

    _push_api_header_locator = (By.ID, 'doXhr_btn')
    _reg_btn_locator = (By.ID, 'reg_btn')

    _subscribe_btn_locator = (By.ID, 'subscribe_btn')
    _repeat_txt_locator = (By.ID, 'repeat_txt')
    _reg_btn_locator = (By.ID, 'reg_btn')


    @property
    def is_reg_btn_present(self):
        return self.is_element_displayed(*self._reg_btn_locator)


    #@property
    def reg_btn_click(self):
        self.find_element(*self._reg_btn_locator).click()


    @property
    def is_subscribe_btn_present(self):
        return self.is_element_displayed(*self._subscribe_btn_locator)


    @property
    def subscribe_btn_click(self):
        self.find_element(*self._subscribe_btn_locator).click()


    @property
    def is_repeat_txt_present(self):
        return self.is_element_displayed(*self._repeat_txt_locator)

    @property
    def set_repeat_text(self):
        return self.find_element(*self._repeat_txt_locator).send_keys(REPEAT_TEXT)


    @property
    def is_doXhr_btn_present(self):
        return self.is_element_displayed(*self._doXhr_btn_locator)


    @property
    def doXhr_btn_click(self):
        self.find_element(*self._doXhr_btn_locator).click()

