import time
import unittest
from src.utils.imports import *
from src.common.actions.login_actions import *
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.options import Options




class WebDriverSetupFirefox(unittest.TestCase):
    def setUp(self) -> None:
        try:
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
