from pypom import Page


class Base(Page):


    def __init__(self, base_url, selenium, **kwargs):
        """ Override Page's init method to set a higher timeout. """
        super(Base, self).__init__(
            selenium, base_url, timeout=30, **kwargs)
