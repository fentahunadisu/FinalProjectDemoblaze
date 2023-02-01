
from web.Page.web_page.cart_page import cart_page
from web.BaseTest.base import Base_home
import pytest
import allure


class Test_cart_page(Base_home):

    @allure.description
    def test_cart_correctly(self):
        driver = self.driver
        cart = cart_page(driver)
        cart.click_cart()
        cart.click_place_order()
        cart.enter_name("fentahun")
        cart.enter_country("israel")
        cart.enter_city("beer sheva")
        cart.enter_credit_card("6543278190")
        cart.enter_month("april")
        cart.enter_year("1996")
        cart.click_purchas()
        # cart.click_close()