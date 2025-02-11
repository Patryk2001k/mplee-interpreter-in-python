from mplee_interpreter.lexer import Lexer
import pytest

@pytest.fixture
def lexer_object(mplee):
    return Lexer("example.mplee", mplee)

@pytest.fixture
def lexer_make_tokens_return_tokens(mplee):
    lexer = Lexer("example.mplee", mplee)
    tokens, _ = lexer.make_tokens()
    return tokens

@pytest.fixture
def lexer_make_tokens_return_error(mplee):
    lexer = Lexer("example.mplee", mplee)
    _, error = lexer.make_tokens()
    return error


