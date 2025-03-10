from mplee_interpreter.definitions.utils import Position
from mplee_interpreter.errors.strings_with_arrows import string_with_arrows


def test_if_string_with_arrows_draws_correct_amount_of_arrows():
    text = "line 1\nline 2\nline 3"
    pos_start = Position(7, 1, 2, "test_file", text)
    pos_end = Position(11, 1, 6, "test_file", text)

    expected_output = "line 2\n  ^^^^"

    result = string_with_arrows(text, pos_start, pos_end)

    assert result.strip() == expected_output


def test_how_string_with_arrows_handles_single_line():
    text = "single line"
    pos_start = Position(0, 0, 0, "test_file", text)
    pos_end = Position(11, 0, 11, "test_file", text)

    expected_output = "single line\n^^^^^^^^^^^"

    result = string_with_arrows(text, pos_start, pos_end)

    assert result.strip() == expected_output


def test_how_string_with_arrows_handles_multiple_lines():
    text = "first line\nsecond line\nthird line"
    pos_start = Position(6, 0, 6, "test_file", text)
    pos_end = Position(25, 2, 5, "test_file", text)

    expected_output = (
        "first line\n      ^^^\nsecond line\n^^^^^^^^^^^\nthird line\n^^^^^"
    )

    result = string_with_arrows(text, pos_start, pos_end)

    assert result.strip() == expected_output
