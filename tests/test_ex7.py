import pytest

from pytest_bdd import scenarios, given, when, then, parsers, scenario

from exercise7 import word_to_ubbi_dubbi


# Scenarions
scenarios("ex7.feature")

# Fixtures


@scenario(
    "ex7.feature",
    "one word",
    example_converters=dict(word=str, ubbidubbi=str)
)
def test_word():
    pass

# Given Steps
@given("<word>", target_fixture="function_output")
def start_single_word(word):
    """Prepare dict for output"""
    assert isinstance(word, str)
    return dict(word=word)

# When Steps
@when("I transform the word <word> into ubbi dubbi")
def transform_single_word(function_output, word):
    assert isinstance(word, str)
    function_output["ubbidubbi"] = word_to_ubbi_dubbi(word)


# Then Steps
@then("I obtain <ubbidubbi>")
def pig_ouptput_matches_expected(function_output, ubbidubbi):
    assert isinstance(ubbidubbi, str)
    assert function_output["ubbidubbi"] == ubbidubbi
