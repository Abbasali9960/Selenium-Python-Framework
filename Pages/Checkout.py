
import time


class Checkout():

    def __init__(self,driver):
        self.driver = driver
        self.name_textbox_xpath = "//input[@name='name']"
        self.phoneno_xpath = "//input[@name='phone']"
        self.pincode_xpath = "//input[@name='pincode']"
        self.locality_xpath = "//input[@name='addressLine2']"
        self.address_xpath = "//textarea[@name='addressLine1']"
        self.landmark_xpath = "//input[@name='landmark']"
        self.home_xpath = "//span[text()='Home (All day delivery)']"
        self.deliver_xpath = "//button[@class='_2AkmmA EqjTfe _7UHT_c']"
        self.continue_xpath = "//button[text()='CONTINUE']"
        self.flipcart_xpath = "//img[@title='Flipkart']"



    def enter_name(self,name):
        time.sleep(15)
        self.driver.find_element_by_xpath(self.name_textbox_xpath).send_keys(name)

    def enter_phno(self,phoneno):
        self.driver.find_element_by_xpath(self.phoneno_xpath).send_keys(phoneno)
        time.sleep(10)

    def enter_pincode(self,pincode):
        self.driver.find_element_by_xpath(self.pincode_xpath).send_keys(pincode)
        time.sleep(10)

    def enter_locality(self,locality):
        self.driver.find_element_by_xpath(self.locality_xpath).clear()
        self.driver.find_element_by_xpath(self.locality_xpath).send_keys(locality)
        time.sleep(10)

    def enter_address(self,address):
        self.driver.find_element_by_xpath(self.address_xpath).clear()
        self.driver.find_element_by_xpath(self.address_xpath).send_keys(address)
        time.sleep(10)


    def enter_landmark(self,landmark):
        time.sleep(10)
        self.driver.find_element_by_xpath(self.landmark_xpath).clear()
        self.driver.find_element_by_xpath(self.landmark_xpath).send_keys(landmark)

    def click_homeaddress(self):
        self.driver.find_element_by_xpath(self.home_xpath).click()
        time.sleep(15)

    def click_deliverbutton(self):
        self.driver.find_element_by_xpath(self.deliver_xpath).click()
        time.sleep(10)


    def click_continuebutton(self):
        self.driver.find_element_by_xpath(self.continue_xpath).click()
        time.sleep(10)

    def click_flipcarthomebutton(self):
        self.driver.find_element_by_xpath(self.flipcart_xpath).click()

