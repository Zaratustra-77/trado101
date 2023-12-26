import time
import unittest
from src.utils.imports import *
from src.common.actions.login_actions import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.options import Options


class WebDriverSetup(unittest.TestCase):

    @classmethod
    def set_browser(cls, browser: str):
        """
        setup class to come before the regular setup
        :param browser: str
        :return:
        """
        cls.browser_name = browser

    def setUp(self) -> None:
        try:
            if self.browser_name == 'chrome':
                chrome_options = Options()
                chrome_options.add_argument("--ignore-ssl-errors=yes")
                chrome_options.add_argument("--start-maximized")
                chrome_options.add_argument("--ignore-certificate-errors")
                chrome_options.add_argument("disable_extensions")
                chrome_options.headless = False
                self.driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install(),options=chrome_options)
                )

                self.driver.set_page_load_timeout(30)
                self.driver.get("http://qa.trado.ai/")
                time.sleep(5)
            elif self.browser_name == 'firefox':

                # Setup for Firefox
                options = FirefoxOptions()
                options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
                options.headless = False
                self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install(), options=options))


                pass
            # Add more browsers if needed

            self.driver.set_page_load_timeout(30)
            self.driver.get("http://qa.trado.ai/")
            time.sleep(5)

        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()

