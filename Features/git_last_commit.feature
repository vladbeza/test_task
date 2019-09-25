Feature: Git last commit

Scenario: Last commit on django main page
    Given I have number of last commit on commits git django page
    When I open main git django page
    Then Number of commit in header is the same as number of last commit