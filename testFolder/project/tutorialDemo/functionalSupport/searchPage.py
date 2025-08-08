from attr import dataclass
from selenium.webdriver.common.by import By

from testFolder.util.userAction import UserAction


@dataclass
class Element:
    product_name_link_text =(By.LINK_TEXT, "HP LP3065") 
    proper_error_msg_xpath =(By.XPATH, "//input[@id='button-search']/following-sibling::p")


class SearchPage(UserAction):

    def __init__(self, browser):
        super().__init__(browser)

    
    def verify_valid_product_name(self):
        return self.is_product_link_visible(Element.product_name_link_text)

    def verify_proper_error_msg(self, expected_text):
        return self.getText(Element.proper_error_msg_xpath).__eq__(expected_text)
