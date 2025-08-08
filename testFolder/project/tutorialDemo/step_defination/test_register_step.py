
from pytest_bdd import given, scenario, then, when

from testFolder.project.tutorialDemo.functionalSupport import homePage
from testFolder.project.tutorialDemo.functionalSupport.accountSuccessPage import AccountSuccessPage
from testFolder.project.tutorialDemo.functionalSupport.homePage import HomePage
from testFolder.project.tutorialDemo.functionalSupport.registerPage import RegisterPage


@scenario('../features/register.feature', 'Register with mandatory fields')
def test_Register_with_mandatory_fields():
    pass

@scenario('../features/register.feature', 'Register with all fields')
def test_Register_with_all_fields():
    pass

@scenario('../features/register.feature', 'Register with a duplicate email address')
def test_Register_with_duplicate_email():
    pass

@scenario('../features/register.feature', 'Register without providing any details')
def test_Register_without_any_details():
    pass

# -------------------Given------------------------------

@given("I navigate to Register Page")
def open_register_page(browser):
    homePage = HomePage(browser)
    homePage.click_on_my_account_option()
    homePage.click_on_register_option()

# ------------------When---------------------------------

@when("I enter details into mandatory fields")
def enter_mandatory_fields(browser):
    registerPage = RegisterPage(browser)
    registerPage.enter_firstName("Sum")
    registerPage.enter_lastName("Roy")
    registerPage.enter_emailId(registerPage.generate_new_email_address())
    registerPage.enter_Telephone_Number("987654321")
    registerPage.enter_password("12345")
    registerPage.enter_confirm_password("12345")
    registerPage.click_on_agree_checkbox()

@when("I enter details into all fields")
def enter_all_fields(browser):
    registerPage = RegisterPage(browser)
    registerPage.enter_firstName("Sum")
    registerPage.enter_lastName("Roy")
    registerPage.enter_emailId(registerPage.generate_new_email_address())
    registerPage.enter_Telephone_Number("9876543210")
    registerPage.enter_password("1234567")
    registerPage.enter_confirm_password("1234567")
    registerPage.click_on_newsletter_checkbox()
    registerPage.click_on_agree_checkbox()

@when("I enter details into all fields except email field")
def enter_details_except_emailId(browser):
    registerPage = RegisterPage(browser)
    registerPage.enter_firstName("Sum")
    registerPage.enter_lastName("Roy")
    registerPage.enter_Telephone_Number("9876543210")
    registerPage.enter_password("1234567")
    registerPage.enter_confirm_password("1234567")
    registerPage.click_on_newsletter_checkbox()
    registerPage.click_on_agree_checkbox()

@when("I do not enter any details into any of the fields")
def doNot_enter_any_details(browser):
    registerPage = RegisterPage(browser)
    registerPage.enter_firstName("")
    registerPage.enter_lastName("")
    registerPage.enter_emailId("")
    registerPage.enter_Telephone_Number("")
    registerPage.enter_password("")
    registerPage.enter_confirm_password("")

@when("I enter existing account's email into email field")
def enter_existing_emailId(browser):
    registerPage = RegisterPage(browser)
    registerPage.enter_emailId("suman1234roy@gmail.com")

@when("I click on Continue button")
def click_submit_button(browser):
    registerPage = RegisterPage(browser)
    registerPage.click_on_continue_button()

# ----------------------- Then ------------------------

@then("Account should get created")
def account_created_successfully(browser):
    accountSuccessPage = AccountSuccessPage(browser)
    accountSuccessPage.display_successful_account_creation_msg()

@then("I should get a proper warning message for duplicate email")
def display_proper_warning_msg_duplicate_emailId(browser):
    registerPage = RegisterPage(browser)
    registerPage.validate_warning_msg_for_duplicate_email()

@then("I should get a proper warning messages for all the required fields")
def display_proper_warning_msg_AllRequiredFields(browser):
    registerPage = RegisterPage(browser)
    registerPage.validate_expected_privacy_policy_warning_msg()
    registerPage.validate_expected_first_name_warning_msg()
    registerPage.validate_expected_last_name_warning_msg()
    registerPage.validate_expected_email_id_warning_msg()
    registerPage.validate_expected_input_telephone_warning_msg()
    registerPage.validate_expected_input_password_warning_msg()
