import allure
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selene import browser
from settings import config
from utils import attach


@pytest.fixture
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": "bs://sample.app",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": config.user_name,
            "accessKey": config.access_key
        }
    })
    browser.config.driver = webdriver.Remote(config.remote_url, options=options)
    yield
    attach.attach_screenshot()
    session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

    attach.attach_bstack_video(session_id)


@pytest.fixture
def mobile_management_ios():
    options = XCUITestOptions().load_capabilities({
        "app": "bs://sample.app",
        "deviceName": "iPhone 11 Pro",
        "platformName": "ios",
        "platformVersion": "13",
        "bstack:options": {
            "userName": config.user_name,
            "accessKey": config.access_key,
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test"
        }
    })
    browser.config.driver = webdriver.Remote(config.remote_url, options=options)
    yield
    attach.attach_screenshot()
    session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

    attach.attach_bstack_video(session_id)
