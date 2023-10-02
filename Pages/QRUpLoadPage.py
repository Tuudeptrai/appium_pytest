from Pages.BasePage import BasePage
from Utilities import configReader
from Utilities.readProperties import ReadConfig
from Utilities.readjsonData import ReadJson
from Utilities.randomeString import RanDom
from Utilities.scroll_util import ScrollUtil
from Utilities.readJsonScreenshot import ReadJsonScreenshot 
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.mobileby import MobileBy as mobily_by
import time
from libs.helpers.mail_helper import get_cloudflare_code
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wwait
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
import json
import requests
import jsonpath
import os
from Pages.AuthorizationPage import Authorization
class QRUpload(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def TakeScreenshot(self):
      

        assert True
        print(" turn on chrome browser in phone")
        self.driver = self.driver.start_activity("com.android.chrome","org.chromium.chrome.browser.ChromeTabbedActivity")
        print(" typing ""gmail"" to serch text field")
        self.driver.find_element_by_id(configReader.readConfig("locators", "el_chrome_search_box_text_ID")).send_keys("react-app.walletconnect.com"+"\n")
        time.sleep(3)
        print("click in first search hint")
        self.driver.find_element_by_id(configReader.readConfig("locators", "el_chrome_search_line_1_ID")).click()
        time.sleep(10)
        print("click in Eth_goerliBtn & click connect btn & click QR code generator")
        self.driver.find_element_by_xpath(configReader.readConfig("locators", "el_dapp_Eth_Goerli_btn")).click()
        time.sleep(3)
        print("scroll up")
        ScrollUtil.swipeUp(7,self.driver)
        time.sleep(3)
        self.driver.find_element_by_xpath(configReader.readConfig("locators", "el_dapp_connect_select_btn")).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(configReader.readConfig("locators", "el_dapp_QRcode_btn")).click()
        time.sleep(3)
        b=datetime.now().strftime("%d%m%Y%H%M%S")
        self.driver.save_screenshot("../ScreenShot/"+b+".png")
        a = {
                "namepicture": b,
                "url": "",
                "pic_id":"" 
            }
        ReadJsonScreenshot.writetoafile(a)
        c =  '../ScreenShot/'+ ReadJsonScreenshot.geinputData()["namepicture"]+".png"
        files = {
                'file': open( c, 'rb'),
                'custom_id': (None, 'SampleMedia'+RanDom.random_string_generator(5)),
        }
        response = requests.post('https://api-cloud.browserstack.com/app-automate/upload-media', files=files, auth=('testsavvy_deyw9B', 'AWsf9sjzd5YFxTu1Pmwc'))
        print(response.text)
        responseJson = json.loads(response.text)
        a = {
                "namepicture": ReadJsonScreenshot.geinputData()["namepicture"]+".png",
                "url": responseJson["media_url"],
                "pic_id":responseJson["custom_id"]
            }
        ReadJsonScreenshot.writetoafile(a)

