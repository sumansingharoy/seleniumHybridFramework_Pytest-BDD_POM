from datetime import datetime
from attr import dataclass
from selenium.webdriver.common.by import By

from testFolder.project.tutorialDemo.functionalSupport.accountSuccessPage import AccountSuccessPage
from testFolder.util.userAction import UserAction

@dataclass
class Element:

    first_name_id =(By.ID, "input-firstname") 
    last_name_id =(By.ID, "input-lastname") 
    email_id =(By.ID, "input-email") 
    telephone_number_id =(By.ID, "input-telephone") 
    input_password_id =(By.ID, "input-password") 
    confirm_password_id =(By.ID, "input-confirm") 
    agree_checkbox_name =(By.NAME, "agree") 
    continue_button_xpath =(By.XPATH, "//input[@value='Continue']") 
    newsletter_checkbox_xpath =(By.XPATH, "//input[@name='newsletter'][@value=1]") 
    proper_warning_msg_xpath =(By.XPATH, "//div[@id='account-register']/div[1]") 
    expected_privacy_policy_warning_msg_xpath =(By.XPATH, "//div[@id='account-register']/div[1]") 
    expected_first_name_warning_msg_xpath =(By.XPATH, "//input[@id='input-firstname']/following-sibling::div") 
    expected_last_name_warning_msg_xpath =(By.XPATH, "//input[@id='input-lastname']/following-sibling::div") 
    expected_email_id_warning_msg_xpath =(By.XPATH, "//input[@id='input-email']/following-sibling::div") 
    expected_input_telephone_warning_msg_xpath =(By.XPATH, "//input[@id='input-telephone']/following-sibling::div") 
    expected_input_password_warning_msg_xpath =(By.XPATH, "//input[@id='input-password']/following-sibling::div") 



class RegisterPage(UserAction):

    def __init__(self, browser):
        super().__init__(browser)

    

    def enter_firstName(self, first_name):
        self.sendKeys(Element.first_name_id, first_name)

    def enter_lastName(self, last_name):
        self.sendKeys(Element.last_name_id, last_name)

    def enter_emailId(self, email_text):
        self.sendKeys(Element.email_id, email_text)

    def enter_Telephone_Number(self, TelNo):
        self.sendKeys(Element.telephone_number_id, TelNo)

    def enter_password(self, input_password):
        self.sendKeys(Element.input_password_id, input_password)

    def enter_confirm_password(self, input_confirm_password):
        self.sendKeys(Element.confirm_password_id, input_confirm_password)

    def click_on_agree_checkbox(self):
        self.click(Element.agree_checkbox_name)

    def click_on_continue_button(self):
        self.click(Element.continue_button_xpath)
        return AccountSuccessPage(self.browser)

    def click_on_newsletter_checkbox(self):
        self.click(Element.newsletter_checkbox_xpath)

    def validate_warning_msg_for_duplicate_email(self):
        return self.getText(Element.proper_warning_msg_xpath).__contains__("Warning: E-Mail Address is already registered!")

    def validate_expected_privacy_policy_warning_msg(self):
        return self.getText(Element.expected_privacy_policy_warning_msg_xpath).__contains__("Warning: You must agree to the Privacy Policy!")

    def validate_expected_first_name_warning_msg(self):
        return self.getText(Element.expected_first_name_warning_msg_xpath).__contains__("First Name must be between 1 and 32 characters!")

    def validate_expected_last_name_warning_msg(self):
        return self.getText(Element.expected_last_name_warning_msg_xpath).__contains__("Last Name must be between 1 and 32 characters!")

    def validate_expected_email_id_warning_msg(self):
        return self.getText(Element.expected_email_id_warning_msg_xpath).__contains__("E-Mail Address does not appear to be valid!")

    def validate_expected_input_telephone_warning_msg(self):
        return self.getText(Element.expected_input_telephone_warning_msg_xpath).__contains__("Telephone must be between 3 and 32 characters!")

    def validate_expected_input_password_warning_msg(self):
        return self.getText(Element.expected_input_password_warning_msg_xpath).__contains__("Password must be between 4 and 20 characters!")

    def generate_new_email_address(self):
        now = datetime.now()
        time_str = now.strftime("%Y_%m_%d_%H_%M_%S")
        return "ssr1" + time_str + "@gmail.com"



