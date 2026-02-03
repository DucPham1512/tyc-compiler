"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
import lexererr

# Convert Tokenizer.get_tokens_as_string() into a list of token names.
def _token_names(source: str) -> list[str]:
    token_string = Tokenizer(source).get_tokens_as_string()
    if not token_string:
        return []

    i = 0
    length = len(token_string)
    names: list[str] = []

    while i < length:
        next_comma_pos = token_string.find(",", i)
        if next_comma_pos == -1:
            names.append(token_string[i:])
            break

        name = token_string[i:next_comma_pos]
        names.append(name)
        i = next_comma_pos + 1

        if i < length and token_string[i] == ",":
            i += 1
            if i < length and token_string[i] == ",":
                i += 1
            continue

        next_comma_pos = token_string.find(",", i)
        if next_comma_pos == -1:
            break
        i = next_comma_pos + 1

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
    assert str(e.value) == "Error Token @"


# LX-020: Invalid identifier with special characters at end
def test_LX_020_invalid_identifier_special_suffix():
    source = "identifier!@#$%$"
    with pytest.raises(lexererr.ErrorToken) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Error Token @"


# LX-021: Invalid identifier starting with zero
def test_LX_021_invalid_identifier_zero_prefix():
    source = "0identifier"
    assert _token_names_no_eof(source) == ["INT_LIT", "ID"]


# LX-022: Invalid identifier starting with digit followed by letter
def test_LX_022_invalid_identifier_digit_letter():
    source = "9a"
    assert _token_names_no_eof(source) == ["INT_LIT", "ID"]


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
    print(_token_names_no_eof(source))
    assert _token_names_no_eof(source) == ["INT_LIT", "ID"]


# LX-036: Invalid integer literal 2
def test_LX_036_invalid_integer_literal_2_hex_like():
    source = "0x10"
    assert _token_names_no_eof(source) == ["INT_LIT", "ID"]


# LX-037: Invalid integer literal 3 (actually float literal)
def test_LX_037_invalid_integer_literal_3_is_float():
    source = "1.20E+04"
    print(_token_names_no_eof(source))
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-038: Invalid integer literal 4 (trailing minus)
def test_LX_038_invalid_integer_literal_4_trailing_minus():
    source = "45-"
    assert _token_names_no_eof(source) == ["INT_LIT", "MINUS"]


# LX-039: Invalid integer literal 5 (actually float literal)
def test_LX_039_invalid_integer_literal_5_is_float():
    source = "12.34"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]
    

## Test Cases for Float Literals ##
# LX-040: Valid float literal 1
def test_LX_040_valid_float_literal_1():
    source = "213.4412343"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-041: Valid float literal 2
def test_LX_041_valid_float_literal_2():
    source = "2133.7e12344134"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-042: Valid float literal 3
def test_LX_042_valid_float_literal_3():
    source = "3423423.5e-1243452"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-043: Valid float literal 4
def test_LX_043_valid_float_literal_4():
    source = "321435.3e+324324"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-044: Valid float literal 5
def test_LX_044_valid_float_literal_5():
    source = "231244.6E1445315"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-045: Valid float literal 6
def test_LX_045_valid_float_literal_6():
    source = "43254325.9E+43252"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-046: Valid float literal 7
def test_LX_046_valid_float_literal_7():
    source = "3434.1E324234"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-047: Valid float literal 8
def test_LX_047_valid_float_literal_8():
    source = "1."
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-048: Valid float literal 9
def test_LX_048_valid_float_literal_9():
    source = ".5"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-049: Valid float literal 10
def test_LX_049_valid_float_literal_10():
    source = ".3E123443"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-050: Valid float literal 11
def test_LX_050_valid_float_literal_11():
    source = ".5e1432"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-051: Valid float literal 12
def test_LX_051_valid_float_literal_12():
    source = ".2e+343242"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-052: Valid float literal 13
def test_LX_052_valid_float_literal_13():
    source = ".4e-234234"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-053: Valid float literal 14
def test_LX_053_valid_float_literal_14():
    source = ".6E-342432"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-054: Valid float literal 15
def test_LX_054_valid_float_literal_15():
    source = ".8E+2657"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-055: Valid float literal 16
def test_LX_055_valid_float_literal_16():
    source = "3E14"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-056: Valid float literal 17
