from mplee_interpreter.lexer import Lexer
from mplee_interpreter.definitions.values import Token
from mplee_interpreter.definitions.utils import Position
from mplee_interpreter.definitions.types import (
    TT_INT,
    TT_EOF,
    TT_STRING,
    TT_KEYWORD,
    TT_MINUS,
    TT_NE,
    TT_EQ,
    TT_LTE,
    TT_GTE
)
import pytest

@pytest.mark.parametrize("mplee", ["5"])
def test_lexer_creates_tokens(lexer_make_tokens_return_tokens):
    assert isinstance(lexer_make_tokens_return_tokens[0], Token)
    assert isinstance(lexer_make_tokens_return_tokens[1], Token)
    
@pytest.mark.parametrize("mplee", ["5"])
def test_is_first_token_value_5(lexer_make_tokens_return_tokens):
    result = lexer_make_tokens_return_tokens
    assert isinstance(result[0].value, int)

@pytest.mark.parametrize("mplee", ["5"])
def test_advance(lexer_object):
    pos = Position(1, 0, 1, "mplee", "5")
    lexer_object_ref = lexer_object
    lexer_object_ref.advance()
    assert pos.idx == lexer_object_ref.pos.idx   
    assert pos.ln == lexer_object_ref.pos.ln 
    assert pos.col == lexer_object_ref.pos.col

@pytest.mark.parametrize("mplee", ["5"])
def test_make_tokens(lexer_make_tokens_return_tokens):
    assert isinstance(lexer_make_tokens_return_tokens[0], Token)
    assert isinstance(lexer_make_tokens_return_tokens[1], Token)
    
    int_token = Token(TT_INT, 5)
    eof_token = Token(TT_EOF) # eof = end of line
    
    assert lexer_make_tokens_return_tokens[0].value == int_token.value
    assert lexer_make_tokens_return_tokens[1].type == eof_token.type

@pytest.mark.parametrize("mplee", ["5"])
def test_make_number(lexer_object):
    lexer_object_make_number = lexer_object.make_number()
    int_token = Token(TT_INT, 5)
    
    assert isinstance(lexer_object_make_number, Token)
    assert lexer_object_make_number.type == int_token.type
    assert lexer_object_make_number.value == int_token.value
    
@pytest.mark.parametrize("mplee", ['"5"'])
def test_make_string(lexer_object):
    lexer_object_make_string = lexer_object.make_string()
    string_token = Token(TT_STRING, "5")
    
    assert isinstance(lexer_object_make_string, Token)
    assert lexer_object_make_string.type == string_token.type
    assert lexer_object_make_string.value == string_token.value 
    
@pytest.mark.parametrize("mplee", ["var"])
def test_make_identifier(lexer_object):
    lexer_object_make_identifier = lexer_object.make_identifier()
    id_token = Token(TT_KEYWORD, "var")

    assert isinstance(lexer_object_make_identifier, Token)
    assert lexer_object_make_identifier.type == id_token.type
    assert lexer_object_make_identifier.value == id_token.value
    
@pytest.mark.parametrize("mplee", ["-"])
def test_make_minus_or_arrow(lexer_object):
    lexer_object_make_minus_or_arrow = lexer_object.make_minus_or_arrow()
    minus_or_arrow_token = Token(TT_MINUS, "-")

    assert isinstance(lexer_object_make_minus_or_arrow, Token)
    assert lexer_object_make_minus_or_arrow.type == minus_or_arrow_token.type

    
@pytest.mark.parametrize("mplee", ["!="])
def test_make_not_equals(lexer_object):
    token, error = lexer_object.make_not_equals()
    make_not_equals_token = Token(TT_NE)
    
    assert isinstance(token, Token)
    assert error == None
    assert token.type == make_not_equals_token.type
    
    
@pytest.mark.parametrize("mplee", ["="])
def test_make_equals(lexer_object):
    lexer_object_make_equals = lexer_object.make_equals()
    make_equals_token = Token(TT_EQ)
    
    assert isinstance(lexer_object_make_equals, Token)
    assert lexer_object_make_equals.type == make_equals_token.type
    
@pytest.mark.parametrize("mplee", ["<="])
def test_make_less_than(lexer_object):
    lexer_object_make_less_than = lexer_object.make_less_than()
    make_less_than_token = Token(TT_LTE)
    
    assert isinstance(lexer_object_make_less_than, Token)
    assert lexer_object_make_less_than.type == make_less_than_token.type
        
@pytest.mark.parametrize("mplee", [">="])
def test_make_less_than(lexer_object):
    lexer_object_make_greater_than = lexer_object.make_greater_than()
    make_greater_than_token = Token(TT_GTE)
    
    assert isinstance(lexer_object_make_greater_than, Token)
    assert lexer_object_make_greater_than.type == make_greater_than_token.type
        