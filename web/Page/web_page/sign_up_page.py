from web.BaseTest.base import *
from selenium.webdriver.chrome.webdriver import WebDriver
from web.locators.web_locator.sign_up_locator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import allure
import pytest


class sign_up_form(Base_home):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.Sign_up = sign_up_page.sign_up
        self.Username = sign_up_page.username
        self.Password = sign_up_page.password
        self.done = sign_up_page.sign_up_done
        self.Close = sign_up_page.close

    @pytest.mark.sanity
    @allure.description('click sign up ')
    def click_sign_up_page(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Sign_up).click()
        sleep(1)

    @pytest.mark.sanity
    @allure.description('insert value to "Username" input')
    def enter_username_page(self, Username):
        field = self.driver.find_element(By.XPATH, self.Username)
        field.clear()
        field.send_keys(Username)
        sleep(1)

    @pytest.mark.sanity
    @allure.description('insert value to "Password" input')
    def enter_password_page(self, Password):
        field = self.driver.find_element(By.XPATH, self.Password)
        field.clear()
        field.send_keys(Password)
        sleep(1)

    @pytest.mark.sanity
    @allure.description('click sign up done')
    def click_done(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.done).click()
        sleep(1)

    @pytest.mark.sanity
    @allure.description('click sign up close')
    def click_Close(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Close).click()
        sleep(1)

    @pytest.mark.sanity
    @allure.description('click sign up close')
    def alat_off(self):
        self.driver.switch_to.alert.accept()