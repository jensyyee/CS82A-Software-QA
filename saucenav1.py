# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re


links_landing_titles ={
    "RESOURCES" : "Resources",
    "SIGN UP" : "Sauce Labs: Sign Up for a Free Trial",
    "COMPANY" : "Values",
    "LOGIN" : "Login",
    "COMMUNITY" : "Open Sauce",
    "SOLUTIONS" : "Selenium Testing by Sauce Labs",
    }

#Titles with dupicate in the main nav bar: they need to be handled with xpath.
links_by_xpath = {
    "(//a[contains(text(),'Enterprise')])[3]": "Sauce Labs: Enterprise-grade testing on Sauce",
    "(//a[contains(text(),'Pricing')])[3]": "Sauce Labs: Pricing",
    "(//a[contains(text(),'Features')])[3]": "Features",
    "(//a[contains(text(),'Docs')])[3]": "Sauce Labs Docs",
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

        for link in links_by_xpath:
            driver.get(self.base_url)
            driver.find_element_by_css_selector("a.hamburger").click()
            driver.find_element_by_xpath(link).click()
            expected_title = links_by_xpath[link]
            try:
                self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e:
                self.verificationErrors.append(str(e))
                
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
