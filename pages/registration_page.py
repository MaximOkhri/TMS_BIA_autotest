from .base_page import BasePage
from .locators import RegistrationWindowLocators
from selenium.webdriver.chrome.webdriver import WebDriver
import json

class RegistrationPage(BasePage):
    
    def create_new_user(self):
        f = open('user_data.json', encoding='utf-8')
        file_content = f.read()
        user_data = json.loads(file_content)

        first_name = self.browser.find_element(*RegistrationWindowLocators.FIRST_NAME)
        first_name.send_keys(user_data['name'])
        last_name = self.browser.find_element(*RegistrationWindowLocators.LAST_NAME)
        last_name.send_keys(user_data['surname'])
        e_mail = self.browser.find_element(*RegistrationWindowLocators.E_MAIL)
        e_mail.send_keys(user_data['email'])
        user_password = self.browser.find_element(*RegistrationWindowLocators.USER_PASSWORD)
        user_password.send_keys(user_data['user_password'])
        registration_button = self.browser.find_element(*RegistrationWindowLocators.REGISTRATION_BUTTON)
        registration_button.click()
        assert self.is_element_present(*RegistrationWindowLocators.SUCCESS_MESSAGE), "no success message"
        close_success_message_button = self.browser.find_element(*RegistrationWindowLocators.CLOSE_SUCCESS_MESSAGE)
        close_success_message_button.click()