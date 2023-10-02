# Android environment
import os
import time
import pytest
import pyotp
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from TestCase.BaseTest import BaseTest
from Utilities import dataProvider
from Pages.AuthorizationPage import Authorization
import json
import requests
import jsonpath
from Utilities.readProperties import ReadConfig
from Utilities.readjsonData import ReadJson
from appium.webdriver.common.touch_action import TouchAction

class TestAuthorization(BaseTest):
    tokenLogin = ""
    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    @pytest.mark.TC_
    # @pytest.mark.parametrize("user,password", dataProvider.get_data("LoginTest"))
    def test_auth(self):
        auth = Authorization(self.driver)
        time.sleep(4)
        
        # print(" tap on screen the location of NOTIFICATIONS ALLOW")
        # window_width = self.driver.get_window_size()["width"]
        # window_height = self.driver.get_window_size()["height"]
        # x = window_width * 0.625
        # y = window_height * 0.594
        # print("x:",x, "y:", y)
        # TouchAction(self.driver).tap(None,x, y).perform()
        #if in box is empty then open the code below
        # auth.clickElLoginWithEmail()
        # time.sleep(1)
        # auth.sendkeyElEmail(user)
        # time.sleep(1)
        # auth.clickElNext()
        print("===delete all old mail===")
       
        auth.deleteGmail()
        print("===type email to atato===")
        auth.clickElLoginWithEmail()
        time.sleep(5)
        auth.sendkeyElEmail(self.user)
        time.sleep(5)
        print("===click next to go to email===")
        auth.clickElNext()
        time.sleep(10)
        print("===click workspace in email===")
        auth.openChrome()
        print("===type password to atato===")
        auth.sendkeyElPassword(self.password)
        time.sleep(2)
        print("===click login button atato===")
        auth.clickElLogin()
        time.sleep(5)
        print("===tap to skip face id scan===")
        auth.clickDoitlater()
        self.driver.execute_script("browserstack_executor: {\"action\":\"biometric\", \"arguments\": {\"biometricMatch\" : \"pass\"}}")
        print("===send api create the approver===")
        auth.create_approver()
        print("===click dropdown approver===")
        auth.clickApproverDropdown()
        time.sleep(15)
        print("===scroll and click the approver===", ReadJson.geinputData()["approver_name"])
        auth.clickScrollToTheApprover(ReadJson.geinputData()["approver_name"])
        # window_width = self.driver.get_window_size()["width"]
        # window_height = self.driver.get_window_size()["height"]
        # x = window_width * 0.5
        # y = window_height * 0.65
        # print("x:",x, "y:", y)
        # TouchAction(self.driver).tap(None,x, y).perform()
        time.sleep(10)
        print("===type code of approver===", ReadJson.geinputData()["approver_code"])
        auth.typeCodeApprover(ReadJson.geinputData()["approver_code"])
        time.sleep(10)
        print("===click active of approver===")
        auth.clickApproverActive()
        time.sleep(10)
        print("===create a rule==")
        auth.create_rule()
        time.sleep(10)
        print("===create a wallet===")
        auth.create_walet()
        time.sleep(10)
        print("===verify a wallet===")
        auth.verify_walet()
        time.sleep(10)
   


