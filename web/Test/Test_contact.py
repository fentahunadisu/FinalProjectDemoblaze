
from web.Page.web_page.Contact_page import contact_run
from web.BaseTest.base import Base_home
import pytest
import allure


class Test_contactPage(Base_home):

    @allure.description('sign_up correctly')
    def test_sign_up_correctly(self):
        driver = self.driver
        signup = contact_run(driver)
        signup.click_contact_page()
        signup.enter_Username('bela')
        signup.enter_passwored('testsu12')
        signup.Click_massage('never give up ')
        signup.send_button_click()
        signup.alat_off()
