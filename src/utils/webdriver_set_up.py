import time
import unittest

from src.utils.imports import *
from src.common.actions.login_actions import *

class WebDriverSetup(unittest.TestCase):
    def setUp(self) -> None:
        try:
            # setUp the driver

            # options = webdriver.ChromeOptions()

            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            chrome_options.add_argument("--ignore-ssl-errors=yes")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("disable_extensions")
            chrome_options.headless = False
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )
            self.login_module_actions = LoginModule(self.driver)
            self.driver.set_page_load_timeout(30)
            self.driver.get("http://qa.trado.ai/")
            time.sleep(5)

        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
