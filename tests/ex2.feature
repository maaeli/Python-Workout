@backend
Feature: A simple sum function
  As a user,
  I want calculate the sum of all elements in my list,
  so that I can proceed to calculate the mean.

  Scenario: Easy sum
    Given random integers
    When I calculate my sum
    Then I obtain the same result as the built-in

  Scenario: Empty sum
    Given no arguments
    When I calculate my sum
    Then I obtain 0 
