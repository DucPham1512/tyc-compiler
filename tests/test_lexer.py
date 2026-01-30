"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
import lexererr

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


# LX-003: Block comment with special characters
def test_LX_003_block_comment_with_special_characters():
    source = ("/* !@#$%^&*()_+-=[]{}|;:'\"<>/?`~ \\b \\t \\f \\\\ /* // still comment \n*/id")
    assert _token_names_no_eof(source) == ["ID"]

# LX-004: Unterminated block comment (reaches EOF)
def test_LX_004_unterminated_block_comment_reaches_eof():
    source = "/* Unclosed block comment"
    assert _token_names_no_eof(source) == ["DIV", "MUL", "ID", "ID", "ID"]


# LX-005: Valid line comment (ends at newline)
def test_LX_005_valid_line_comment_ends_at_newline():
    source = "// Valid line comment\nid"
    assert _token_names_no_eof(source) == ["ID"]


# LX-006: /* */ has no meaning inside line comment
def test_LX_006_block_markers_have_no_meaning_inside_line_comment():
    source = "// this /* is not a block */\nid"
    assert _token_names_no_eof(source) == ["ID"]

# LX-007: Comments are not nested
def test_LX_007_comments_not_nested_block_comment_stops_at_first_end():
    source = "/* outer */ inner */ id"
    assert _token_names_no_eof(source) == ["ID", "MUL", "DIV", "ID"]


# LX-008: Line comment at EOF
def test_LX_008_line_comment_at_eof():
    source = "// Line comment encounter EOF <EOF>"
    assert _token_names_no_eof(source) == []
    

# LX-009: Nested line comments
def test_LX_009_nested_line_comments():
    source = "// Outer comment // Inner comment\r\nid"
    assert _token_names_no_eof(source) == ["ID"]    
    

# LX-010: Line comment with special characters
def test_LX_010_line_comment_with_special_characters():
    source = "// !@#$%^&*()_+-=[]{}|;:'\"<>/?`~ \\b \\t \\f \\\\ /* not a block */ // still comment \nid"
    assert _token_names_no_eof(source) == ["ID"]
    
## Test Cases for Identifiers ##
# LX-011: Valid identifier (lowercase)
def test_LX_011_valid_identifier_lowercase():
    source = "validIdentifier"
    assert _token_names_no_eof(source) == ["ID"]


# LX-012: Valid identifier (case-sensitive)
def test_LX_012_valid_identifier_case_sensitive():
    source = "ValidIdentifier"
    assert _token_names_no_eof(source) == ["ID"]


# LX-013: Valid identifier with underscore and digits
def test_LX_013_valid_identifier_underscore_digits():
    source = "_valid_1234"
    assert _token_names_no_eof(source) == ["ID"]


# LX-014: Valid identifier single letter
def test_LX_014_valid_identifier_single_letter():
    source = "a"
    assert _token_names_no_eof(source) == ["ID"]


# LX-015: Valid identifier underscore only
def test_LX_015_valid_identifier_single_underscore():
    source = "_"
    assert _token_names_no_eof(source) == ["ID"]


# LX-016: Valid identifier underscore followed by digit
def test_LX_016_valid_identifier_underscore_digit():
    source = "_0"
    assert _token_names_no_eof(source) == ["ID"]


# LX-017: Valid identifier mixed letters digits underscore
def test_LX_017_valid_identifier_mixed():
    source = "A0_b2"
    assert _token_names_no_eof(source) == ["ID"]


# LX-018: Invalid identifier starting with digits
def test_LX_018_invalid_identifier_starts_with_digits():
    source = "1234Identifier"
    assert _token_names_no_eof(source) == ["INT_LIT", "ID"]


def test_LX_019_invalid_identifier_special_prefix():
    source = "!@#@$identifier"
    with pytest.raises(lexererr.ErrorToken) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Error Token !"


# LX-020: Invalid identifier with special characters at end
def test_LX_020_invalid_identifier_special_suffix():
    source = "identifier!@#$%$"
    with pytest.raises(lexererr.ErrorToken) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Error Token !"


