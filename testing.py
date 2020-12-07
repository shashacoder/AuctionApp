import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AuctionLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_in_auction_app(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/?next=/")
        self.assertIn("Online Auctions", driver.title)
        username = driver.find_element_by_id("id_username")
        username.send_keys("ranka123")
        password=driver.find_element_by_id("id_password")
        password.send_keys("Aditya@123")
        clicking=driver.find_element_by_id("submitButton")
        clicking.click()
        loginbutton=driver.find_element_by_id("createAuction")
        loginbutton.click()
        titlename = driver.find_element_by_name("title")
        titlename.send_keys("jnjnl")                                                  #add title here
        description = driver.find_element_by_name("description")
        description.send_keys("mkjj")                                                #add description here
        driver.find_element_by_name("image").send_keys(os.getcwd()+"/garima.jpeg")          #add the image here
        val = driver.find_element_by_name("min_value")
        val.send_keys("100")                                                        #add value here
        clickCreate=driver.find_element_by_id("submitAuction")
        clickCreate.click()
        clickLogout = driver.find_element_by_id("logout")
        clickLogout.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()