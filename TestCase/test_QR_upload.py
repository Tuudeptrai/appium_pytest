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
from Pages.QRUpLoadPage import QRUpload
import json
import requests
import jsonpath
from Utilities.readProperties import ReadConfig
from Utilities.readjsonData import ReadJson
from appium.webdriver.common.touch_action import TouchAction
from Pages.AuthorizationPage import Authorization

class TestQRUpload(BaseTest):
    def test_QR(self):
        # qRUP = QRUpload(self.driver)
        # time.sleep(4)
        # qRUP.TakeScreenshot()
        auth = Authorization(self.driver)
        time.sleep(4)
        auth.get_operation()
