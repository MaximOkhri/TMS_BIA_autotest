import os
from .base_page import BasePage
from .locators import NewClientPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
import json

class NewClientPage(BasePage):

    def create_new_client(self):
        f = open('client_data.json', encoding='utf-8')
        file_content = f.read()
        client_data = json.loads(file_content)

        company_name = self.browser.find_element(*NewClientPageLocators.CLIENT_NAME)
        company_name.send_keys(client_data['name'])
        company_phone = self.browser.find_element(*NewClientPageLocators.COMPANY_PHONE)
        company_phone.click()
        company_phone.send_keys(client_data['company_phone'])
        load_logo = self.browser.find_element(*NewClientPageLocators.LOAD_LOGO)
        
        current_dir = os.path.abspath(os.path.dirname(__file__))  
        logo_path = os.path.join(current_dir, 'img/Logo.jpg')         
        load_logo.send_keys(logo_path)

        contact_name = self.browser.find_element(*NewClientPageLocators.CONTACT_NAME)
        contact_name.send_keys(client_data['contact_name'])
        contact_phone = self.browser.find_element(*NewClientPageLocators.CONTACT_PHONE)
        contact_phone.click()
        contact_phone.send_keys(client_data['contact_phone'])
        contact_email = self.browser.find_element(*NewClientPageLocators.CONTACT_EMAIL)
        contact_email.send_keys(client_data['contact_email'])
        create_new_client_button = self.browser.find_element(*NewClientPageLocators.CREATE_CLIENT_BUTTON)
        create_new_client_button.click()

        assert self.is_element_present(*NewClientPageLocators.CREATE_SUCCESS_MESSAGE), "no success message"
        check_success_message = self.browser.find_element(*NewClientPageLocators.CREATE_SUCCESS_MESSAGE)
        assert check_success_message.text == "Клиент успешно создан!", "success message are different"
    