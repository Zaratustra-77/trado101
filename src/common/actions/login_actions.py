from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pa import password, db_name, user_name
from src.utils.mongoScrape import get_code_for_testing
import time



class LoginModule:
    def __init__(self, driver):
        self.my_driver = driver

    def click_login_btn(self):
        # locate and click on register login
        div_element_login_register = WebDriverWait(self.my_driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a')
            )
        )
        div_element_login_register.click()

    def send_phone(self, phone):
        phone_for_testing = phone

        # locate phone field and send keys
        phone_input = (
            WebDriverWait(self.my_driver, 10)
            .until(EC.presence_of_element_located((By.CLASS_NAME, "form-control")))
            .send_keys(phone_for_testing)
        )

    def click_enter(self):
        # click submit to move to enter code
        submit_btn = (
            WebDriverWait(self.my_driver, 10)
            .until(EC.presence_of_element_located((By.CLASS_NAME, "form_submitBtn")))
            .click()
        )
        time.sleep(5)

    def get_code(self, phone_for_testing):
        phone = phone_for_testing
        phone_to_use = f"972{phone}"
        # handle the code aquiring

        code = get_code_for_testing(phone_to_use)

        return code


    def send_login_code(self,code):
        WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal_modal"))
        )

        # Interact with each input element

        input_class = "input_0"
        input_element = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input',
                )
            )
        )
        # Debugging: Check if element is visible and enabled
        input_element.send_keys(code)
    def click_submit(self):
        submit_btn2 = (
            WebDriverWait(self.my_driver, 10)
            .until(EC.presence_of_element_located((By.CLASS_NAME, "form_submitBtn")))
            .click()
        )

