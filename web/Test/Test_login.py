from web.Page.web_page.login_page import login_form
from web.BaseTest.base import Base_home
import pytest
import allure


class Test_login_(Base_home):

    def test_login_correctly(self):
        driver = self.driver
        loginPage = login_form(driver)
        loginPage.click_login_page()

    def test_username(self):
        driver = self.driver
        loginPage = login_form(driver)
        loginPage.click_login_page()
        loginPage.enter_username("fentahun")
        loginPage.enter_password("7654321")
        loginPage.click_login()
        loginPage.alat_off()

    def test_close(self):
        driver = self.driver
        loginPage = login_form(driver)
        loginPage.click_login_page()
        loginPage.click_close_button()