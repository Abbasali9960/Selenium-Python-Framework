import time


class loginPopup():

    def __init__(self,driver):
        self.driver = driver

        self.close_popup = "//button [@class='_2AkmmA _29YdH8']"
        self.log_xpath = "//a[text()='Login']"
        self.username_textbox_xpath = "//input[@class='_2zrpKA _1dBPDZ']"
        self.password_textbox_xpath = "//input[@class='_2zrpKA _3v41xv _1dBPDZ']"
        self.login_button_xpath = "(//span[text()='Login'])[2]"

    def click_popup(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.close_popup)

    def click_loginonhomepage(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.log_xpath)

    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_loginbutton(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        time.sleep(5)

