from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser: WebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def open_registration_window(self):
        registration_window_button = self.browser.find_element(*BasePageLocators.REGISTRATION_LINK)
        registration_window_button.click()

    def open_login_window(self):
        login_window_button = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_window_button.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True