from selenium.webdriver.firefox.options import Options
from selenium import webdriver


class SeleniumDriver:

    def __init__(self, drive_name="firefox", headless=True, implicitly_wait=20):
        option = Options()
        option.headless = headless
        self._implicitly_wait = implicitly_wait
        if drive_name == "firefox":
            self._driver = webdriver.Firefox(options=option)
        else:
            self._driver = webdriver.Chrome(options=option)

    def obter_driver(self, url):
        print(f"Carregando Driver para URL -> {url}")
        self._driver.get(url)
        self._driver.implicitly_wait(self._implicitly_wait)  # in seconds
        return self._driver
