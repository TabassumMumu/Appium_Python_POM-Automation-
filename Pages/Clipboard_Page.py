from appium.webdriver.common.appiumby import AppiumBy
from .Base_Page import BasePage

class ClipboardPage(BasePage):
    MESSAGE_INPUT = (AppiumBy.ACCESSIBILITY_ID, "messageInput")
    SET_CLIPBOARD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Set Clipboard Text")')
    REFRESH_CLIPBOARD_TEXT = (AppiumBy.XPATH, '//android.widget.TextView[@text="Refresh Clipboard Text"]')
    REFRESH_BTN = (AppiumBy.ACCESSIBILITY_ID, "refreshClipboardText")
    NAVIGATE_UP = (AppiumBy.ACCESSIBILITY_ID, "Navigate Up")

    def enter_message(self, msg):
        self.type_text(self.MESSAGE_INPUT, msg)

    def set_clipboard_text(self):
        self.click(self.SET_CLIPBOARD)

    def refresh_clipboard_text(self):
        self.click(self.REFRESH_CLIPBOARD_TEXT)

    def refresh_button(self):
        self.click(self.REFRESH_BTN)

    def go_back(self):
        self.click(self.NAVIGATE_UP)
