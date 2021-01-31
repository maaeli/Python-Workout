@demo
Feature: Sort a list of address dicts by last name

  Scenario: GW and Vlad
    Given the address book [{'first': 'Reuven', 'last': 'Lerner', 'email': 'lerner'}, {'first': 'Donald', 'last': 'Trump', 'email': 'trump'},{'first': 'Vladimir', 'last': 'Putin', 'email': 'putin'}]
    When I sort it by last name
    Then I obtain [{'first': 'Reuven', 'last': 'Lerner', 'email': 'lerner'}, {'first': 'Vladimir', 'last': 'Putin', 'email': 'putin'}, {'first': 'Donald', 'last': 'Trump', 'email': 'trump'}]
