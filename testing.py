import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AuctionLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_in_auction_app(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Online Auctions", driver.title)
        username = driver.find_element_by_id("id_username")
        username.send_keys("")                                                  #add username
        password=driver.find_element_by_id("id_password")
        password.send_keys("")                                                  #add password
        clicking=driver.find_element_by_id("submitButton")
        clicking.click()
        clickCreate=driver.find_element_by_id("createAuction")
        clickCreate.click()
        titlename = driver.find_element_by_name("title")
        titlename.send_keys("")                                                 #add title here
        description = driver.find_element_by_name("description")
        description.send_keys("")                                               #add description here
        driver.find_element_by_name("image").send_keys(os.getcwd()+"/")         #add image here
        val = driver.find_element_by_name("min_value")
        val.send_keys("")                                                       #add value here
        clickSubmit=driver.find_element_by_id("submitAuction")
        clickSubmit.click()
        clickLogout = driver.find_element_by_id("logout")
        clickLogout.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()