from .base_page import BasePage
from .locators import MyProfileLocators
from selenium.webdriver.chrome.webdriver import WebDriver

class MyProfilePage(BasePage):

    def open_client_page(self):
        client_page_button = self.browser.find_element(*MyProfileLocators.CLIENT_BUTTON)
        client_page_button.click()

    