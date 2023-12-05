import pytest
from tic_tac_toe.utils import computer_step


@pytest.mark.parametrize('fields', [
    ({
        '1': False,
        '2': False,
        '3': False,
        '4': False,
        '5': False,
        '6': False,
        '7': False,
        '8': False,
        '9': False,
    }),
])
def test_computer_step_all_fields_free(fields):
    assert fields[computer_step(fields)] is False


@pytest.mark.parametrize('fields, expected_result', [
    ({
        '1': 'X',
        '2': 'X',
        '3': 'X',
        '4': 'X',
        '5': 'X',
        '6': 'X',
        '7': 'X',
        '8': 'X',
        '9': False,
    }, '9'),
    ({
        '1': 'X',
        '2': False,
        '3': 'O',
        '4': 'X',
        '5': 'X',
        '6': 'O',
        '7': 'X',
        '8': 'X',
        '9': 'O',
    }, '2'),
])
def test_computer_step_only_one_field_free(fields, expected_result):
    assert computer_step(fields) == expected_result
