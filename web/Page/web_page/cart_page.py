import allure

from web.BaseTest.base import *
from selenium.webdriver.chrome.webdriver import WebDriver
from web.locators.web_locator.cart_locator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class cart_page(Base_home):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.cart = Cart_link.Cart
        self.place_order = Cart_link.Place_order
        self.name = Cart_link.Name
        self.country = Cart_link.Country
        self.city = Cart_link.City
        self.credit_card = Cart_link.Credit_card
        self.month = Cart_link.Month
        self.year = Cart_link.Year
        self.purchas = Cart_link.Purchas
        self.close = Cart_link.Close

    def click_cart(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.cart).click()
        sleep(1)

    def click_place_order(self):
        self.driver.find_element(By.XPATH, self.place_order).click()
        sleep(1)

    @allure.step
    @allure.description('insert value to "name" input')
    def enter_name(self, name):
        field = self.driver.find_element(By.XPATH, self.name)
        field.clear()
        field.send_keys(name)
        sleep(1)

    @allure.step
    @allure.description('insert value to "country" input')
    def enter_country(self, country):
        field = self.driver.find_element(By.XPATH, self.country)
        field.clear()
        field.send_keys(country)
        sleep(1)

    @allure.step
    @allure.description('insert value to "city" input')
    def enter_city(self, city):
        field = self.driver.find_element(By.XPATH, self.city)
        field.clear()
        field.send_keys(city)
        sleep(1)

    @allure.step
    @allure.description('insert value to "credit_card" input')
    def enter_credit_card(self, credit_card):
        field = self.driver.find_element(By.XPATH, self.credit_card)
        field.clear()
        field.send_keys(credit_card)
        sleep(1)

    @allure.step
    @allure.description('insert value to "month" input')
    def enter_month(self, month):
        field = self.driver.find_element(By.XPATH, self.month)
        field.clear()
        field.send_keys(month)
        sleep(1)

    @allure.step
    @allure.description('insert value to "year" input')
    def enter_year(self, year):
        field = self.driver.find_element(By.XPATH, self.year)
        field.clear()
        field.send_keys(year)
        sleep(1)

    def click_purchas(self):
        self.driver.find_element(By.XPATH, self.purchas).click()
        sleep(1)

    def click_close(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.close).click()
        sleep(2)