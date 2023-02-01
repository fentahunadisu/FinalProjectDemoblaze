from web.BaseTest.base import *
from selenium.webdriver.chrome.webdriver import WebDriver
from web.locators.web_locator.login_locator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import allure


class login_form(Base_home):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.Login = login_page.login
        self.Username = login_page.username
        self.Password = login_page.password
        self.Done = login_page.done
        self.Close = login_page.close

    def click_login_page(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Login).click()
        sleep(1)

    @allure.step
    @allure.description('insert value to "Username" input')
    def enter_username(self, Username):
        field = self.driver.find_element(By.XPATH, self.Username)
        field.clear()
        field.send_keys(Username)
        sleep(1)

    @allure.step
    @allure.description('insert value to "Password" input')
    def enter_password(self, Password):
        field = self.driver.find_element(By.XPATH, self.Password)
        field.clear()
        field.send_keys(Password)
        sleep(1)

    @allure.step
    @allure.description('click on the login button')
    def click_login(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Done).click()
        sleep(1)

    def alat_off(self):
        self.driver.switch_to.alert.accept()

    @allure.step
    @allure.description('click on the close button')
    def click_close_button(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Close).click()
        sleep(1)