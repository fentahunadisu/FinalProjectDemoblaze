from lib2to3.pgen2 import driver

import allure
import pytest

from web.BaseTest.base import *
from web.locators.web_locator.home_locator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class TestHome(Base_home):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.Phone_Home = home_locator.homePage
        self.Phone_Type = home_locator.Phone
        self.cart = home_locator.Cart
        self.S6_SamsungGalaxy = home_locator.SamsungGalaxyS6
        self.Cart = home_locator.AddToCart
        self.Logo = home_locator.Img
        self.Product_Store = home_locator.Brand
        self.Scroll = home_locator.carouselActive
        self.ScrollRight = home_locator.NextRight
        self.ScrollLeft = home_locator.NextLeft

        self.NokiaPhone = home_locator.Nokia
        self.TextNokia = home_locator.NokiaText
        self.PhonePrice = home_locator.Price

        self.Nexus_6Phone = home_locator.Nexus_6
        self.Nexus_6text = home_locator.NokiaText
        self.Nexus_6price = home_locator.NexusPrice

        self.samsungGalaxy_S7 = home_locator.SamsungGalaxy_S7
        self.SamsungGalaxy_S7text = home_locator.SamsungGalaxy_S7Text
        self.samsungGalaxy_S7price = home_locator.SamsungGalaxy_S7Price

        self.iphone_6_32gb = home_locator.Iphone_6_32gb
        self.iphone_6_32gb_text = home_locator.Iphone_6_32gbText
        self.iphone_6_32gb_price = home_locator.Iphone_6_32gbPrice

        self.sonyXperia_z5 = home_locator.SonyXperia_z5
        self.sonyXperia_z5text = home_locator.SonyXperia_z5Text
        self.sonyXperia_z5price = home_locator.SonyXperia_z5Price

        self.hTCOneM9 = home_locator.HTCOneM9
        self.hTCOneM9text = home_locator.HTCOneM9Text
        self.hTCOneM9price = home_locator.HTCOneM9Price

        self.about_us__ = home_locator.About_us__
        self.get_in_touch = home_locator.Get_in_touch
        self.address = home_locator.Address
        self.phoneAbout = home_locator.PhoneAbout
        self.emailAbout = home_locator.EmailAbout
        self.next = home_locator.Next
        self.previous = home_locator.Previous

        self.sonyLapI5 = home_locator.SonyVaioI5
        self.SonyAdd = home_locator.sonAdd
        self.sonyTextI5 = home_locator.lapText
        self.sonyI5LapP = home_locator.lapPrice

        self.sonLapI7 = home_locator.sonyvaioI7
        self.sonyLapI7Add = home_locator.sonAddI7
        self.sonyTextI7 = home_locator.I7lapText
        self.SonyI7LapPrice = home_locator.lapPriceI7

        self.cart = home_locator.Cart
        self.place_order = home_locator.Place_order
        self.name = home_locator.Name
        self.country = home_locator.Country
        self.city = home_locator.City
        self.credit_card = home_locator.Credit_card
        self.month = home_locator.Month
        self.year = home_locator.Year
        self.purchas = home_locator.Purchas



    def click_home_phone(self):
        self.driver.find_element(By.XPATH, self.Phone_Home).click()

    def click_phone(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Phone_Type).click()
        sleep(2)

    def click_cart_home(self):
        self.driver.find_element(By.XPATH,self.cart).click()

    def samsung_galaxy(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.S6_SamsungGalaxy).click()
        sleep(2)

    def click_cart(self):
        self.driver.find_element(By.XPATH, self.Cart).click()
        sleep(20)

    def alat_off(self):
        self.driver.switch_to.alert.accept()

    def click_logo(self):
        self.driver.find_element(By.XPATH, self.Logo).click()
        sleep(2)

    def click_product_store(self):
        self.driver.find_element(By.XPATH, self.Product_Store).click()
        sleep(2)

    def click_scroll(self):
        self.driver.find_element(By.XPATH, self.Scroll).click()
        sleep(2)

    def click_scroll_right(self):
        self.driver.find_element(By.XPATH, self.ScrollRight).click()
        sleep(2)

    def click_scroll_left(self):
        self.driver.find_element(By.XPATH, self.ScrollLeft).click()
        sleep(2)

    def Nokia_lumia_1520(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.NokiaPhone).click()
        sleep(2)

    def mach_text_nokia(self):
        product_name = self.driver.find_element(By.XPATH, self.TextNokia).text
        assert product_name == 'Nokia lumia 1520'
        sleep(5)

    def mach_phone_price(self):
        product_name = self.driver.find_element(By.XPATH, self.PhonePrice).text
        assert product_name == '$820 *includes tax'
        sleep(5)

    def click_Nexus_6Phone(self):
        self.driver.find_element(By.XPATH, self.Nexus_6Phone).click()
        sleep(5)

    def mach_nexus_text(self):
        product_name = self.driver.find_element(By.XPATH, self.Nexus_6text).text
        assert product_name == 'Nexus 6'
        sleep(5)

    def mach_nexus_price(self):
        product_name = self.driver.find_element(By.XPATH, self.Nexus_6price).text
        assert product_name == '$650 *includes tax'
        sleep(5)

    def click_samsungGalaxy_S7(self):
        self.driver.find_element(By.XPATH, self.samsungGalaxy_S7).click()
        sleep(5)

    def mach_samsung7_text(self):
        product_name = self.driver.find_element(By.XPATH, self.SamsungGalaxy_S7text).text
        assert product_name == 'Samsung galaxy s7'
        sleep(5)

    def mach_samsung7_price(self):
        product_name = self.driver.find_element(By.XPATH, self.samsungGalaxy_S7price).text
        assert product_name == '$800 *includes tax'
        sleep(5)

    def click_iphone_6_32gb(self):
        self.driver.find_element(By.XPATH, self.iphone_6_32gb).click()
        sleep(5)

    def mach_iphone_text(self):
        product_name = self.driver.find_element(By.XPATH, self.iphone_6_32gb_text).text
        assert product_name == 'Iphone 6 32gb'
        sleep(5)

    def mach_iphone_price(self):
        product_name = self.driver.find_element(By.XPATH, self.iphone_6_32gb_price).text
        assert product_name == '$790 *includes tax'
        sleep(5)

    def click_sonyXperia_z5(self):
        self.driver.find_element(By.XPATH, self.sonyXperia_z5).click()
        sleep(5)

    def mach_sonyXperia_text(self):
        product_name = self.driver.find_element(By.XPATH, self.sonyXperia_z5text).text
        assert product_name == 'Sony xperia z5'
        sleep(5)

    def mach_sonyXperia_price(self):
        product_name = self.driver.find_element(By.XPATH, self.sonyXperia_z5price).text
        assert product_name == '$320 *includes tax'
        sleep(5)

    def click_htc(self):
        self.driver.find_element(By.XPATH, self.hTCOneM9).click()
        sleep(5)

    def mach_htc_text(self):
        product_name = self.driver.find_element(By.XPATH, self.hTCOneM9text).text
        assert product_name == 'HTC One M9HTC One M9'
        sleep(5)

    def mach_htc_price(self):
        product_name = self.driver.find_element(By.XPATH, self.hTCOneM9price).text
        assert product_name == '$700 *includes tax'
        sleep(5)

    def click_next_page(self):
        self.driver.find_element(By.XPATH, self.next).click()
        sleep(5)

    def click_previous_page(self):
        self.driver.find_element(By.XPATH, self.previous).click()
        sleep(5)

    def scroll_page_down(self):
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)

    def click_lapI5_page(self):
        self.driver.find_element(By.XPATH, self.sonyLapI5).click()
        sleep(5)

    def click_lapI5_add(self):
        self.driver.find_element(By.XPATH, self.SonyAdd).click()
        sleep(5)

    def click_lapI5_text(self):
        product_name = self.driver.find_element(By.XPATH, self.sonyTextI5).text
        assert product_name == 'Sony vaio i5'
        sleep(5)

    def click_lapI5_price(self):
        product_name = self.driver.find_element(By.XPATH, self.sonyI5LapP).text
        assert product_name == '$790 *includes tax'
        sleep(5)

    def click_lapI7_page(self):
        self.driver.find_element(By.XPATH, self.sonLapI7).click()
        sleep(5)

    def click_lapI7_add(self):
        self.driver.find_element(By.XPATH, self.sonyLapI7Add).click()
        sleep(5)

    def click_lapI7_text(self):
        product_name = self.driver.find_element(By.XPATH, self.sonyTextI7).text
        assert product_name == 'Sony vaio i7'
        sleep(5)

    def click_lapI7_price(self):
        product_name = self.driver.find_element(By.XPATH, self.SonyI7LapPrice).text
        assert product_name == '$790 *includes tax'
        sleep(5)

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
