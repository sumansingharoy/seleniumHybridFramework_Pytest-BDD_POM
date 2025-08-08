@login
Feature: Login Functionality Validation

    @loginWith_Valid_Credentials
    Scenario Outline: Login with valid email and valid password
      Given I navigated to Login page
      When I enter valid email as "<email>" and valid password as "<password>" into the fields
      And I click on Login button
      Then I should get logged in
      Examples:
      |email                  |password   |
      |suman1234roy@gmail.com |suman@1234 |
      |sumroy10@gmail.com     |sumroy1234 |

    @loginWith_InvalidEmail_ValidPassword
    Scenario: Login with invalid email and valid password
      Given I navigated to Login page
      When I enter invalid email and valid password into the fields
      And I click on Login button
      Then I should get a proper warning message

    @loginWith_ValidEmail_InvalidPassword
    Scenario: Login with valid email and invalid password
      Given I navigated to Login page
      When I enter valid email and invalid password into the fields
      And I click on Login button
      Then I should get a proper warning message

    @loginWith_Invalid_Credentials
    Scenario: Login with invalid credentials
      Given I navigated to Login page
      When I enter invalid email and invalid password into the fields
      And I click on Login button
      Then I should get a proper warning message

    @loginWithout_Credentials
    Scenario: Login without entering any credentials
      Given I navigated to Login page
      When I dont enter anything into email and password fields
      And I click on Login button
      Then I should get a proper warning message
