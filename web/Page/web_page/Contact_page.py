from lib2to3.pgen2 import driver

import allure

from web.BaseTest.base import *
from selenium.webdriver.chrome.webdriver import WebDriver
from web.locators.web_locator.contact_locator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class contact_run(Base_home):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.contact_link= Contact_link.Contact
        # self.ContactText = Contact_link.ContactEmail
        self.EmailEnter = Contact_link.Email
        self.ContactNameText = Contact_link.ContactName
        self.NameEnter = Contact_link.Name
        self.MessageText = Contact_link.Message
        self.MessageEnter = Contact_link.EnterMessage
        self.MessageSend = Contact_link.SendMessage
        self.Out = Contact_link.Close

    def click_contact_page(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.contact_link).click()
        sleep(5)

    @allure.step
    @allure.description('clicking on signup button - should navigate to signup page')
    def click_contact_page(self):
        self.driver.find_element(By.XPATH, self.contact_link).click()

    @allure.step
    @allure.description('insert value to "username" input')
    def enter_Username(self, EmailEnter):
        field = self.driver.find_element(By.XPATH, self.EmailEnter)
        field.clear()
        field.send_keys(EmailEnter)
        sleep(3)

    @allure.step
    @allure.description('insert value to "password"')
    def enter_passwored(self, NameEnter):
        field = self.driver.find_element(By.XPATH, self.NameEnter)
        field.clear()
        field.send_keys(NameEnter)
        sleep(3)

    @allure.step
    @allure.description('insert you want message')
    def Click_massage(self, MessageEnter):
        field = self.driver.find_element(By.XPATH, self.MessageEnter)
        field.clear()
        field.send_keys(MessageEnter)
        sleep(3)


    @allure.step
    @allure.description('clicking on signup button')
    def send_button_click(self):
        self.driver.find_element(By.XPATH, self.MessageSend).click()

    def alat_off(self):
        self.driver.switch_to.alert.accept()