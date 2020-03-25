from selenium.webdriver.firefox.options import Options
from selenium import webdriver

class SeleniumDriver:

    def __init__(self, driveName="firefox", headless=True,implicitly_wait=20):
        option = Options()
        option.headless = headless
        self._implicitly_wait=implicitly_wait
        if(driveName == "firefox"):
            self._driver = webdriver.Firefox(options=option)
        else:
            self._driver = webdriver.Firefox(options=option)

    def obter_driver(self, url):
        self._driver.get(url)
        self._driver.implicitly_wait(self._implicitly_wait)  # in seconds
        return self._driver
