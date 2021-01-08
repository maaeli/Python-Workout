@demo
Feature: Average my runs times
  As a runner,
  I want calculate how long it takes me to run 10 km,
  so that I can compare myself to the rest of the world.

  Scenario: 3 different runs
    Given the program is running
    When I enter 1, 2, 3 ENTER
    Then The text "Average of 2.0 over 3 runs" is displayed
