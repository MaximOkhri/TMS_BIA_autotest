from .base_page import BasePage
from .locators import ClientPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
import json

class ClientPage(BasePage):

    def open_new_client_page(self):
        new_client_page = self.browser.find_element(*ClientPageLocators.NEW_CLIENT_BUTTON)
        new_client_page.click()

    def open_client_card(self):
        client_link = self.browser.find_element(*ClientPageLocators.CLIENT_LINK)
        client_link.click()

    def check_client(self):
        f = open('client_data.json', encoding='utf-8')
        file_content = f.read()
        client_data = json.loads(file_content)

        client_name = self.browser.find_element(*ClientPageLocators.CLIENT_NAME)
        client_name_value = client_name.get_attribute("value")
        assert client_name_value == client_data['name'], "client name are different"

        company_phone = self.browser.find_element(*ClientPageLocators.COMPANY_PHONE)
        company_phone_value = company_phone.get_attribute("value")
        company_phone_value = company_phone_value.replace(' ', '')
        assert company_phone_value == "+7" + str(client_data['company_phone']), "company phone are different"

        contact_name = self.browser.find_element(*ClientPageLocators.CONTACT_NAME)
        contact_name_value = contact_name.get_attribute("value")
        assert contact_name_value == client_data['contact_name'], "contact name are different"

        contact_phone = self.browser.find_element(*ClientPageLocators.CONTACT_PHONE)
        contact_phone_value = contact_phone.get_attribute("value")
        contact_phone_value = contact_phone_value.replace(' ', '')
        assert contact_phone_value == "+7" + str(client_data['contact_phone']), "contact phone are different"

        contact_email = self.browser.find_element(*ClientPageLocators.CONTACT_EMAIL)
        contact_email_value = contact_email.get_attribute("value")
        assert contact_email_value == client_data['contact_email'], "contact email are different"

        assert self.is_element_present(*ClientPageLocators.LOGO_ON_PAGE), "no picture on the page"
    
    def delete_client(self):
        delete_client_button = self.browser.find_element(*ClientPageLocators.DELETE_CLIENT)
        delete_client_button.click()
        
        assert self.is_element_present(*ClientPageLocators.DELETE_SUCCESS_MESSAGE), "no success message"
        check_success_message = self.browser.find_element(*ClientPageLocators.DELETE_SUCCESS_MESSAGE)
        assert check_success_message.text == "Клиент успешно удален!", "success message are different"
        empty_list = self.browser.find_element(*ClientPageLocators.EMPTY_LIST)
        assert empty_list.text == "Список клиентов пуст", "list is not empty"
        