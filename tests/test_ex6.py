import pytest

from pytest_bdd import scenarios, given, when, then, parsers, scenario

from exercise6 import word_to_pig_latin, sentence_to_pig_latin


# Scenarions
scenarios("ex6.feature")

# Fixtures


@scenario(
    "ex6.feature",
    "Word starts with a vowel",
    example_converters=dict(word=str, latin=str)
)
def test_vowel():
    pass

@scenario(
    "ex6.feature",
    "Word starts with a consonant",
    example_converters=dict(word=str, latin=str)
)
def test_consonant():
    pass

@scenario(
    "ex6.feature",
    "Whole sentence",
    example_converters=dict(sentence=str, latin=str)
)
def test_sentence():
    pass

# Given Steps
@given("<word>", target_fixture="function_output")
def start_single_word(word):
    """Prepare dict for output"""
    assert isinstance(word, str)
    return dict(word=word)

@given("<sentence>", target_fixture="function_output")
def start_sentence(sentence):
    """Prepare dict for output"""
    assert isinstance(sentence, str)
    return dict(sentence=sentence)


# When Steps
@when("I transform the word <word> into piglatin")
def transform_single_word(function_output, word):
    assert isinstance(word, str)
    function_output["latin"] = word_to_pig_latin(word)

# When Steps
@when("I transform the sentence <sentence> into piglatin")
def transform_single_word(function_output, sentence):
    assert isinstance(sentence, str)
    function_output["latin"] = sentence_to_pig_latin(sentence)

# Then Steps
@then("I obtain <latin>")
def pig_ouptput_matches_expected(function_output, latin):
    assert isinstance(latin, str)
    assert function_output["latin"] == latin
