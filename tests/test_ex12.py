import pytest

from pytest_bdd import scenarios, given, when, then, parsers, scenario

from exercise12 import create_occurence_dic, get_word_with_the_most_letters


# Scenarions
scenarios("ex12.feature")

# Fixtures

@scenario(
    "ex12.feature",
    "Create dic of letter ocurences in a word",
    example_converters=dict(word=str, dic=str)
)
def test_word():
    pass

# Given Steps
@given("<word>", target_fixture="function_output")
def start_single_word(word):
    """Prepare dict for output"""
    assert isinstance(word, str)
    return dict(word=word)

@given("an empty string", target_fixture="function_output")
def start_single_word():
    """Prepare dict for output"""
    return dict()

@given(parsers.parse("the list of strings {word_list}"), target_fixture="function_output")
def start_single_word(word_list):
    """Parse input and prepare dict for output"""
    input_list = eval(word_list)
    return dict(input_list = input_list)

# When Steps
@when("I count the letters in <word>")
def transform_single_word(function_output, word):
    assert isinstance(word, str)
    function_output["occurence_dic"] = create_occurence_dic(word)

@when("I count the letters in the empty string")
def transform_single_word(function_output):
    function_output["occurence_dic"] = create_occurence_dic("")

@when("I request the word with the most repeated letters")
def transform_single_word(function_output):
    function_output["returned_word"] = get_word_with_the_most_letters(function_output["input_list"])

# Then Steps
@then("I obtain the <dic>")
def pig_ouptput_matches_expected(function_output, dic):
    excpected_dic = eval(dic)
    assert function_output["occurence_dic"] == excpected_dic

@then("I obtain an empty dic")
def pig_ouptput_matches_expected(function_output):
    excpected_dic = {}
    assert function_output["occurence_dic"] == excpected_dic

@then(parsers.parse("I obtain '{word}'"))
def pig_ouptput_matches_expected(word,function_output):
    assert function_output["returned_word"] == word
