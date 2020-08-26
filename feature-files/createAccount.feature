Feature: Create Account flow
As QA Engineer,
I would like to ensure that users can successfully create a new account
To ensure the create account flow works properly

Scenario: Verify user created a new account successfully
  Given I am on the Amazon homepage
  And I click on the \d+ link
  And I am on the \d+ page
  And I enter valid user information
  And I successfully go through verify email flow
  When I click on Create Your Amazon Account
  Then I have successfully created my account