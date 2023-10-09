from .base_page import BasePage
from .locators import ChooseRoleLocators
from selenium.webdriver.chrome.webdriver import WebDriver

class ChooseRolePage(BasePage):

    def choose_role(self):
        TFL_button = self.browser.find_element(*ChooseRoleLocators.CHOOSE_ROLE)
        TFL_button.click()