@search
Feature: Search Feature

  @searchValid
  Scenario Outline: Search with a valid product
    Given User is on the Home page of the application
    When User enters "<valid_product>" in the search box
    And clicked on search button
    Then Valid Product should be displayed in search result page

    Examples:
      | valid_product |
      | HP            |


  @searchInvalid
  Scenario Outline: Search with an invalid product
    Given User is on the Home page of the application
    When User enters "<invalid_product>" in the search box
    And clicked on search button
    Then Proper message should be displayed

    Examples:
      | invalid_product |
      | Honda         |
      | abcd!@#         |
