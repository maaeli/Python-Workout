import json
from subprocess import run, Popen, PIPE, STDOUT
from os import linesep
import pytest

from pytest_bdd import scenarios, given, when, then, parsers


# Scenarions
scenarios("ex3.feature")

# Fixtures

# Given Steps
@given("the program is running", target_fixture="program_pipe")
def prepare_random_numbers():
    """Start and return program"""
    run_programm = Popen(["python", "exercise3.py"],
                            universal_newlines=True,
                            stdout=PIPE, stderr=PIPE, stdin=PIPE)
    return dict(pipe=run_programm)


# When Steps
@when(parsers.parse('I enter {numbers} ENTER'))
def get_account_data(numbers, program_pipe):
    number_as_str = [x.strip(",") for x in numbers.split()]
    program_input = ""
    for number in number_as_str:
        program_input += number + linesep
    program_input += linesep
    stdout, stderr = program_pipe["pipe"].communicate(program_input)
    program_pipe["final"] = stdout.split(linesep)[-2]

# Then Steps
@then(parsers.parse('The text "Average of {average} over {number_of_runs} runs" is displayed'))
def compare_to_built_in(average, number_of_runs, program_pipe):
    assert program_pipe["final"] == f"Average of {average} over {number_of_runs} runs"
