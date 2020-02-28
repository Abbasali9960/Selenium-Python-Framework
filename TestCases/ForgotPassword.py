from selenium import webdriver
import unittest
import HTMLTestRunner

from Pages.ForgotPassword import Forgot

class Flipcart1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"D:\Selenium-PYTHON\Python-Test-Automation-Framework-master\driver\chromedriver_80.exe")
        cls.driver.maximize_window()

    def test_forgotpassword(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        forgotpassword = Forgot(driver)
        forgotpassword.click_popup()
        forgotpassword.click_loginonhomepage()
        forgotpassword.enter_username("9620690281")
        forgotpassword.click_forgot()
        forgotpassword.logout()

    if __name__ == '__main__':
        unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(
            output=r'D:\Selenium-PYTHON\Python-Test-Automation-Framework-master\Reports'))
