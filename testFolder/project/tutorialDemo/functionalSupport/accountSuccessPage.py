from attr import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from testFolder.util.userAction import UserAction

@dataclass
class Element:
    
    successful_account_creation_msg_xpath =(By.XPATH, "//div[@id='content']/h1")

class AccountSuccessPage(UserAction):

    def __init__(self, browser):
        super().__init__(browser)

    

    def display_successful_account_creation_msg(self):
        return self.getText(Element.successful_account_creation_msg_xpath).__eq__("Your Account Has Been Created!")
