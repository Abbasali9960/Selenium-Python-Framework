from selenium import webdriver
import unittest
import HTMLTestRunner

from Pages.AddToCart import Addtocart
from Pages.Checkout import Checkout
from Pages.Login import loginPopup
from Pages.HomePage import Search
from Pages.Logout import Logout


class Flipcart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"D:\Selenium-PYTHON\Python-Test-Automation-Framework-master\driver\chromedriver_80.exe")
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        login = loginPopup(driver)
        login.click_popup()
        login.click_loginonhomepage()
        login.enter_username("9620690281")
        login.enter_password("Chinnu1989$")
        login.click_loginbutton()


        search = Search(driver)
        search.enter_productname("samsung s10")
        search.click_product()


        addtocart = Addtocart(driver)
        addtocart.click_addtocart()
        addtocart.click_plussign()
        addtocart.click_savebutton()
        addtocart.click_movetocartbutton()
        addtocart.click_placeorderbutton()

        checkout = Checkout(driver)
        checkout.enter_name("Shilpashree")
        checkout.enter_phno("9620689990")
        checkout.enter_pincode("577204")
        checkout.enter_locality("Vinobanagar")
        checkout.enter_address("Sri Maruthi Krupa,60 feet Road,Vinoba nagar")
        checkout.enter_landmark("OPP ShubhaMangala Kalyana Mantapa")
        checkout.click_homeaddress()
        checkout.click_deliverbutton()
        checkout.click_continuebutton()
        checkout.click_flipcarthomebutton()

        logout = Logout(driver)
        logout.close()



        if __name__ == '__main__':
            unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(
                output='D:/Selenium-PYTHON\Python-Test-Automation-Framework-master/Reports'))
