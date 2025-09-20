from appium.webdriver.common.appiumby import AppiumBy
from .Base_Page import BasePage

class HomePage(BasePage):
    CLIPBOARD_DEMO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Clipboard Demo")')
    LIST_DEMO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("List Demo")')
    PICKER_DEMO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Picker Demo")')

    def go_to_clipboard_demo(self):
        self.click(self.CLIPBOARD_DEMO)

    def go_to_list_demo(self):
        self.click(self.LIST_DEMO)

    def go_to_picker_demo(self):
        self.click(self.PICKER_DEMO)
