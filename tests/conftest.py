import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
import os


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
            "userName": "bsuser_z1ABvm",
            "accessKey": "V8XbR7NPHDoqWp9LiejD"
        }
    })
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    yield
    browser.quit()


@pytest.fixture
def mobile_management_ios():
    options = XCUITestOptions().load_capabilities({
        "app": "bs://sample.app",
        "deviceName": "iPhone 11 Pro",
        "platformName": "ios",
        "platformVersion": "13",
        "bstack:options": {
            "userName": "bsuser_z1ABvm",
            "accessKey": "V8XbR7NPHDoqWp9LiejD",
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test"
        }
    })
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    yield
    browser.quit()
