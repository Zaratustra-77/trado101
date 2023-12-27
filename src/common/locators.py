from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pa import password, db_name, user_name
from src.utils.mongoScrape import get_code_for_testing
import time


class Locators:
    def __init__(self, driver):
        self.my_driver = driver

    def login_module_registration_btn(self):
        login_module_registration_btn = WebDriverWait(self.my_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login_titleContainer"))).getText('innerText')
        return login_module_registration_btn