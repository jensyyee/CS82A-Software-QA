# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re


links_landing_titles ={
    "RESOURCES" : "Resources",
    "PRICING" : "Sauce Labs: Pricing",
    "FEATURES" : "Features",
    "DOCS" : "Sauce Labs Docs",
    "SIGN UP" : "Sauce Labs: Sign Up for a Free Trial",
    "COMPANY" : "Values",
    "ENTERPRISE" : "Sauce Labs: Enterprise-grade testing on Sauce",
    "LOGIN" : "Login",
    "COMMUNITY" : "Open Sauce",
    "SOLUTIONS" : "Selenium Testing by Sauce Labs",
    }

class Saucenav1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_saucenav(self):
        driver = self.driver

        for link in links_landing_titles: 
            driver.get(self.base_url)
            driver.find_element_by_xpath("//li/a[@class='hamburger']").click()
            driver.find_element_by_link_text(link).click()
            expected_title = links_landing_titles[link]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))
    
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
