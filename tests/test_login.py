import pytest
import allure
from src.utils.webdriver_set_up_Chrome import WebDriverSetupChrome
from src.utils.Webdriver_set_up_Firefox import WebDriverSetupFirefox
from src.common.actions.login_actions import LoginModule
from src.common.locators import Locators
from src.utils.webdriver_set_up_Chrome import WebDriverSetupChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestValidLoginChrome(WebDriverSetupChrome):

    @pytest.mark.sanity
    @allure.title('est_1_valid_login_Chrome')
    @allure.severity('High')
    def test_1_valid_login_Chrome(self):
        self.login_module_actions = LoginModule(self.driver)
        self.login_module_actions.click_login_btn()
        self.login_module_actions.send_phone('00123456')
        self.login_module_actions.click_enter()
        code = self.login_module_actions.get_code('00123456')
        self.login_module_actions.send_login_code(code)
        self.login_module_actions.click_submit()
        text = "שלום    "
        hello = div_element_login_register = (
            WebDriverWait(self.driver, 10)
                .until(EC.element_to_be_clickable((By.CLASS_NAME, "header_userAreaLink")))
                .get_attribute("text")
        )
        print(hello)
        assert str(hello) == text

class TestValidLoginFirefox(WebDriverSetupFirefox):

    def test_1_valid_login_Firefox(self):

        self.login_module_actions = LoginModule(self.driver)
        self.login_module_actions.click_login_btn()
        self.login_module_actions.send_phone('00123456')
        self.login_module_actions.click_enter()
        code = self.login_module_actions.get_code('00123456')
        self.login_module_actions.send_login_code(code)
        self.login_module_actions.click_submit()

        text = "שלום    "
        hello = div_element_login_register = (
            WebDriverWait(self.driver, 10)
                .until(EC.element_to_be_clickable((By.CLASS_NAME, "header_userAreaLink")))
                .get_attribute("text")
        )
        print(hello)
        assert str(hello) == text
# # header_userAreaLink
