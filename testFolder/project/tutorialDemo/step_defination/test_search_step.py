from pytest_bdd import given, when, then, scenario, parsers
import pytest
from testFolder.conftest import browser
from pytest_bdd.parsers import cfparse
from testFolder.project.tutorialDemo.functionalSupport.homePage import HomePage
from testFolder.project.tutorialDemo.functionalSupport.searchPage import SearchPage

# Load the feature file
@scenario('../features/search.feature', 'Search with a valid product')
def test_searchValidProduct():
    pass

@scenario('../features/search.feature', 'Search with an invalid product')
def test_searchInvalidProduct():
    pass


# Assuming Page Objects are used



@given("User is on the Home page of the application")
def user_on_homepage(browser):
    homepage = HomePage(browser)
    homepage.verify_page_title("Your Store")


@when(cfparse('User enters "{product}" in the search box'))
def enter_product_in_search(browser, product):
    homepage = HomePage(browser)
    homepage.enter_search_item_name(product)


@when("clicked on search button")
def click_search_button(browser):
    homepage = HomePage(browser)
    homepage.click_operation_on_search_button()


@then("Valid Product should be displayed in search result page")
def validate_valid_product_result(browser):
    search_page = SearchPage(browser)
    assert search_page.verify_valid_product_name()


@then("Proper message should be displayed")
def validate_invalid_search_result(browser):
    search_page = SearchPage(browser)
    assert search_page.verify_proper_error_msg("There is no product that matches the search criteria.")
