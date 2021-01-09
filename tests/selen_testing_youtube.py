#####################################################################
## Description:    The program makes UI tests for YouTube using
##                 https://www.youtube.com/watch?v=D08L2JJB1ag
#####################################################################
## Author:         Yelyzaveta Tepliakova
## Python version: 3.8.
## Date:           26.12.2020
#####################################################################


import os
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


if os.path.isfile("YouTube_testing_results.txt") is True:  # creates file for results of YouTube_test
    os.remove("YouTube_testing_results.txt")
with open("YouTube_testing_results.txt", 'w') as doc:
    doc.write("\n\n\nTest suite \"testing YouTube\":\n")


class YouTubeTesting(unittest.TestCase):
    """
    Tests for some abilities in YouTube
    """

    def setUp(self):
        """

        :return: None
        """
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url="https://www.youtube.com/watch?v=D08L2JJB1ag")
        self.driver.set_window_size(1200, 600)


    def test1_inability_to_like_video(self):
        """
        The test case is intended for checking of inability
        to like video if user is not signed in
        :return: None
        """
        name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/'
                                                  'div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/'
                                                  'div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/'
                                                  'a/yt-icon-button/button/yt-icon')))
        name.click()
        name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/ytd-popup-container/iron-dropdown/div/'
                                                      'ytd-modal-with-title-and-button-renderer/yt-formatted-string[2]')))
        name = self.driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/iron-dropdown/div/"
                                                 "ytd-modal-with-title-and-button-renderer/yt-formatted-string[2]").text
        try:
            assert name == "Увійдіть, щоб ми могли врахувати вашу думку."
            print("Test \"test1_inability_to_like_video_if_not_signed_in\" passed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test1_inability_to_like_video_if_not_signed_in\" passed")
        except AssertionError:
            print("Test \"test1_inability_to_like_video_if_not_signed_in\" failed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test1_inability_to_like_video_if_not_signed_in\" failed")


    def test2_press_sign_in_button(self):
        """
        The test case is intended for checking of press the button to sign in
        :return: None
        """
        name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/'
                                                  'div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/'
                                                  'div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/'
                                                  'yt-icon-button/button/yt-icon')))
        name.click()
        name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/ytd-popup-container/iron-dropdown/div/'
                                                  'ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer'
                                                  '/a/paper-button/yt-formatted-string')))
        name.click()
        try:
            assert self.driver.current_url == "https://accounts.google.com/ServiceLogin?service=youtube&uilel=" \
                                              "3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3" \
                                              "Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Duk%26next%3D%252" \
                                              "Fwatch%253Fv%253DD08L2JJB1ag&hl=uk&ec=66426"
            print("Test \"test2_pressing_button_to_sign_in\" passed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test2_pressing_button_to_sign_in\" passed")
        except:
            print("Test \"test2_pressing_button_to_sign_in\" failed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test2_pressing_button_to_sign_in\" failed")


    def test3_going_to_the_channel(self):
        """
        The test case is intended for checking of the button to go to channel
        :return: None
        """
        name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/'
                                                  'div[1]/div/div[6]/div[3]/ytd-video-secondary-info-renderer/div/'
                                                  'div[2]/ytd-video-owner-renderer/a/yt-img-shadow/img')))
        name.click()
        try:
            assert self.driver.current_url == "https://www.youtube.com/user/novychannel"
            print("Test \"test3_going_to_the_channel\" passed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test3_going_to_the_channel\" passed")
        except:
            print("Test \"test3_going_to_the_channel\" failed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test3_going_to_the_channel\" failed")


    def test4_open_instagram(self):
        """
        The test case is intended for checking of button pressing
        of going to channel and opening instagram
        :return: None
        """

        # checks button going to channel and opening instagram
        name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/'
                                                  'div[1]/div/div[6]/div[3]/ytd-video-secondary-info-renderer/div/'
                                                  'div[2]/ytd-video-owner-renderer/a/yt-img-shadow/img')))
        name.click()
        name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/'
                                                  'ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/'
                                                  'div[2]/div[2]/div/div[2]/div[2]/a[3]/yt-img-shadow/img')))
        name.click()
        try:
            assert len(self.driver.window_handles) == 2
            print("Test \"test4_going_to_the_channel_and_opening_instagram\" (part 1) passed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test4_going_to_the_channel_and_opening_instagram\" (part 1) passed")
        except:
            print("Test \"test4_going_to_the_channel_and_opening_instagram\" (part 1)failed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test4_going_to_the_channel_and_opening_instagram\" (part 1)failed")
        self.driver.switch_to.window(self.driver.window_handles[1])
        try:
            assert self.driver.current_url == "https://www.instagram.com/accounts/login/"
            print("Test \"test4_going_to_the_channel_and_opening_instagram\" (part 2) passed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test4_going_to_the_channel_and_opening_instagram\" (part 2) passed")
        except:
            print("Test \"test4_going_to_the_channel_and_opening_instagram\" (part 2) failed")
            with open("test_YouTube.txt", 'a') as doc:
                doc.write("\nTest case \"test4_going_to_the_channel_and_opening_instagram\" (part 2) failed")


    def tearDown(self):
        pass


if __name__ == "__main__":
    result = unittest.main()
