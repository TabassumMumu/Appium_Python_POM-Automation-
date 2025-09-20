from appium.webdriver.common.appiumby import AppiumBy
from .Base_Page import BasePage

class PickerPage(BasePage):
    MONTH_PICKER = (AppiumBy.ACCESSIBILITY_ID, "monthPicker")
    DAY_PICKER = (AppiumBy.ACCESSIBILITY_ID, "dayPicker")
    LEARN_MORE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Learn More")')

    def select_month(self, month_name):
        self.click(self.MONTH_PICKER)
        self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{month_name}")'))

    def select_day(self, day_num):
        self.click(self.DAY_PICKER)
        self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{day_num}")'))


