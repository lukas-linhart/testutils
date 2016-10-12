class WebDriverReanimator(object):

    def __init__(self, wd_func=None, wd_kwargs={}):
        self.webdriver = wd_func(**wd_kwargs)

