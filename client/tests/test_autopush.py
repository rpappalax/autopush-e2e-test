import pytest
from pages.autopush_test_page import AutopushTestPage 
import time


class TestAutopush:

    @pytest.mark.nondestructive
    #def test_push_notification(self, selenium, base_url):
    def test_push_notification(self, base_url, selenium):
        autopush_page = AutopushTestPage(base_url, selenium).open()
        autopush_page.wait_for_page_to_load()

        assert autopush_page.is_reg_btn_present
        time.sleep(3)
        autopush_page.reg_btn_click()
        time.sleep(5)

        assert autopush_page.is_subscribe_btn_present
        time.sleep(3)
        autopush_page.subscribe_btn_click()

        assert autopush_page.is_repeat_txt_present
        time.sleep(3)
        autopush_page.set_repeat_text()
        assert autopush_page.is_doXhr_btn_present
        time.sleep(3)
        autopush_page.doXhr_btn_click()
