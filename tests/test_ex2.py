"""Step defintions for testing backend API."""

import json
import random
import pytest

from pytest_bdd import scenarios, given, when, then, parsers

from exercise_2 import my_sum


# Scenarions
scenarios("ex2.feature")

# Fixtures

# Given Steps
@given("random integers", target_fixture="initial_array")
def prepare_random_numbers():
    """Create a test list with up to 100 numbers between -1000 and 1000"""
    list_length = random.randint(1,100)
    numbers = list(map(lambda x: random.randint(-1000,1000), range(list_length)))
    return dict(list=numbers)

@given("no arguments", target_fixture="initial_array")
def prepare_no_argument():
    """Create an empty test list"""
    return dict(list=[])


# When Steps
@when('I calculate my sum')
def get_account_data(initial_array):
    calculated = my_sum(*initial_array["list"])
    initial_array["sum"] = calculated


# Then Steps
@then('I obtain the same result as the built-in')
def compare_to_built_in(initial_array):
    assert initial_array["sum"] == sum(initial_array["list"])


@then(parsers.parse('I obtain {expected}'))
def compare_to_expected(initial_array, expected):
    assert initial_array["sum"] == float(expected)
