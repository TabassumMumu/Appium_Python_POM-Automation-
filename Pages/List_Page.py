from appium.webdriver.common.appiumby import AppiumBy
from .Base_Page import BasePage

class ListPage(BasePage):
    CIRROCUMULUS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cirrocumulus")')
    CUMULUS_HUMILIS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cumulus humilis")')
    OK_BUTTON = (AppiumBy.ID, "android:id/button1")
    NAVIGATE_UP = (AppiumBy.ACCESSIBILITY_ID, "Navigate Up")

    def select_cirrocumulus(self):
        self.click(self.CIRROCUMULUS)
        self.click(self.OK_BUTTON)

    def select_cumulus_humilis(self):
        self.click(self.CUMULUS_HUMILIS)
        self.click(self.OK_BUTTON)

    def go_back(self):
        self.click(self.NAVIGATE_UP)
