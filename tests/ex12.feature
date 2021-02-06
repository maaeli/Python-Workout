@demo
Feature: Sort a list of address dicts by last name

Scenario Outline: Create dic of letter ocurences in a word
  Given <word>
  When I count the letters in <word>
  Then I obtain the <dic>

    Examples:
    | word | dic |
    |  aa |  {'a': 2}  |
    |  ab | {'a': 1, 'b': 1} |
    | aba | {'a': 2, 'b': 1} |

  Scenario: Empty string
    Given an empty string
    When I count the letters in the empty string
    Then I obtain an empty dic

@demo
Feature: Get the word with most repeated letters

  Scenario: Posed problem
  Given the list of strings ['this', 'is', 'an', 'elementary', 'test', 'example']
  When I request the word with the most repeated letters
  Then I obtain 'elementary'
