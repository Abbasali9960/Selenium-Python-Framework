import time

from selenium.webdriver.common.keys import Keys


class Search():

    def __init__(self,driver):
        self.driver = driver
        self.search_item_xpath = "//input[@class='LM6RPg']"
        self.select_prd_xpath = "//div[text()='Samsung Galaxy S10 (Prism Black, 128 GB)']"


    def enter_productname(self, productname):
        self.driver.find_element_by_xpath(self.search_item_xpath).send_keys(productname, Keys.ENTER)
        time.sleep(10)

    def click_product(self):
        self.driver.find_element_by_xpath(self.select_prd_xpath).click()


