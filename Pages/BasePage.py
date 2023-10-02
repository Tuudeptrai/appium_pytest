import logging

from Utilities import configReader
from appium.webdriver.common.mobileby import MobileBy as mobily_by
from appium.webdriver.common.touch_action import TouchAction



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(mobily_by.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).click()
            print("Clicking on an Element "+ str(locator))
    
    def clickScroll(self,label):
        
        # el = self.driver.find_element(mobily_by.XPATH,configReader.readConfig("locators", locator))
        el = self.driver.find_element(mobily_by.XPATH,f'//*[@text="{label["name"]}"]')
        if(el):
            el.click()
            el.click()
            el.click()
            # size = el.size
            # w, h = size['width'], size['height']
            # window_width = self.driver.get_window_size()["width"]
            # window_height = self.driver.get_window_size()["height"]
            # x = window_width * 0.5
            # y = window_height * 0.53125
            # print("Clicking on an Element: -->size")
            # print(size)
            TouchAction(self.driver).tap(el).perform()
            TouchAction(self.driver).tap(el).perform()
            TouchAction(self.driver).tap(el).perform()

    
    def clicklongActive(self):
        el = self.driver.find_element(mobily_by.XPATH,f'//*[@text="Activate"]')
        el.click()
        # el.click()
        

   
    def clickIndex(self, locator, index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements_by_xpath(configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_elements_by_accessibility_id(configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements_by_id(configReader.readConfig("locators", locator))[index].click()
        print("Clicking on an Element "+ str(locator) + "with index : " + str(index))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).send_keys(value)
        print("Typing in an Element "+ str(locator)+ " entered the value as : "+ str(value))
    
    def getText(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element_by_id(configReader.readConfig("locators", locator)).text
        print("Getting text from an element "+ str(locator))
        return text
    def get_element_wait(self, locator):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
