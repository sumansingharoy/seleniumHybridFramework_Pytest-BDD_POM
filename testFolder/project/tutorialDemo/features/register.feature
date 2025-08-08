@register
Feature: Register Account functionality

  @registerWith_mandatory_Fields
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter details into mandatory fields
    And I click on Continue button
    Then Account should get created

  @registerWith_All_fields
  Scenario: Register with all fields
    Given I navigate to Register Page
    When I enter details into all fields
    And I click on Continue button
    Then Account should get created

  @registerWith_duplicate_email
  Scenario: Register with a duplicate email address
    Given I navigate to Register Page
    When I enter details into all fields except email field
    And I enter existing account's email into email field
    And I click on Continue button
    Then I should get a proper warning message for duplicate email

  @registerWithout_Any_details
  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I do not enter any details into any of the fields
    And I click on Continue button
    Then I should get a proper warning messages for all the required fields