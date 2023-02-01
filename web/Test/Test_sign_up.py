from web.Page.web_page.sign_up_page import sign_up_form
from web.BaseTest.base import Base_home


class Test_sign_up(Base_home):

    def test_sign_up_home(self):
        driver = self.driver
        sign_up = sign_up_form(driver)
        sign_up.click_sign_up_page()

    def test_username_sign_up_correctly(self):
        driver = self.driver
        sign_up = sign_up_form(driver)
        sign_up.click_sign_up_page()
        sign_up.enter_username_page("fentahun")
        sign_up.enter_password_page("23456")
        sign_up.click_done()
        sign_up.alat_off()

    def test_username_sign_up_incorrectly(self):
        driver = self.driver
        sign_up = sign_up_form(driver)
        sign_up.click_sign_up_page()
        sign_up.enter_username_page("adisu")
        sign_up.enter_password_page("54321")
        sign_up.click_done()
        sign_up.alat_off()

    def test_close_sign_up(self):
        driver = self.driver
        sign_up = sign_up_form(driver)
        sign_up.click_sign_up_page()
        sign_up.click_Close()
