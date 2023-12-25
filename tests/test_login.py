from src.utils.webdriver_set_up import WebDriverSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestValidLogin(WebDriverSetup):

    def test_1_valid_login(self):
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
