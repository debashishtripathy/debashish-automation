import pytest
from selenium.webdriver import Firefox,Ie,Chrome


def get_driver_instance():

    type = pytest.config.option.type
    env = pytest.config.option.env

    # type = 'Firefox'

    if env == 'local':
        if type.lower() == 'firefox':
            browser=Firefox()
        elif type.lower() == 'chrome':
            browser = Chrome('./browser-server/chromedriver.exe')

        elif type.lower()=='ie':
            browser = Ie('./browser-server/IEDriverServer.exe')

    elif env=='remote':
        print('Running on remote env')

    browser.maximize_window()
    browser.implicitly_wait(30)
    browser.get("https://qa.etimsportal.com/etims/login.jsp")
    return browser
