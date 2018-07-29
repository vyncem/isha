Feature: Email attendees
  As an moderator
  I want to email attendees
  So that I thank them


Scenario: Moderator emais eventbrite attendees
  Given I'm a moderator
  When I email attendees
  Then I get a receipt
