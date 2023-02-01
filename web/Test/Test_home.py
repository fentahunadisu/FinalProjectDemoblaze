import allure
import pytest

from web.BaseTest.base import Base_home
from web.Page.web_page.Home_Page import TestHome


class Test_run(Base_home):

    @pytest.mark.sanity
    @allure.description('click phone type')
    def test_home_phone(self):
        driver = self.driver
        test_phone = TestHome(driver)
        test_phone.click_home_phone()

    @pytest.mark.sanity
    @allure.description('display product phone')
    def test_phone(self):
        driver = self.driver
        testPhone = TestHome(driver)
        testPhone.click_phone()

    def test_samsung(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.samsung_galaxy()

    def test_home_nokia(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.Nokia_lumia_1520()

    def test_cart(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.Nokia_lumia_1520()
        Test_Home.click_cart()
        Test_Home.alat_off()
        Test_Home.click_cart_home()

    def test_logo(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_logo()

    def test_product_store(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_product_store()

    def test_scroll(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_scroll()

    def test_scroll_right(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_scroll_right()

    def test_scroll_left(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_scroll_left()

    def test_nokia(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.Nokia_lumia_1520()

    def test_nokia_text(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.Nokia_lumia_1520()
        Test_Home.mach_text_nokia()

    def test_nokia_price(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.Nokia_lumia_1520()
        Test_Home.mach_phone_price()

    def test_Nexus_6Phone(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_Nexus_6Phone()
        Test_Home.mach_nexus_price()
        Test_Home.mach_nexus_price()

    def test_samsungGalaxy_S7(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_samsungGalaxy_S7()
        Test_Home.samsungGalaxy_S7()
        Test_Home.mach_samsung7_text()
        Test_Home.mach_samsung7_price()

    def test_iphone_6_32gb(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_iphone_6_32gb()
        Test_Home.mach_iphone_text()
        Test_Home.mach_phone_price()

    def test_sonyXperia_z5(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_sonyXperia_z5()
        Test_Home.mach_sonyXperia_text()
        Test_Home.mach_sonyXperia_price()

    def test_htc(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.click_htc()
        Test_Home.mach_htc_price()
        Test_Home.mach_htc_price()

    def test_next_page(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.scroll_page_down()
        Test_Home.click_next_page()

    def test_previous_page(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.scroll_page_down()
        Test_Home.click_previous_page()

    def test_lapSonyI5_page(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.scroll_page_down()
        Test_Home.click_lapI5_page()
        Test_Home.click_lapI5_text()
        Test_Home.click_lapI5_price()
        Test_Home.click_lapI5_add()
        Test_Home.alat_off()

    def test_lapSonyI7_page(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.scroll_page_down()
        Test_Home.click_lapI7_page()
        Test_Home.click_lapI7_text()
        Test_Home.click_lapI7_add()
        Test_Home.alat_off()
        Test_Home.click_cart()
        Test_Home.click_place_order()
        Test_Home.enter_name("fentahun")
        Test_Home.enter_country("israel")
        Test_Home.enter_city("beer sheva")
        Test_Home.enter_credit_card("6543278190")
        Test_Home.enter_month("april")
        Test_Home.enter_year("1996")
        Test_Home.click_purchas()

    def test_lapSonyI7_price(self):
        driver = self.driver
        Test_Home = TestHome(driver)
        Test_Home.scroll_page_down()
        Test_Home.click_lapI7_page()
        Test_Home.click_lapI7_price()

