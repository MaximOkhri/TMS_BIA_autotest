from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.client_page import ClientPage
from .pages.new_client_page import NewClientPage
from .pages.choose_role_page import ChooseRolePage
from .pages.registration_page import RegistrationPage
from .pages.my_profile_page import MyProfilePage
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest

class TestRegistrationFromMainPage():

    def test_open_registration_window_and_create_new_user(self, browser: WebDriver):
        link = "https://tms.biacorp.ru/"
        page = MainPage(browser, link)
        page.open()
        page.open_registration_window()
        registration_page = RegistrationPage(browser, browser.current_url)
        registration_page.create_new_user()

class TestRClientPage():
        
    def test_create_new_client(self, browser: WebDriver):
        link = "https://tms.biacorp.ru/"
        page = MainPage(browser, link)
        page.open()
        page.open_login_window()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user()
        choose_role_page = ChooseRolePage(browser, browser.current_url)
        choose_role_page.choose_role()
        my_profile_page = MyProfilePage(browser, browser.current_url)
        my_profile_page.open_client_page()
        client_page = ClientPage(browser, browser.current_url)
        client_page.open_new_client_page()
        new_client_page = NewClientPage(browser, browser.current_url)
        new_client_page.create_new_client()

    def test_check_client(self, browser: WebDriver):
        link = "https://tms.biacorp.ru/"
        page = MainPage(browser, link)
        page.open()
        page.open_login_window()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user()
        choose_role_page = ChooseRolePage(browser, browser.current_url)
        choose_role_page.choose_role()
        my_profile_page = MyProfilePage(browser, browser.current_url)
        my_profile_page.open_client_page()
        client_page = ClientPage(browser, browser.current_url)
        client_page.open_client_card()
        client_page = ClientPage(browser, browser.current_url)
        client_page.check_client()
        
    def test_delete_client(self, browser: WebDriver):
        link = "https://tms.biacorp.ru/"
        page = MainPage(browser, link)
        page.open()
        page.open_login_window()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user()
        choose_role_page = ChooseRolePage(browser, browser.current_url)
        choose_role_page.choose_role()
        my_profile_page = MyProfilePage(browser, browser.current_url)
        my_profile_page.open_client_page()
        client_page = ClientPage(browser, browser.current_url)
        client_page.open_client_card()
        client_page.delete_client()