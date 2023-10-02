import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    sauce_url = "http://127.0.0.1:4723/wd/hub"
    sauce_urls = "https://vvnthnh_9WyXp6:tGmRqWRRiq9HpDWsWczb@hub-cloud.browserstack.com/wd/hub"
    # sauce_urls = "https://interviewsavvyco_Fs7grm:7ayC9S7npyZkBy7Ysoen@hub-cloud.browserstack.com/wd/hub"
    desired_cap = {
            'autoGrantPermissions': True,
            'platformName': 'Android',
            'deviceName': 'R58T41DCNEE',
            'deviceOrientation': 'portrait',
            'app': 'C:\\Users\\vuvan\\OneDrive\\Desktop\\crypto\\atato\\adap-autotest-android\\ConfigurationData\\atato.apk',
            'appPackage': 'com.atato.custody.qa',
            'appActivity': 'com.atato.custody.MainActivity',
            'appWaitActivity': 'com.atato.custody.MainActivity',
            'full-reset': True
        }
    desired_caps = {
            "platformName": "android",
            "platformVersion": "10.0",
            "deviceName": "Samsung Galaxy A11",
            "app": "bs://b23169ef6b214a499367805b948dea0d7911d49b", #bs://d9f37a6680e3ee176b6e2d837365af18fd2f58c2
            "bstack:options": {
                "projectName": "test atato",
                "appiumVersion": "1.18.0",
                "acceptInsecureCerts": "true",
                "enableBiometric" : "true",
                "enablePasscode" : "true",
                "enableCameraImageInjection" : "true",
            },
        }
    desired_caps_ios = {
        "appium:app": "/Users/thanhvuvan/Documents/project/adap-autotest-android/ConfigurationData/qa.ipa",
        "platformName": "iOS",
        "appium:platformVersion": "15.6",
        "appium:deviceName": "iPhone của Thành",
        "appium:automationName": "XCUITest",
        "appium:xcodeSigningId": "iPhone Developer",
        "appium:bundleId": "com.atato.custody.qa",
        "appium:udid": "00008030-0010458934F8202E",
        "appium:noReset": "true",
        "appium:xcodeOrgId": "Atato Pte Ltd"
        }
    desired_caps_ioss = {
        "platformName": "iOS",
        "platformVersion": "15",
        "deviceName": "iPhone 11",
        "automationName": "XCUITest",
        "browserstack.enableBiometric" : "true",
        "browserstack.enableCameraImageInjection" : "true",
        "app": "bs://536125a2e2c46483319a2666f9b12bffa300280a"
    }
    driver = webdriver.Remote(sauce_urls, desired_caps) # this for browserstack test
    
    # driver = webdriver.Remote(sauce_url, desired_cap) # this for appium test
    # driver = webdriver.Remote(sauce_url, desired_caps_ios) # this for ios appium test
    # driver = webdriver.Remote(sauce_urls, desired_caps_ioss) # this for ios browserstack test\
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Opencart'
#     config._metadata['Module Name'] = 'CustRegistration'
#     config._metadata['Tester'] = 'Pavan'
#     config.option.htmlpath = "..\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
    
@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
