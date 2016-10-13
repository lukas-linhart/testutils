from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


default_wd_func = webdriver.Remote
default_wd_kwargs = {
    'command_executor': 'http://127.0.0.1:4444/wd/hub',
    'desired_capabilities': DesiredCapabilities.CHROME
}


class WebDriverReanimator(object):

    def __init__(self, wd_func=default_wd_func, wd_kwargs=default_wd_kwargs):
        self.webdriver = wd_func(**wd_kwargs)


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_value, exc_tb):
        pass

