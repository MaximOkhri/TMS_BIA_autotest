from .base_page import BasePage
from .locators import LoginWindowLocators
from selenium.webdriver.chrome.webdriver import WebDriver
import json

class LoginPage(BasePage):
    
    def login_user(self):
        
        f = open('user_data.json', encoding='utf-8')
        file_content = f.read()
        user_data = json.loads(file_content)

        e_mail = self.browser.find_element(*LoginWindowLocators.E_MAIL)
        e_mail.send_keys(user_data['email'])
        user_password = self.browser.find_element(*LoginWindowLocators.USER_PASSWORD)
        user_password.send_keys(user_data['user_password'])
        login_button = self.browser.find_element(*LoginWindowLocators.LOGIN_BUTTON)
        login_button.click()
