from selenium.webdriver.common.by import By

class BasePageLocators():
    REGISTRATION_LINK = (By.CSS_SELECTOR, "button.css-12h2ojt")
    LOGIN_LINK = (By.CSS_SELECTOR, "button.css-vgoep3")

class RegistrationWindowLocators():
    FIRST_NAME = (By.NAME, "name")
    LAST_NAME = (By.NAME, "surname")
    E_MAIL = (By.NAME, "email")
    USER_PASSWORD = (By.NAME, "password")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.css-yhxv9x")
    SUCCESS_MESSAGE = (By.ID, "toast-1-description")
    CLOSE_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "button.css-1pq15d")

class LoginWindowLocators():
    E_MAIL = (By.NAME, "email")
    USER_PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.css-yhxv9x")

class ChooseRoleLocators():
    CHOOSE_ROLE = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/a[2]")

class MyProfileLocators():
    CLIENT_BUTTON = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[5]/button")

class ClientPageLocators():
    NEW_CLIENT_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/a")
    CLIENT_LINK = (By.CSS_SELECTOR, "a.css-1r73ipu")
    CLIENT_NAME = (By.CSS_SELECTOR, "input[name=name]")
    COMPANY_PHONE = (By.NAME, "company_phone")
    LOGO_ON_PAGE = (By.CSS_SELECTOR, "img.css-3ej1yo")
    CONTACT_NAME = (By.NAME, "contact_name")
    CONTACT_PHONE = (By.NAME, "contact_phone")
    CONTACT_EMAIL = (By.NAME, "contact_email")
    DELETE_CLIENT = (By.CSS_SELECTOR, "button.css-1w1e55e")
    DELETE_SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div[5]/div/div/div/div/div")
    EMPTY_LIST = (By.CSS_SELECTOR, "div.css-qt2l4d")

class NewClientPageLocators():
    CLIENT_NAME = (By.NAME, "name")
    COMPANY_PHONE = (By.NAME, "company_phone")
    LOAD_LOGO = (By.CSS_SELECTOR, "input[type=file]")
    CONTACT_NAME = (By.NAME, "contact_name")
    CONTACT_PHONE = (By.NAME, "contact_phone")
    CONTACT_EMAIL = (By.NAME, "contact_email")
    CREATE_CLIENT_BUTTON = (By.CSS_SELECTOR, "button.css-yh0kq8")
    CREATE_SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div[5]/div/div/div/div/div")