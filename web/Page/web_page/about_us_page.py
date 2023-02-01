from web.BaseTest.base import *
from selenium.webdriver.chrome.webdriver import WebDriver
from web.locators.web_locator.about_us_locator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import allure



class about_us_Page(Base_home):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.About_us = about_us_home_page.about_us
        self.Play = about_us_home_page.play
        self.Close = about_us_home_page.close
        self.x = about_us_home_page.X
        self.Sound = about_us_home_page.sound
        self.Vlue = about_us_home_page.vlue
        self.Zoom = about_us_home_page.zoom

    def click_about_us(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.About_us).click()
        sleep(1)

    def click_play_button(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Play).click()
        sleep(5)

    def click_x_exeit(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.x).click()
        sleep(1)

    def click_sound_button(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Sound).click()
        sleep(1)

    def click_vlue(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Vlue).click()
        sleep(1)

    def click_zoom(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Zoom).click()
        sleep(1)

    def click_close_button(self):
        super().__init__()
        self.driver.find_element(By.XPATH, self.Close).click()
        sleep(1)
