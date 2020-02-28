import time


class Addtocart():

    def __init__(self,driver):
        self.driver = driver
        Parent_Window = driver.current_window_handle
        All_Windows = driver.window_handles

        for Child_Window in All_Windows:
            driver.switch_to.window(Child_Window)
            driver.implicitly_wait(20)

        self.add_tocart_xpath = "//button[text()='ADD TO CART']"
        self.increase_prodqty_xpath = "//button[text()='+']"
        self.save_forlater_xpath = "//div[text()='Save for later']"
        self.move_tocart_xpath = "//div[text()='Move to cart']"
        self.place_order_xpath = "//span[text()='Place Order']"


    def click_addtocart(self):
        self.driver.find_element_by_xpath(self.add_tocart_xpath).click()
        time.sleep(10)

    def click_plussign(self):
        self.driver.find_element_by_xpath(self.increase_prodqty_xpath).click()
        time.sleep(5)

    def click_savebutton(self):
        self.driver.find_element_by_xpath(self.save_forlater_xpath).click()
        time.sleep(5)

    def click_movetocartbutton(self):
        self.driver.find_element_by_xpath(self.move_tocart_xpath).click()
        time.sleep(10)

    def click_placeorderbutton(self):
        self.driver.find_element_by_xpath(self.place_order_xpath).click()
        time.sleep(5)