def test_LX_056_valid_float_literal_17():
    source = "123E+04"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-057: Valid float literal 18
def test_LX_057_valid_float_literal_18():
    source = "22E-212"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-058: Valid float literal 19
def test_LX_058_valid_float_literal_19():
    source = "5e2"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-059: Valid float literal 20
def test_LX_059_valid_float_literal_20():
    source = "10e-2"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-060: Valid float literal 21
def test_LX_060_valid_float_literal_21():
    source = "43e+123"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-061: Valid float literal 22
def test_LX_061_valid_float_literal_22():
    source = "1.00E+00"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]


# LX-062: Invalid float literal 1
def test_LX_062_invalid_float_literal_1():
    source = "1.23e"
    assert _token_names_no_eof(source) == ["FLOAT_LIT", "ID"]


# LX-063: Invalid float literal 2
def test_LX_063_invalid_float_literal_2():
    source = "1.23E-"
    assert _token_names_no_eof(source) == ["FLOAT_LIT", "ID", "MINUS"]


# LX-064: Invalid float literal 3
def test_LX_064_invalid_float_literal_3():
    source = "0..1"
    assert _token_names_no_eof(source) == ["FLOAT_LIT", "FLOAT_LIT"]


# LX-065: Invalid float literal 4
def test_LX_065_invalid_float_literal_4():
    source = "1.2.3"
    assert _token_names_no_eof(source) == ["FLOAT_LIT", "FLOAT_LIT"]


# LX-066: Invalid float literal 5 (negative float)
def test_LX_066_invalid_float_literal_5_negative():
    source = "-1.5"
    assert _token_names_no_eof(source) == ["FLOAT_LIT"]
    

## Test Cases for Keywords ##
# LX-067: All keywords
def test_LX_067_all_keywords():
    source = "auto break case continue default else float for if int return string struct switch void while"
    assert _token_names_no_eof(source) == [
        "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE",
        "FLOAT", "FOR", "IF", "INT", "RETURN", "STRING",
        "STRUCT", "SWITCH", "VOID", "WHILE"
    ]


# LX-068: Arithmetic operators
def test_LX_068_arithmetic_operators():
    source = "+ - * / %"
    assert _token_names_no_eof(source) == ["PLUS", "MINUS", "MUL", "DIV", "MOD"]


# LX-069: Relational operators
def test_LX_069_relational_operators():
    source = "== != < > <= >="
    assert _token_names_no_eof(source) == ["EQ", "NEQ", "LT", "GT", "LE", "GE"]


# LX-070: Logical operators
def test_LX_070_logical_operators():
    source = "|| && !"
    assert _token_names_no_eof(source) == ["OR", "AND", "NOT"]


# LX-071: Unary / assignment / member access
def test_LX_071_unary_assignment_member_access():
    source = "++ -- = ."
    assert _token_names_no_eof(source) == ["INC", "DEC", "ASSIGN", "DOT"]


# LX-072: Separators
def test_LX_072_separators():
    source = "{ } ( ) ; : ,"
    print(_token_names_no_eof(source))
    assert _token_names_no_eof(source) == ["LBRACE", "RBRACE", "LPAREN", "RPAREN", "SEMI", "COLON", "COMMA"]


## Test Cases for String Literals ##
# LX-073: Empty String
def test_LX_073_empty_string():
    source = "\"\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-074: Simple String
def test_LX_074_simple_string():
    source = "\"Hello World\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-075: Long String
def test_LX_075_long_string():
    source = "\"Very very very very very very very very very very very very very very  very very very  long string\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-076: String with Escapes
def test_LX_076_string_with_escapes():
    source = "\"Line\\nTab\\t\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-077: Escaped Quote/Slash
def test_LX_077_escaped_quote_and_backslash():
    source = "\"He said \\\"Hi\\\" \\\\\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-078: Extended ASCII
def test_LX_078_extended_ascii():
    source = "\"\x80\xFF\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]
    
    # LX-079: Error: Illegal Escape (Checks for invalid escape char)
def test_LX_079_illegal_escape_invalid_char():
    source = "\"Bad escape: \\a\""
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"Bad escape: \\a\""


