import time


class Forgot():

    def __init__(self, driver):
        self.driver = driver
        self.close_popup = "//button [@class='_2AkmmA _29YdH8']"
        self.log_xpath = "//a[text()='Login']"
        self.username_textbox_xpath = "//input[@class='_2zrpKA _1dBPDZ']"
        self.Forgotpassword_xpath = "//span[text()='Forgot?']"


    def click_popup(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.close_popup)

    def click_loginonhomepage(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.log_xpath)

    def enter_username(self,username):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def click_forgot(self):
        time.sleep(10)
        self.driver.find_element_by_xpath(self.Forgotpassword_xpath).click()

    def logout(self):
        self.driver.quit()

