from attr import dataclass
from selenium.webdriver.common.by import By

from testFolder.project.tutorialDemo.functionalSupport.loginPage import LoginPage
from testFolder.project.tutorialDemo.functionalSupport.registerPage import RegisterPage
from testFolder.project.tutorialDemo.functionalSupport.searchPage import SearchPage
from testFolder.util.userAction import UserAction


@dataclass
class Element:

    my_account_option_xpath =(By.XPATH, "//span[text()='My Account']")
    login_link_text =(By.LINK_TEXT, "Login") 
    register_link_text =(By.LINK_TEXT, "Register") 
    search_field_name =(By.NAME, "search") 
    search_button_xpath =(By.XPATH, "//div[@id='search']//button") 

class HomePage(UserAction):

    def __init__(self, browser):
        super().__init__(browser)

    

    def click_on_my_account_option(self):
        self.click(Element.my_account_option_xpath)

    def click_on_login_option(self):
        self.click(Element.login_link_text)
        return LoginPage(self.browser)

    def click_on_register_option(self):
        self.click(Element.register_link_text)
        return RegisterPage(self.browser)

    def verify_page_title(self, Expected_title):
        return self.getTitle().__eq__(Expected_title)

    def click_on_search_box(self):
        self.click(Element.search_field_name)

    def enter_search_item_name(self, Item_Name):
        self.sendKeys(Element.search_field_name, Item_Name)

    def click_operation_on_search_button(self):
        self.click(Element.search_button_xpath)
        return SearchPage(self.browser)





