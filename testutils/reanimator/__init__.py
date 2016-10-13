from .default_webdriver import default_wd_func, default_wd_kwargs


class WebDriverReanimator(object):

    def __init__(self, wd_func=default_wd_func, wd_kwargs=default_wd_kwargs):
        self.webdriver = wd_func(**wd_kwargs)


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_value, exc_tb):
        pass

