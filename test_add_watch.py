# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from webdriver_manager.chrome import ChromeDriverManager
import os


class test_add_watch(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_test_add_watch(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/watchshop/sign-in/?next=/watchshop/")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("Nixer")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("nixer")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Add watch").click()
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Glycyrrhiza glabra")
        driver.find_element_by_id("id_short_description").click()
        driver.find_element_by_id("id_short_description").clear()
        driver.find_element_by_id("id_short_description").send_keys("G-Shock")
        driver.find_element_by_id("id_image").click()
        driver.find_element_by_id("id_price").clear()
        driver.find_element_by_id("id_image").send_keys(os.getcwd()+"/01.jpg")
        driver.find_element_by_id("id_price").click()
        driver.find_element_by_id("id_price").clear()
        driver.find_element_by_id("id_price").send_keys("3000")
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
