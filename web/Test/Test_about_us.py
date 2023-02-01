from web.Page.web_page.about_us_page import *
from web.BaseTest.base import Base_home
import pytest
import allure


class Test_about_us(Base_home):

    @allure.description
    def test_about_us_page(self):
        driver = self.driver
        about = about_us_Page(driver)
        about.click_about_us()
        about.click_play_button()
        # about.click_zoom()
        # about.click_vlue()
        # about.click_sound_button()
        # about.click_x_exeit()

    def test_close_button(self):
        driver = self.driver
        about = about_us_Page(driver)
        about.click_about_us()
        about.click_play_button()
        about.click_close_button()