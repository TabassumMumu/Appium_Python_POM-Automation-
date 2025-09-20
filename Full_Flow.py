import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.Home_Page import HomePage
from Pages.Clipboard_Page import ClipboardPage
from Pages.List_Page import ListPage
from Pages.Picker_Page import PickerPage

def test_full_app_flow(driver):
    home = HomePage(driver)

    # Clipboard Demo
    home.go_to_clipboard_demo()
    clipboard = ClipboardPage(driver)
    clipboard.enter_message("MY Text Message One")
    clipboard.set_clipboard_text()
    clipboard.refresh_clipboard_text()
    clipboard.enter_message("New Replaced Text Message")
    clipboard.set_clipboard_text()
    clipboard.refresh_button()
    clipboard.go_back()

    # List Demo
    home.go_to_list_demo()
    list_page = ListPage(driver)
    list_page.select_cirrocumulus()
    list_page.select_cumulus_humilis()
    list_page.go_back()

    # Picker Demo
    home.go_to_picker_demo()
    picker = PickerPage(driver)
    picker.select_month("July")
    picker.select_day("7")
    picker.select_month("October")
    picker.select_day("16")

    # pytest -v -s -k Full_Flow.py --alluredir="./allurereport/"
    allure.attach(driver.get_screenshot_as_png(), name= "alert message", attachment_type = AttachmentType.PNG)