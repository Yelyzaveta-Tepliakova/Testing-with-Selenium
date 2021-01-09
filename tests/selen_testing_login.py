#####################################################################
## Description:    The program makes UI tests to log in using
##                 https://semantic-ui.com/examples/login.html
#####################################################################
## Author:         Yelyzaveta Tepliakova
## Python version: 3.8.
## Date:           25.12.2020
#####################################################################

import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


if os.path.isfile("test_login.txt") == True:    # creates file for results of test_login
    os.remove("test_login.txt")
with open("test_login.txt", 'w') as doc:
    doc.write("\n\n\nTest suite \"testing login\":\n")


class tests_for_login(unittest.TestCase):    # unittests for ability to log in


    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url="https://semantic-ui.com/examples/login.html")


    def test1_NoData(self):       # pressing log in button without data and writing result into file
        search = self.driver.find_element_by_class_name(name="ui.fluid.large.teal.submit.button")
        search.click()
        try:
            assert "Please enter your e-mail" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter a valid e-mail" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter your password" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Your password must be at least 6 characters" in self.driver.find_element_by_class_name(
                "ui.error.message").text
            print("Test \"test1_NoData\" passed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test1_NoData\" passed")
        except:
            print("Test \"test1_NoData\" failed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test1_NoData\" failed")


    def test2_OnlyInvalidEmail(self):   # pressing log in button with invalid email and writing result into file
        email = self.driver.find_element_by_name("email")
        email.send_keys("hello")
        search = self.driver.find_element_by_class_name(name="ui.fluid.large.teal.submit.button")
        search.click()
        try:
            assert "Please enter your e-mail" not in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter a valid e-mail" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter your password" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Your password must be at least 6 characters" in self.driver.find_element_by_class_name(
                "ui.error.message").text
            print("Test \"test2_OnlyInvalidEmail\" passed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test2_OnlyInvalidEmail\" passed")
        except AssertionError:
            print("Test \"test2_OnlyInvalidEmail\" failed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test2_OnlyInvalidEmail\" failed")


    def test3_OnlyValidEmail(self):   # pressing log in button with valid email and writing result into file
        email = self.driver.find_element_by_name("email")
        email.send_keys("elon_musk@gmail.com")
        search = self.driver.find_element_by_class_name("ui.fluid.large.teal.submit.button")
        search.click()
        try:
            assert "Please enter your e-mail" not in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter a valid e-mail" not in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter your password" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Your password must be at least 6 characters" in self.driver.find_element_by_class_name(
                "ui.error.message").text
            print("Test \"test3_OnlyValidEmail\" passed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test3_OnlyValidEmail\" passed")
        except AssertionError:
            print("Test \"test3_OnlyValidEmail\" failed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test3_OnlyValidEmail\" failed")


    def test4_OnlyTooShortPassword(self):   # pressing log in button with too short password and writing result into file
        password = self.driver.find_element_by_name("password")
        password.send_keys("world")
        search = self.driver.find_element_by_class_name("ui.fluid.large.teal.submit.button")
        search.click()
        try:
            assert "Please enter your e-mail" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter a valid e-mail" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter your password" not in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Your password must be at least 6 characters" in self.driver.find_element_by_class_name(
                "ui.error.message").text
            print("Test \"test4_OnlyTooShortPassword\" passed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test4_OnlyTooShortPassword\" passed")
        except AssertionError:
            print("Test \"test4_OnlyTooShortPassword\" failed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test4_OnlyTooShortPassword\" failed")


    def test5_OnlyPasswordWithEnoughSymbols(self):  # pressing log in button with password consisting enough symbols
                                                    # and writing result into file
        password = self.driver.find_element_by_name("password")
        password.send_keys("worldworld")
        search = self.driver.find_element_by_class_name("ui.fluid.large.teal.submit.button")
        search.click()
        try:
            assert "Please enter your e-mail" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter a valid e-mail" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter your password" not in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Your password must be at least 6 characters" not in self.driver.find_element_by_class_name(
                "ui.error.message").text
            print("Test \"test5_OnlyPasswordWithEnoughSymbols\" passed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test5_OnlyPasswordWithEnoughSymbols\" passed")
        except AssertionError:
            print("Test \"test5_OnlyPasswordWithEnoughSymbols\" failed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test5_OnlyPasswordWithEnoughSymbols\" failed")


    def test6_InvalidEmailWithTooShortPassword(self):  # pressing log in button with invalid email and too short
                                                       # password and writing result into file
        email = self.driver.find_element_by_name("email")
        email.send_keys("hello")
        password = self.driver.find_element_by_name("password")
        password.send_keys("world")
        search = self.driver.find_element_by_class_name("ui.fluid.large.teal.submit.button")
        search.click()
        try:
            assert "Please enter your e-mail" not in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter a valid e-mail" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter your password" not in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Your password must be at least 6 characters" in self.driver.find_element_by_class_name(
                "ui.error.message").text
            print("Test \"test6_InvalidEmailWithTooShortPassword\" passed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test6_InvalidEmailWithTooShortPassword\" passed")
        except AssertionError:
            print("Test \"test6_InvalidEmailWithTooShortPassword\" failed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test6_InvalidEmailWithTooShortPassword\" failed")


    def test7_InvalidEmailWithPasswordWithEnoughSymbols(self): # pressing log in button with invalid email and password
                                                               # consisting enough symbols and writing result into file
        email = self.driver.find_element_by_name("email")
        email.send_keys("hello")
        password = self.driver.find_element_by_name("password")
        password.send_keys("worldworld")
        search = self.driver.find_element_by_class_name("ui.fluid.large.teal.submit.button")
        search.click()
        try:
            assert "Please enter your e-mail" not in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter a valid e-mail" in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Please enter your password" not in self.driver.find_element_by_class_name("ui.error.message").text
            assert "Your password must be at least 6 characters" not in self.driver.find_element_by_class_name(
                "ui.error.message").text
            print("Test \"test7_InvalidEmailWithPasswordWithEnoughSymbols\" passed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test7_InvalidEmailWithPasswordWithEnoughSymbols\" passed")
        except AssertionError:
            print("Test \"test7_InvalidEmailWithPasswordWithEnoughSymbols\" failed")
            with open("test_login.txt", 'a') as doc:
                doc.write("\nTest case \"test7_InvalidEmailWithPasswordWithEnoughSymbols\" failed")


    # def test8_ValidEmailWithPasswordWithTooShortPassword(self):  # pressing log in button with valid email
    #                                                              # and too short password and writing result into file
    #     email = self.driver.find_element_by_name("email")
    #     email.send_keys("elon_musk@gmail.com")
    #     password = self.driver.find_element_by_name("password")
    #     password.send_keys("world")
    #     search = self.driver.find_element_by_class_name("ui.fluid.large.teal.submit.button")
    #     search.click()
    #     try:
    #         assert "Please enter your e-mail" not in self.driver.find_element_by_class_name("ui.error.message").text
    #         assert "Please enter a valid e-mail" not in self.driver.find_element_by_class_name("ui.error.message").text
    #         assert "Please enter your password" not in self.driver.find_element_by_class_name("ui.error.message").text
    #         assert "Your password must be at least 6 characters" in self.driver.find_element_by_class_name(
    #         "ui.error.message").text
    #         print("Test \"test8_ValidEmailWithPasswordWithTooShortPassword\" passed")
    #         with open("test.txt", 'a') as doc:
    #             doc.write("\nTest case \"test8_ValidEmailWithPasswordWithTooShortPassword\" passed")
    #     except AssertionError:
    #         print("Test \"test8_ValidEmailWithPasswordWithTooShortPassword\" failed")
    #         with open("test.txt", 'a') as doc:
    #             doc.write("\nTest case \"test8_ValidEmailWithPasswordWithTooShortPassword\" failed")


    # def test9_ValidEmailWithPasswordWithEnoughSymbols(self):  # pressing log in button with valid email and password
    #                                                           # consisting enough symbols and writing result into file
    #     email = self.driver.find_element_by_name("email")
    #     email.send_keys("elon_musk@gmail.com")
    #     password = self.driver.find_element_by_name("password")
    #     password.send_keys("worldworld")
    #     search = self.driver.find_element_by_class_name("ui.fluid.large.teal.submit.button")
    #     search.click()
    #     try:
    #         assert "Please enter your e-mail" not in self.driver.find_element_by_class_name("ui.error.message").text
    #         assert "Please enter a valid e-mail" not in self.driver.find_element_by_class_name("ui.error.message").text
    #         assert "Please enter your password" not in self.driver.find_element_by_class_name("ui.error.message").text
    #         assert "Your password must be at least 6 characters" not in self.driver.find_element_by_class_name(
    #         "ui.error.message").text
    #         print("Test \"test9_ValidEmailWithPasswordWithEnoughSymbols\" passed")
    #         with open("test.txt", 'a') as doc:
    #             doc.write("\nTest case \"test9_ValidEmailWithPasswordWithEnoughSymbols\" passed")
    #     except AssertionError:
    #         print("Test \"test9_ValidEmailWithPasswordWithEnoughSymbols\" failed")
    #         with open("test.txt", 'a') as doc:
    #             doc.write("\nTest case \"test9_ValidEmailWithPasswordWithEnoughSymbols\" failed")


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()