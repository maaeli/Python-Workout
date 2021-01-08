@demo
Feature: Render sentence in pig latin
  As a kid,
  I want to speak pig latin,
  so that my parents cannot understand me.

  Scenario Outline: Word starts with a vowel
    Given <word>
    When I transform the word <word> into piglatin
    Then I obtain <latin>

      Examples:
      | word | latin |
      |  a |  away  |
      | icon | iconway |

  Scenario Outline: Word starts with a consonant
    Given <word>
    When I transform the word <word> into piglatin
    Then I obtain <latin>

      Examples:
      | word | latin |
      | python |  ythonpay  |
      | computer | omputercay |

  Scenario Outline: Whole sentence
    Given <sentence>
    When I transform the sentence <sentence> into piglatin
    Then I obtain <latin>

      Examples:
      | sentence | latin |
      | this is a test translation |  histay isway away esttay ranslationtay |
