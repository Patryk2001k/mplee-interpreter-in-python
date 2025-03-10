from mplee_interpreter.definitions.types import (TT_EOF, TT_EQ, TT_GTE, TT_INT,
                                                 TT_KEYWORD, TT_LTE, TT_MINUS,
                                                 TT_NE, TT_STRING)
from mplee_interpreter.definitions.utils import Position
from mplee_interpreter.definitions.values import Token
from mplee_interpreter.lexer import Lexer


def test_checks_if_make_tokens_method_return_tokens():
    lexer = Lexer("example.mplee", "5")
    tokens, _ = lexer.make_tokens()
    assert isinstance(tokens[0], Token)
    assert isinstance(tokens[1], Token)


def test_if_value_of_first_token_is_5_for_input_5():
    lexer = Lexer("example.mplee", "5")
    tokens, _ = lexer.make_tokens()
    assert isinstance(tokens[0].value, int)


def test_if_id_line_and_column_will_change_their_value_correctly_in_Position_class():
    lexer = Lexer("example.mplee", "5")
    pos = Position(1, 0, 1, "mplee", "5")
    lexer_object_ref = lexer
    lexer_object_ref.advance()
    assert pos.idx == lexer_object_ref.pos.idx
    assert pos.ln == lexer_object_ref.pos.ln
    assert pos.col == lexer_object_ref.pos.col


def test_if_make_tokens_method_return_EOF_token_for_input_5():
    lexer = Lexer("example.mplee", "5")
    tokens, _ = lexer.make_tokens()
    assert isinstance(tokens[0], Token)
    assert isinstance(tokens[1], Token)

    int_token = Token(TT_INT, 5)
    eof_token = Token(TT_EOF)  # eof = end of file

    assert tokens[0].value == int_token.value
    assert tokens[1].type == eof_token.type


def test_if_make_number_method_return_5_number_token_for_input_5():
    lexer = Lexer("example.mplee", "5")
    lexer_object_make_number = lexer.make_number()
    int_token = Token(TT_INT, 5)

    assert isinstance(lexer_object_make_number, Token)
    assert lexer_object_make_number.type == int_token.type
    assert lexer_object_make_number.value == int_token.value


def test_if_make_string_return_5_string_token_for_input_5():
    lexer = Lexer("example.mplee", '"5"')
    lexer_object_make_string = lexer.make_string()
    string_token = Token(TT_STRING, "5")

    assert isinstance(lexer_object_make_string, Token)
    assert lexer_object_make_string.type == string_token.type
    assert lexer_object_make_string.value == string_token.value


def test_if_make_identifier_return_var_token_for_input_var():
    lexer = Lexer("example.mplee", "var")
    lexer_object_make_identifier = lexer.make_identifier()
    id_token = Token(TT_KEYWORD, "var")

    assert isinstance(lexer_object_make_identifier, Token)
    assert lexer_object_make_identifier.type == id_token.type
    assert lexer_object_make_identifier.value == id_token.value


def test_if_make_minus_or_arrow_return_minus_token_for_single_input_minus():
    lexer = Lexer("example.mplee", "-")
    lexer_object_make_minus_or_arrow = lexer.make_minus_or_arrow()
    minus_or_arrow_token = Token(TT_MINUS, "-")

    assert isinstance(lexer_object_make_minus_or_arrow, Token)
    assert lexer_object_make_minus_or_arrow.type == minus_or_arrow_token.type


def test_if_make_not_equals_return_not_equal_token_for_single_input_not_equal():
    lexer = Lexer("example.mplee", "!=")
    token, error = lexer.make_not_equals()
    make_not_equals_token = Token(TT_NE)

    assert isinstance(token, Token)
    assert error == None
    assert token.type == make_not_equals_token.type


def test_if_make_equals_return_equals_token_for_single_input_equals():
    lexer = Lexer("example.mplee", "=")
    lexer_object_make_equals = lexer.make_equals()
    make_equals_token = Token(TT_EQ)

    assert isinstance(lexer_object_make_equals, Token)
    assert lexer_object_make_equals.type == make_equals_token.type


def test_if_make_less_than_return_less_than_token_for_single_input_less_than():
    lexer = Lexer("example.mplee", "<=")
    lexer_object_make_less_than = lexer.make_less_than()
    make_less_than_token = Token(TT_LTE)

    assert isinstance(lexer_object_make_less_than, Token)
    assert lexer_object_make_less_than.type == make_less_than_token.type


def test_if_make_greater_than_return_greater_than_token_for_single_input_greater_than():
    lexer = Lexer("example.mplee", ">=")
    lexer_object_make_greater_than = lexer.make_greater_than()
    make_greater_than_token = Token(TT_GTE)

    assert isinstance(lexer_object_make_greater_than, Token)
    assert lexer_object_make_greater_than.type == make_greater_than_token.type
