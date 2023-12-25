

from src.utils.webdriver_set_up import WebDriverSetup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from pa import password, db_name, user_name
from src.utils.mongoScrape import create_mongo_db,create_mongo_connection,get_loginCode

class TestOH(WebDriverSetup):
    def test_1_valid_login(self):
        # locate and click on register login
        div_element_login_register = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a')
            )
        )
        div_element_login_register.click()
        phone = "00123456"

        # locate phone field and send keys
        phone_input = (
            WebDriverWait(self.driver, 10)
            .until(EC.presence_of_element_located((By.CLASS_NAME, "form-control")))
            .send_keys(phone)
        )

        # click submit to move to enter code
        submit_btn = (
            WebDriverWait(self.driver, 10)
            .until(EC.presence_of_element_located((By.CLASS_NAME, "form_submitBtn")))
            .click()
        )

        time.sleep(5)
        phon = "00123456"
        phone_to_use = f"972{phone}"
        # handle the code aquiring
        client = create_mongo_connection(user_name, password, db_name)
        db = create_mongo_db(client, db_name)
        code = get_loginCode(db, "97200123456")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal_modal"))
        )

        # Interact with each input element

        input_class = "input_0"
        input_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input',
                )
            )
        )
        # Debugging: Check if element is visible and enabled
        input_element.send_keys(code)

        submit_btn2 = (
            WebDriverWait(self.driver, 10)
            .until(EC.presence_of_element_located((By.CLASS_NAME, "form_submitBtn")))
            .click()
        )
        # find שלום
        text = "שלום    "
        hello = div_element_login_register = (
            WebDriverWait(self.driver, 10)
            .until(EC.element_to_be_clickable((By.CLASS_NAME, "header_userAreaLink")))
            .get_attribute("text")
        )
        print(hello)
        assert str(hello) == text


# header_userAreaLink
