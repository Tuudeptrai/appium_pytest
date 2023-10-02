from Pages.BasePage import BasePage
from Utilities import configReader
from Utilities.readProperties import ReadConfig
from Utilities.readjsonData import ReadJson
from Utilities.randomeString import RanDom
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

class Authorization(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    approver_code = 0
    approver_id = ""
    rule_id = ""
    wallet_id =""
    

    def clickElLoginWithEmail(self):
        self.click("el_login_with_email_XPATH")

    def sendkeyElEmail(self, user):
        self.type("el_email_XPATH", user)

    def clickElNext(self):
        self.click("el_next_XPATH")
    
    def deleteGmail(self):
        print(" turn on chrome browser in phone")
        self.driver = self.driver.start_activity("com.android.chrome","org.chromium.chrome.browser.ChromeTabbedActivity")
        print(" typing ""gmail"" to serch text field")
        self.driver.find_element_by_id(configReader.readConfig("locators", "el_chrome_search_box_text_ID")).send_keys("gmail")
        time.sleep(3)
        print("click in first search hint")
        self.driver.find_element_by_id(configReader.readConfig("locators", "el_chrome_search_line_1_ID")).click()
        time.sleep(3)
        print(" tap on screen the location of first search result")
        window_width = self.driver.get_window_size()["width"]
        window_height = self.driver.get_window_size()["height"]
        x = window_width * 0.5
        y = window_height * 0.45
        TouchAction(self.driver).tap(None,x, y).perform()
        time.sleep(6)
        print("click sign in button")
        window_width = self.driver.get_window_size()["width"]
        window_height = self.driver.get_window_size()["height"]
        x = window_width * 0.854321
        y = window_height * 0.123456789
        TouchAction(self.driver).tap(None,x, y).perform()
        time.sleep(5)
        print("type email or phone")
        self.driver.find_element_by_class_name(configReader.readConfig("locators", "el_chrome_gmail_username_CLASS")).send_keys(ReadConfig.getUseremail())
        self.driver.find_element_by_class_name(configReader.readConfig("locators", "el_chrome_gmail_passwordNext_CLASS")).click()
        time.sleep(5)
        print("type recovery email")
        self.driver.find_element_by_class_name(configReader.readConfig("locators", "el_chrome_gmail_password_CLASS")).send_keys(ReadConfig.getFromEmail())
        self.driver.find_element_by_class_name(configReader.readConfig("locators", "el_chrome_gmail_signinconsentNext_CLASS")).click()
        time.sleep(5)
        print("type name of our test mail")
        self.driver.find_element(mobily_by.XPATH, configReader.readConfig("locators", "el_firstName_ID")).send_keys("Test")
        self.driver.find_element(mobily_by.XPATH, configReader.readConfig("locators", "el_lastName_ID")).send_keys("Savvy")
        self.driver.find_element_by_class_name(configReader.readConfig("locators", "el_chrome_gmail_signinconsentNext_CLASS")).click()
        self.driver.find_element_by_class_name(configReader.readConfig("locators", "el_chrome_gmail_signinconsentNext_CLASS")).click()
        time.sleep(5)
        print("get active code from verify.app.atato@gmail.com")
        code =  get_cloudflare_code()
        time.sleep(5)
        print("fill active code")
        self.driver.find_element_by_class_name(configReader.readConfig("locators", "el_chrome_gmail_password_CLASS")).send_keys(code)
        self.driver.find_element_by_class_name(configReader.readConfig("locators", "el_chrome_gmail_signinconsentNext_CLASS")).click()
        time.sleep(5)
        print("click testing email ")
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_account_verified_XPATH")).click()
        print("type pass of testing mail")
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_account_pass_XPATH")).send_keys(ReadConfig.getPassword())
        self.driver.find_element_by_class_name(configReader.readConfig("locators", "el_chrome_gmail_signinconsentNext_CLASS")).click()
        time.sleep(8)
        print("click email in top")
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_top_email_BTN_XPATH")).click()
        print("delete email in inbox")
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_delete_mail_btn_XPATH")).click()
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_menu_mail")).click()
        print("enter trash")
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_menu_trash")).click()
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_checkbox_trash")).click()
        time.sleep(3)
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_delete_fever_trash")).click()
        time.sleep(3)
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_menu_mail")).click()
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_menu_inbox")).click()

        # self.scroll_down_until(
        #     lambda: self.wait_until_visible_by(
        #         mobily_by.ACCESSIBILITY_ID,
        #         configReader.readConfig("locators", "el_workspace__ACCESSIBILITYID"),
        #         timeout_duration=5,
        #     )
        # )
        time.sleep(5)
        print(" back to atatp")
        self.driver = self.driver.start_activity("com.atato.custody.qa","com.atato.custody.MainActivity")
       
        # print("click read more")
        # rm_elements =  self.driver.find_elements(mobily_by.XPATH,configReader.readConfig("locators", "el_more_read_XPATH"))
        # n = len(rm_elements)
        # print("day la n rm_elements:",n)
        # if n > 1 :
        #     rm_elements[n-1].click()
        # else:
        #     for i in rm_elements:
        #         i.click()

        # print("Move slider from top to bottom finger movement ")      
        # if ncomp >2 :
        #     TouchAction(self.driver).tap(None,x, y).perform()
        #     screenSize = self.driver.get_window_size()
        #     screenHeight = screenSize['height']   
        #     touchAction = TouchAction(self.driver)
        #     touchAction.press(None, x, screenHeight - (screenHeight/3)).wait(500).move_to(None, 0,screenHeight/3).release().perform()   
		
        # print("tap to the workspace")
        # print("day la n:",ncomp)
        # if ncomp >2:#two mails
        #             window_width = self.driver.get_window_size()["width"]
        #             window_height = self.driver.get_window_size()["height"]
        #             x = window_width * 0.5
        #             y = window_height * 0.219
        #             TouchAction(self.driver).tap(None,x, y).perform()
        # else:# one mail
        
         # self.driver.find_element(mobily_by.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("'+configReader.readConfig("locators", "el_workspace__ACCESSIBILITYID")+'"))').click()
        #self.driver.find_element(mobily_by.ACCESSIBILITY_ID, configReader.readConfig("locators", "el_workspace__ACCESSIBILITYID")).click()
        
        time.sleep(3)

    def openChrome(self):
        print(" turn on chrome")
        self.driver = self.driver.start_activity("com.android.chrome","org.chromium.chrome.browser.ChromeTabbedActivity")
        print("click email in top")
        self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", "el_top_email_BTN_XPATH")).click()
        print("click workspace")
        self.driver.find_element(mobily_by.ACCESSIBILITY_ID, configReader.readConfig("locators", "el_workspace__ACCESSIBILITYID")).click()
        print("click choose atato or chrome for deeplink")
        window_width = self.driver.get_window_size()["width"]
        window_height = self.driver.get_window_size()["height"]
        x = window_width * 0.75
        y = window_height * 0.875
        TouchAction(self.driver).tap(None,x, y).perform()
        TouchAction(self.driver).tap(None,x, y).perform()
        time.sleep(3)

    def sendkeyElPassword(self, password):
        self.type("el_password_XPATH", password)

    def clickElLogin(self):
        self.click("el_login_XPATH")

    def clickDoitlater(self):
        self.click("el_biometric_do_it_XPATH")

    def clickApproverDropdown(self):
        self.click("el_approver_dropdown_XPATH")
        
    def verify_walet(self):
       
        self.click("el_atato_requests_tab_XPATH")
        self.click("el_atato_request_wallet_XPATH")
        self.click("el_atato_aprrove_wallet_Btn_XPATH")
        window_width = self.driver.get_window_size()["width"]
        window_height = self.driver.get_window_size()["height"]
        x = window_width * 0.75
        y = window_height * 0.9
        TouchAction(self.driver).tap(None,x, y).perform()
        TouchAction(self.driver).tap(None,x, y).perform()
        print("x:",x, "y:", y)
        

    def clickScrollToTheApprover(self, label):
        self.clickScroll(label)

    def typeCodeApprover(self, code):
        self.type("el_approver_code_XPATH", code)

    def clickApproverActive(self):
        self.clicklongActive()
  
    def create_approver(self) :
            baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/approvers"
            inputData = {"name":"001 xyz'"+ RanDom.random_string_generator(5) +"'"}
            headers = {
                    "Content-Type": "application/json; charset=utf-8",
                    "Authorization": "Bearer " + ReadConfig.getBearToken()
                }
            response = requests.post(url=baseUrl,json=inputData,headers=headers )
            print("AAAAAAAAAAAAAAAa", response.text)
            responseJson = json.loads(response.text)
            self.approver_code = responseJson["data"]["activation_code"]
            self.approver_id = responseJson["data"]["approver_id"]
            a = {
                "approver_code": self.approver_code,
                "approver_id": self.approver_id,
                "rule_id": self.rule_id,
                "wallet_id": self.wallet_id,
                "approver_name": inputData
            }
            ReadJson.writetoafile(a)
            print("apruve code day nha em", self.approver_code)
            print("apruve id day nha em", self.approver_id)
            print("apruve name day nha em", inputData)
    
 
    def create_rule(self) :
            print(ReadJson.geinputData()["approver_id"])
            baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/rule-templates"
            inputData = {"name":"01 abc'"+RanDom.random_string_generator(5)+"'","network_id":"84703c2b-2c33-4ebf-b195-ab3ec8beda71","approvers":[ReadJson.geinputData()["approver_id"]],"conditions":[],"action":"send_to_approver","type":"transfer"}
            headers = {
                    "Content-Type": "application/json; charset=utf-8",
                    "Authorization": "Bearer " + ReadConfig.getBearToken()
                }
            response = requests.post(url=baseUrl,json=inputData,headers=headers )
            print("BBBBBBBBBBBBBa", response.text)
            responseJson = json.loads(response.text)
            self.rule_id = responseJson["data"]["id"]
            a = {
                "approver_code": ReadJson.geinputData()["approver_code"],
                "approver_id": ReadJson.geinputData()["approver_id"],
                "rule_id": self.rule_id,
                "wallet_id": self.wallet_id,
                "approver_name": ReadJson.geinputData()["approver_name"]
            }
            ReadJson.writetoafile(a)
            print("ruleid day nha em", self.rule_id)

 
    def create_walet(self) :
            print(ReadJson.geinputData()["approver_id"])
            baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/wallets"
            inputData = {"name":"1.abc rain'"+RanDom.random_string_generator(5)+"'","approvers":[ReadJson.geinputData()["approver_id"]],"description":"test rain '"+RanDom.random_string_generator(5)+"'","rules":[ReadJson.geinputData()["rule_id"]],"network_id":"84703c2b-2c33-4ebf-b195-ab3ec8beda71","is_mainnet":"false"}

            headers = {
                    "Content-Type": "application/json; charset=utf-8",
                    "Authorization": "Bearer " + ReadConfig.getBearToken()
                }
            response = requests.post(url=baseUrl,json=inputData,headers=headers )
            print("CCCCCCCCCCCCa", response.text)
            responseJson = json.loads(response.text)
            self.wallet_id = responseJson["data"]["id"]
            a = {
                "approver_code": ReadJson.geinputData()["approver_code"],
                "approver_id": ReadJson.geinputData()["approver_id"],
                "rule_id": ReadJson.geinputData()["rule_id"],
                "wallet_id": self.wallet_id,
                "approver_name": ReadJson.geinputData()["approver_name"]
            }
            ReadJson.writetoafile(a)
            print("ruleid day nha em", self.rule_id)

    def gotoTrains(self):
        pass

    def scroll_down_until(self, predicate, max_number_of_scrolls=2):
        screenSize = self.driver.get_window_size()
        screenHeight = screenSize['height']   
        scroll_distance = screenHeight / 2
        number_of_scrolls = 0
        while number_of_scrolls < max_number_of_scrolls:
            try:
                predicate()
                return self
            except Exception as err:
                self.scroll_down(distance=scroll_distance)
                number_of_scrolls += 1
                err_message = err
        else:
            pass

    def scroll_down(self, number_of_scrolls=1, distance=None, sleep_duration_before_scroll=5):
        time.sleep(3)
        screenSize = self.driver.get_window_size()
        screenHeight = screenSize['height']  
        for _ in range(number_of_scrolls):
            scroll_distance = distance if distance is not None else screenHeight
            TouchAction(self.driver).long_press(x=0, y=screenHeight-10).move_to(
                x=0, y=max(screenHeight - scroll_distance, 0)
            ).release().perform()
            time.sleep(3)
        return self
    

    def wait_until_visible_by(self, locator: By, key, timeout_duration=30):
        start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            return wwait(self.driver, timeout_duration).until(
                EC.visibility_of_element_located((locator, key)), "Not found " + key
            )
        except:
            raise

    def click_by_ratio(self, window_width, window_height, rx, ry):
        x = window_width * rx
        y = window_height * ry
        TouchAction(self.driver).tap(None,x, y).perform()