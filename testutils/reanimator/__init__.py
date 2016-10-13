import logging
from .default_webdriver import default_wd_func, default_wd_kwargs


class WebDriverReanimator(object):

    def __init__(self, wd_func=default_wd_func, wd_kwargs=default_wd_kwargs,
            filename='session_id.txt'):
        self.webdriver = wd_func(**wd_kwargs)
        logging.debug('new session_id: {}'.format(self.webdriver.session_id))
        self.filename = filename


    def __enter__(self):
        session_id = self._load_session_id(self.filename)
        return self


    def __exit__(self, exc_type, exc_value, exc_tb):
        self._save_session_id(self.filename, self.webdriver.session_id)


    def _load_session_id(self, filename):
        try:
            with open(filename) as f:
                session_id = f.read()
        except IOError:
            session_id = None
        logging.debug('loaded session_id: {}'.format(session_id))
        return session_id


    def _save_session_id(self, filename, session_id):
        with open(filename, 'w') as f:
            f.write(session_id)
        logging.debug('saved session_id: {}'.format(self.webdriver.session_id))

