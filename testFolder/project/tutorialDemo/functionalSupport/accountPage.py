from attr import dataclass
from selenium.webdriver.common.by import By

from testFolder.util.userAction import UserAction

@dataclass
class Element:
    account_info_link_text =(By.LINK_TEXT, "Edit your account information") 

class AccountPage(UserAction):

    def __init__(self, browser):
        super().__init__(browser)

    

    def display_if_logged_in_successfully(self):
        return self.is_product_link_visible(Element.account_info_link_text)