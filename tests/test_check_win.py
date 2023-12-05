import pytest
from tic_tac_toe.utils import check_win


VICTORIE_LINES = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7'],
]


@pytest.mark.parametrize('victories_line, fields, expected_result', [
    (VICTORIE_LINES, {
        '1': 'X',
        '2': 'X',
        '3': 'X',
        '4': False,
        '5': False,
        '6': False,
        '7': False,
        '8': False,
        '9': False,
    }, 'X'),
    (VICTORIE_LINES, {
        '1': 'X',
        '2': 'X',
        '3': 'O',
        '4': False,
        '5': False,
        '6': 'O',
        '7': 'O',
        '8': 'O',
        '9': 'O',
    }, 'O'),
    (VICTORIE_LINES, {
        '1': False,
        '2': False,
        '3': False,
        '4': False,
        '5': False,
        '6': False,
        '7': False,
        '8': False,
        '9': False,
    }, None),
    (VICTORIE_LINES, {
        '1': 'X',
        '2': 'O',
        '3': 'X',
        '4': 'X',
        '5': 'O',
        '6': 'X',
        '7': 'O',
        '8': 'X',
        '9': 'O',
    }, None),

])
def test_check_win(victories_line, fields, expected_result):
    assert check_win(victories_line, fields) == expected_result
