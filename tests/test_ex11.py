import json

import pytest

from pytest_bdd import scenarios, given, when, then, parsers

from exercise11 import sort_by_last_name


# Scenarions
scenarios("ex11.feature")

# Fixtures


# Given Steps
@given(parsers.parse("the address book {addresses}"), target_fixture="address_book")
def start_single_word(addresses):
    """Prepare dict for output"""
    addresses = eval(addresses)
    return dict(input=addresses)

# When Steps
@when("I sort it by last name")
def transform_single_word(address_book):
    address_book["output"] = sort_by_last_name(address_book["input"])


# Then Steps
@then(parsers.parse("I obtain {addresses}"))
def pig_ouptput_matches_expected(addresses, address_book):
    addresses = eval(addresses)
    assert address_book["output"] == addresses
