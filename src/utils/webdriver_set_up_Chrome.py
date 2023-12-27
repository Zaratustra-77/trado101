import time
import unittest
from src.utils.imports import *
from src.common.actions.login_actions import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class WebDriverSetupChrome(unittest.TestCase):

    def setUp(self) -> None:

        try:
            chrome_options = Options()
            chrome_options.add_argument("--ignore-ssl-errors=yes")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("disable_extensions")
            chrome_options.headless = False
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install(), options=chrome_options)
            )

            self.driver.set_page_load_timeout(30)
            self.driver.get("http://qa.trado.ai/")
            time.sleep(5)



        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()
