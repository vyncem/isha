Feature: Pull session stats from Eventbrite
  As an moderator
  I want to eventbrite users: registered, atteneded and missed
  So that I note anonymous attendance stats and send thank/missed you emails


Scenario: Moderator pulls Eventbrite session stats
  Given I'm a moderator
  When I pull eventbrite stats
  Then I get valid stats
