Feature: Add items flow
As QA Engineer,
I would like to ensure that users can successfully add items to their shopping cart
To ensure flow for adding items isn't broken

Scenario: Verify user can successfully add items to their shopping cart
  Given I am on the Amazon homepage
  And I search for any item
  And I add to my cart
  When I navigate to my cart
  Then I see the correct item in my car