# LX-021: Invalid identifier starting with zero
def test_LX_021_invalid_identifier_zero_prefix():
    source = "0identifier"
    with pytest.raises(lexererr.ErrorToken) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Error Token 0"


# LX-022: Invalid identifier starting with digit followed by letter
def test_LX_022_invalid_identifier_digit_letter():
    source = "9a"
    with pytest.raises(lexererr.ErrorToken) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Error Token 9"


# LX-023: Invalid identifier containing dollar sign
def test_LX_023_invalid_identifier_dollar_sign():
    source = "a$"
    with pytest.raises(lexererr.ErrorToken) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Error Token $"


# LX-024: Invalid identifier starting with hash
def test_LX_024_invalid_identifier_hash_prefix():
    source = "#name"
    with pytest.raises(lexererr.ErrorToken) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Error Token #"


# LX-025: Invalid identifier non ASCII characters
def test_LX_025_invalid_identifier_non_ascii():
    source = "汉字"
    with pytest.raises(lexererr.ErrorToken) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Error Token 汉"


## Test Cases for Integer Literals ##
# LX-026: Valid integer literal 1
def test_LX_026_valid_integer_literal_1():
    source = "13245335"
    assert _token_names_no_eof(source) == ["INT_LIT"]


# LX-027: Valid integer literal 2
def test_LX_027_valid_integer_literal_2():
    source = "11314353"
    assert _token_names_no_eof(source) == ["INT_LIT"]


# LX-028: Valid integer literal 3
def test_LX_028_valid_integer_literal_3():
    source = "0"
    assert _token_names_no_eof(source) == ["INT_LIT"]


# LX-029: Valid integer literal 4 (negative)
def test_LX_029_valid_integer_literal_4_negative():
    source = "-31254235"
    assert _token_names_no_eof(source) == ["INT_LIT"]


# LX-030: Valid integer literal 5
def test_LX_030_valid_integer_literal_5():
    source = "32423"
    assert _token_names_no_eof(source) == ["INT_LIT"]


# LX-031: Valid integer literal 6
def test_LX_031_valid_integer_literal_6():
    source = "0"
    assert _token_names_no_eof(source) == ["INT_LIT"]


# LX-032: Valid integer literal 7
def test_LX_032_valid_integer_literal_7():
    source = "123"
    assert _token_names_no_eof(source) == ["INT_LIT"]


# LX-033: Valid integer literal 8 (max 32-bit signed)
def test_LX_033_valid_integer_literal_8_max_int32():
    source = "2147483647"
    assert _token_names_no_eof(source) == ["INT_LIT"]


# LX-034: Valid integer literal 9 (negative)
def test_LX_034_valid_integer_literal_9_negative():
    source = "-45"
    assert _token_names_no_eof(source) == ["INT_LIT"]


# LX-035: Invalid integer literal 1 (underscore splits tokens)
def test_LX_035_invalid_integer_literal_1_underscore():
    source = "12_34"
    assert _token_names_no_eof(source) == ["INT_LIT", "UNDERSCORE", "INT_LIT"]


# LX-036: Invalid integer literal 2 (0x10 splits into int * int)
def test_LX_036_invalid_integer_literal_2_hex_like():
    source = "0x10"
    assert _token_names_no_eof(source) == ["INT_LIT", "MUL", "INT_LIT"]


# LX-037: Invalid integer literal 3 (actually float literal)
def test_LX_037_invalid_integer_literal_3_is_float():
    source = "1.20E+04"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-038: Invalid integer literal 4 (trailing minus)
def test_LX_038_invalid_integer_literal_4_trailing_minus():
    source = "45-"
    assert _token_names_no_eof(source) == ["INT_LIT", "SUB"]


# LX-039: Invalid integer literal 5 (actually float literal)
def test_LX_039_invalid_integer_literal_5_is_float():
    source = "12.34"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]