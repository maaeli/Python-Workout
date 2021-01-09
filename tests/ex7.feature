@demo
Feature: Turn a word into Ubbi Dubbi
  As a kid,
  I want to speak ubbi dubbi,
  so that my parents cannot understand me.

  Scenario Outline: one word
    Given <word>
    When I transform the word <word> into ubbi dubbi
    Then I obtain <ubbidubbi>

      Examples:
      | word | ubbidubbi |
      |  milk |  mubilk  |
      |  program | prubogrubam |
      | octopus | uboctubopubus |
      | elephant | ubelubephubant |
