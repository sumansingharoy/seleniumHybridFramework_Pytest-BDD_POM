# Load the feature file
from pytest_bdd import given, scenario, then, when
from pytest_bdd.parsers import cfparse
from testFolder.project.tutorialDemo.functionalSupport.accountPage import AccountPage
from testFolder.project.tutorialDemo.functionalSupport.homePage import HomePage
from testFolder.project.tutorialDemo.functionalSupport.loginPage import LoginPage



@scenario('../features/login.feature', 'Login with valid email and valid password')
def test_loginWith_ValidEmailPassword():
    pass

@scenario('../features/login.feature', 'Login with invalid email and valid password')
def test_loginWith_InvalidEmail_ValidPassword():
    pass

@scenario('../features/login.feature', 'Login with valid email and invalid password')
def test_loginWith_ValidEmail_InvalidPassword():
    pass

@scenario('../features/login.feature', 'Login with invalid credentials')
def test_loginWith_Invalid_Credentials():
    pass

@scenario('../features/login.feature', 'Login without entering any credentials')
def test_loginWithout_Credentials():
    pass
# ------------------Given--------------------
@given("I navigated to Login page")
def open_login_page(browser):
    homepage =HomePage(browser)
    homepage.click_on_my_account_option()
    homepage.click_on_login_option()

# ------------------When--------------------
@when(cfparse('I enter valid email as "{email}" and valid password as "{password}" into the fields'))
def enter_valid_credentials(browser, email, password):
    loginpage = LoginPage(browser)
    loginpage.enter_email_address(email)
    loginpage.enter_password_field(password)

@when("I enter invalid email and valid password into the fields")
def enter_invalid_email(browser):
    loginpage = LoginPage(browser)
    loginpage.enter_email_address("sumannnnn@gmail.com")
    loginpage.enter_password_field("123456")

@when("I enter valid email and invalid password into the fields")
def enter_invalid_password(browser):
    loginpage = LoginPage(browser)
    loginpage.enter_email_address("suman1234roy@gmail.com")
    loginpage.enter_password_field("123456")

@when("I enter invalid email and invalid password into the fields")
def enter_both_invalid(browser):
    loginpage = LoginPage(browser)
    loginpage.enter_email_address("sumannnnnn1234roy@gmail.com")
    loginpage.enter_password_field("123456xysss")

@when("I dont enter anything into email and password fields")
def leave_credentials_blank(browser):
    loginpage = LoginPage(browser)
    loginpage.enter_email_address("")
    loginpage.enter_password_field("")

@when("I click on Login button")
def click_login_button(browser):
    loginpage = LoginPage(browser)
    loginpage.click_on_login_button()

# ----------------------- Then ---------------------

@then("I should get logged in")
def should_login_successfully(browser):
    accountpage = AccountPage(browser)
    accountpage.display_if_logged_in_successfully()

@then("I should get a proper warning message")
def should_get_warning(browser):
    loginpage = LoginPage(browser)
    loginpage.validate_expected_warning_msg("Warning: No match for E-Mail Address and/or Password.")
