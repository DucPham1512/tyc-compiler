"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


def test_lexer_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = "// This is a placeholder test\r\nid"
    tokenizer = Tokenizer(source)
    # TODO: Add actual test assertions
    assert True

# Convert Tokenizer.get_tokens_as_string() into a list of token names.
def _token_names(source: str) -> list[str]:
    s = Tokenizer(source).get_tokens_as_string()
    parts = s.split(",") if s else []
    names = parts[0::2] 
    return names

# Remove trailing EOF token from list of token names.
def _token_names_no_eof(source: str) -> list[str]:
    names = _token_names(source)
    if names and names[-1] == "EOF":
        return names[:-1]
    return names

## Test Cases for Comments ##

# LX-001: Valid block comment
def test_LX_001_valid_block_comment():
    source = "/* Valid block comment */ id"
    assert _token_names_no_eof(source) == ["ID"]


# LX-002: Block comment spans multiple lines
def test_LX_002_block_comment_spans_multiple_lines():
    source = "/* line1\nline2 */ id"
    assert _token_names_no_eof(source) == ["ID"]


# LX-003: Block comment ends at EOF (no trailing code)
def test_LX_003_block_comment_ends_at_eof_no_trailing_code():
    source = "/* comment */"
    assert _token_names_no_eof(source) == []


# LX-004: Unterminated block comment (reaches EOF)
def test_LX_004_unterminated_block_comment_reaches_eof():
    source = "/* Unclosed block comment"
    with pytest.raises(Exception):
        Tokenizer(source).get_tokens_as_string()


# LX-005: Valid line comment (ends at newline)
def test_LX_005_valid_line_comment_ends_at_newline():
    source = "// Valid line comment\nid"
    assert _token_names_no_eof(source) == ["ID"]


# LX-006: /* */ has no meaning inside line comment
def test_LX_006_block_markers_have_no_meaning_inside_line_comment():
    source = "// this /* is not a block */\nid"
    assert _token_names_no_eof(source) == ["ID"]

# LX-007: Comments are not nested (block comment stops at first */)
def test_LX_007_comments_not_nested_block_comment_stops_at_first_end():
    source = "/* outer /* inner */ id"
    assert _token_names_no_eof(source) == ["ID"]