# LX-080: Error: Illegal Escape Priority (Illegal escape detected before unclosed)
def test_LX_080_illegal_escape_priority_over_unclosed():
    source = "\"Invalid \\a and unclosed"
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"Invalid \\a"


# LX-081: Error: Unclosed String (Newline) (CRLF encountered before closing quote)
def test_LX_081_unclosed_string_newline():
    source = "\"Unclosed string\r\nwith newline\""
    with pytest.raises(lexererr.UncloseString) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Unclosed String: \"Unclosed string\r"


# LX-082: Error: Unclosed String (EOF)
def test_LX_082_unclosed_string_eof():
    source = "\"End of file"
    with pytest.raises(lexererr.UncloseString) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Unclosed String: \"End of file"


# LX-083: Escape Backspace
def test_LX_083_escape_backspace():
    source = "\"Test\\bCase\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-084: Escape Formfeed
def test_LX_084_escape_formfeed():
    source = "\"Page\\fBreak\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-085: Escape Carriage Return
def test_LX_085_escape_carriage_return():
    source = "\"Line\\rReturn\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-086: Escape Newline
def test_LX_086_escape_newline():
    source = "\"New\\nLine\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-087: Escape Horizontal Tab
def test_LX_087_escape_horizontal_tab():
    source = "\"Col1\\tCol2\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-088: Escape Double Quote
def test_LX_088_escape_double_quote():
    source = "\"Quote: \\\"\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-089: Escape Backslash
def test_LX_089_escape_backslash():
    source = "\"Path\\\\to\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-090: All Legal Escapes Mixed
def test_LX_090_all_legal_escapes_mixed():
    source = "\"A\\bB\\fC\\rD\\nE\\tF\\\"G\\\\\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]


# LX-091: Illegal: Bell/Alert (\a)
def test_LX_091_illegal_escape_bell():
    source = "\"Ring \\a bell\""
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"Ring \\a"


# LX-092: Illegal: Vertical Tab (\v)
def test_LX_092_illegal_escape_vertical_tab():
    source = "\"Vertical \\v Tab\""
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"Vertical \\v"


# LX-093: Illegal: Single Quote (\')
def test_LX_093_illegal_escape_single_quote():
    source = "\"It\\'s invalid\""
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"It\\'"


# LX-094: Illegal: Question Mark (\?)
def test_LX_094_illegal_escape_question_mark():
    source = "\"What\\?\""
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"What\\?\""


# LX-095: Illegal: Null Character (\0)
def test_LX_095_illegal_escape_null_char():
    source = "\"Null \\0 byte\""
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"Null \\0"


# LX-096: Illegal: Unknown Char (\z)
def test_LX_096_illegal_escape_unknown_char():
    source = "\"Random \\z escape\""
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"Random \\z"


# LX-097: Illegal: Number (\1)
def test_LX_097_illegal_escape_number():
    source = "\"Number \\1 escape\""
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"Number \\1"


# LX-098: Illegal Priority Case 1 (first illegal escape wins)
def test_LX_098_illegal_escape_priority_case_1():
    source = "\"Valid \\n but \\a then \\t\""
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"Valid \\n but \\a"


# LX-099: Illegal Priority Case 2 (illegal escape beats unclosed)
def test_LX_099_illegal_escape_priority_case_2():
    source = "\"Unclosed and \\a illegal"
    with pytest.raises(lexererr.IllegalEscape) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Illegal Escape In String: \"Unclosed and \\a"


# LX-100: String with unprintable ASCII characters (0-31)
def test_LX_100_string_with_ascii_0_31():
    source = "\"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\\n\x0B\x0C\\r\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F\""
    assert _token_names_no_eof(source) == ["STRING_LIT"]
   

# LX-101: Unclosed String with direct \n character    
def test_LX_101_direct_newline_in_string_1():
    source = "\"This string contains a direct newline \n character\""
    with pytest.raises(lexererr.UncloseString) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Unclosed String: \"This string contains a direct newline \n"

# LX-102: Unclosed String with direct \r character
def test_LX_102_direct_newline_in_string_2():
    source = "\"Another string with direct newline \r here\""
    with pytest.raises(lexererr.UncloseString) as e:
        _token_names_no_eof(source)
    assert str(e.value) == "Unclosed String: \"Another string with direct newline \r"


# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"
