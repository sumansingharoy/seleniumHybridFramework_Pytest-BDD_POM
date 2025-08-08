from attr import dataclass
from selenium.webdriver.common.by import By

from testFolder.project.tutorialDemo.functionalSupport.accountPage import AccountPage
from testFolder.util.userAction import UserAction


@dataclass
class Element:

    input_email_address_id =(By.ID, "input-email") 
    input_password_field_id =(By.ID, "input-password")
    login_button_xpath =(By.XPATH, "//input[@value='Login']")
    expected_warning_msg_xpath =(By.XPATH, "//div[contains(@class,'alert-dismissible')]")

class LoginPage(UserAction):

    def __init__(self, browser):
        super().__init__(browser)

    

    def enter_email_address(self, email_text):
        self.sendKeys(Element.input_email_address_id, email_text)

    def enter_password_field(self, password_text):
        self.sendKeys(Element.input_password_field_id, password_text)

    def click_on_login_button(self):
        self.click(Element.login_button_xpath)
        return AccountPage(self.browser)

    def validate_expected_warning_msg(self, Expected_warning_msg):
        return self.getText(Element.expected_warning_msg_xpath).__eq__(
            Expected_warning_msg)
