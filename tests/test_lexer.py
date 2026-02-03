"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
import lexererr

## Test Cases for Comments ##

# LX-001: Valid block comment
def test_LX_001_valid_block_comment():
    tokenizer = Tokenizer("/* Valid block comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


# LX-002: Block comment spans multiple lines
def test_LX_002_block_comment_spans_multiple_lines():
    tokenizer = Tokenizer("/* line1\nline2 */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


# LX-003: Block comment with special characters
def test_LX_003_block_comment_with_special_characters():
    tokenizer = Tokenizer("/* !@#$%^&*()_+-=[]{}|;:'\"<>/?`~ \\b \\t \\f \\\\ /* // still comment \n*/")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

# LX-004: Unterminated block comment (reaches EOF)
def test_LX_004_unterminated_block_comment_reaches_eof():
    tokenizer = Tokenizer("/* Unclosed block comment")
    assert tokenizer.get_tokens_as_string() == "/,*,Unclosed,block,comment,<EOF>"


# LX-005: Valid line comment (ends at newline)
def test_LX_005_valid_line_comment_ends_at_newline():
    tokenizer = Tokenizer("// Valid line comment\n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


# LX-006: /* */ has no meaning inside line comment
def test_LX_006_block_markers_have_no_meaning_inside_line_comment():
    tokenizer = Tokenizer("// this /* is not a block */\n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

# LX-007: Comments are not nested
def test_LX_007_comments_not_nested_block_comment_stops_at_first_end():
    tokenizer = Tokenizer("/* outer */ inner */ id")
    assert tokenizer.get_tokens_as_string() == "inner,*,/,id,<EOF>"


# LX-008: Line comment at EOF
def test_LX_008_line_comment_at_eof():
    tokenizer = Tokenizer("// Line comment encounter EOF <EOF>")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


# LX-009: Nested line comments
def test_LX_009_nested_line_comments():
    tokenizer = Tokenizer("// Outer comment // Inner comment\r\n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


# LX-010: Line comment with special characters
def test_LX_010_line_comment_with_special_characters():
    tokenizer = Tokenizer("// !@#$%^&*()_+-=[]{}|;:'\"<>/?`~ \\b \\t \\f \\\\ /* not a block */ // still comment \n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

## Test Cases for Identifiers ##
# LX-011: Valid identifier (lowercase)
def test_LX_011_valid_identifier_lowercase():
    tokenizer = Tokenizer("validIdentifier")
    assert tokenizer.get_tokens_as_string() == "validIdentifier,<EOF>"

# LX-012: Valid identifier (case-sensitive)
def test_LX_012_valid_identifier_case_sensitive():
    tokenizer = Tokenizer("ValidIdentifier")
    assert tokenizer.get_tokens_as_string() == "ValidIdentifier,<EOF>"


# LX-013: Valid identifier with underscore and digits
def test_LX_013_valid_identifier_underscore_digits():
    tokenizer = Tokenizer("_valid_1234")
    assert tokenizer.get_tokens_as_string() == "_valid_1234,<EOF>"


# LX-014: Valid identifier single letter
def test_LX_014_valid_identifier_single_letter():
    tokenizer = Tokenizer("a")
    assert tokenizer.get_tokens_as_string() == "a,<EOF>"


# LX-015: Valid identifier underscore only
def test_LX_015_valid_identifier_single_underscore():
    tokenizer = Tokenizer("_")
    assert tokenizer.get_tokens_as_string() == "_,<EOF>"


# LX-016: Valid identifier underscore followed by digit
def test_LX_016_valid_identifier_underscore_digit():
    tokenizer = Tokenizer("_0")
    assert tokenizer.get_tokens_as_string() == "_0,<EOF>"


# LX-017: Valid identifier mixed letters digits underscore
def test_LX_017_valid_identifier_mixed():
    tokenizer = Tokenizer("A0_b2")
    assert tokenizer.get_tokens_as_string() == "A0_b2,<EOF>"



# LX-018: Invalid identifier starting with digits
def test_LX_018_invalid_identifier_starts_with_digits():
    tokenizer = Tokenizer("1234Identifier")
    assert tokenizer.get_tokens_as_string() == "1234,Identifier,<EOF>"


def test_LX_019_invalid_identifier_special_prefix():
    tokenizer = Tokenizer("!@#@$identifier")
    assert tokenizer.get_tokens_as_string() == "!,Error Token @"


# LX-020: Invalid identifier with special characters at end
def test_LX_020_invalid_identifier_special_suffix():
    tokenizer = Tokenizer("identifier!@#$%$")
    assert tokenizer.get_tokens_as_string() == "identifier,!,Error Token @"


# LX-021: Invalid identifier starting with zero
def test_LX_021_invalid_identifier_zero_prefix():
    tokenizer = Tokenizer("0identifier")
    assert tokenizer.get_tokens_as_string() == "0,identifier,<EOF>"


# LX-022: Invalid identifier starting with digit followed by letter
def test_LX_022_invalid_identifier_digit_letter():
    tokenizer = Tokenizer("9a")
    assert tokenizer.get_tokens_as_string() == "9,a,<EOF>"


# LX-023: Invalid identifier containing dollar sign
def test_LX_023_invalid_identifier_dollar_sign():
    tokenizer = Tokenizer("a$")
    assert tokenizer.get_tokens_as_string() == "a,Error Token $"


# LX-024: Invalid identifier starting with hash
def test_LX_024_invalid_identifier_hash_prefix():
    tokenizer = Tokenizer("#name")
    assert tokenizer.get_tokens_as_string() == "Error Token #"


# LX-025: Invalid identifier non ASCII characters
def test_LX_025_invalid_identifier_non_ascii():
    tokenizer = Tokenizer("汉字")
    assert tokenizer.get_tokens_as_string() == "Error Token 汉"


## Test Cases for Integer Literals ##
# LX-026: Valid integer literal 1
def test_LX_026_valid_integer_literal_1():
    tokenizer = Tokenizer("13245335")
    assert  tokenizer.get_tokens_as_string() == "13245335,<EOF>"


# LX-027: Valid integer literal 2
def test_LX_027_valid_integer_literal_2():
    tokenizer = Tokenizer("11314353")
    assert  tokenizer.get_tokens_as_string() == "11314353,<EOF>"

# LX-028: Valid integer literal 3
def test_LX_028_valid_integer_literal_3():
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"


# LX-029: Valid integer literal 4 (negative)
def test_LX_029_valid_integer_literal_4_negative():
    tokenizer = Tokenizer("-31254235")
    assert tokenizer.get_tokens_as_string() == "-31254235,<EOF>"


# LX-030: Valid integer literal 5
def test_LX_030_valid_integer_literal_5():
    tokenizer = Tokenizer("32423")
    assert tokenizer.get_tokens_as_string() == "32423,<EOF>"


# LX-031: Valid integer literal 6
def test_LX_031_valid_integer_literal_6():
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"


# LX-032: Valid integer literal 7
def test_LX_032_valid_integer_literal_7():
    tokenizer = Tokenizer("123")
    assert tokenizer.get_tokens_as_string() == "123,<EOF>"


# LX-033: Valid integer literal 8 (max 32-bit signed)
def test_LX_033_valid_integer_literal_8_max_int32():
    tokenizer = Tokenizer("2147483647")
    assert tokenizer.get_tokens_as_string() == "2147483647,<EOF>"


# LX-034: Valid integer literal 9 (negative)
def test_LX_034_valid_integer_literal_9_negative():
    tokenizer = Tokenizer("-45")
    assert tokenizer.get_tokens_as_string() == "-45,<EOF>"


# LX-035: Invalid integer literal 1 (underscore splits tokens)
def test_LX_035_invalid_integer_literal_1_underscore():
    tokenizer = Tokenizer("12_34")
    assert tokenizer.get_tokens_as_string() == "12,_34,<EOF>"


# LX-036: Invalid integer literal 2
def test_LX_036_invalid_integer_literal_2_hex_like():
    tokenizer = Tokenizer("0x10")
    assert tokenizer.get_tokens_as_string() == "0,x10,<EOF>"


# LX-037: Invalid integer literal 3 (actually float literal)
def test_LX_037_invalid_integer_literal_3_is_float():
    tokenizer = Tokenizer("1.20E+04")
    assert tokenizer.get_tokens_as_string() == "1.20E+04,<EOF>"



# LX-038: Invalid integer literal 4 (trailing minus)
def test_LX_038_invalid_integer_literal_4_trailing_minus():
    tokenizer = Tokenizer("45-")
    assert tokenizer.get_tokens_as_string() == "45,-,<EOF>"


# LX-039: Invalid integer literal 5 (actually float literal)
def test_LX_039_invalid_integer_literal_5_is_float():
    tokenizer = Tokenizer("12.34")
    assert tokenizer.get_tokens_as_string() == "12.34,<EOF>"


## Test Cases for Float Literals ##
# LX-040: Valid float literal 1
def test_LX_040_valid_float_literal_1():
    tokenizer = Tokenizer("213.4412343")
    assert tokenizer.get_tokens_as_string() == "213.4412343,<EOF>"


# LX-041: Valid float literal 2
def test_LX_041_valid_float_literal_2():
    tokenizer = Tokenizer("2133.7e12344134")
    assert tokenizer.get_tokens_as_string() == "2133.7e12344134,<EOF>"


# LX-042: Valid float literal 3
def test_LX_042_valid_float_literal_3():
    tokenizer = Tokenizer("3423423.5e-1243452")
    assert tokenizer.get_tokens_as_string() == "3423423.5e-1243452,<EOF>"


# LX-043: Valid float literal 4
def test_LX_043_valid_float_literal_4():
    tokenizer = Tokenizer("321435.3e+324324")
    assert tokenizer.get_tokens_as_string() == "321435.3e+324324,<EOF>"


# LX-044: Valid float literal 5
def test_LX_044_valid_float_literal_5():
    tokenizer = Tokenizer("231244.6E1445315")
    assert tokenizer.get_tokens_as_string() == "231244.6E1445315,<EOF>"


# LX-045: Valid float literal 6
def test_LX_045_valid_float_literal_6():
    tokenizer = Tokenizer("43254325.9E+43252")
    assert tokenizer.get_tokens_as_string() == "43254325.9E+43252,<EOF>"


# LX-046: Valid float literal 7
def test_LX_046_valid_float_literal_7():
    tokenizer = Tokenizer("3434.1E324234")
    assert tokenizer.get_tokens_as_string() == "3434.1E324234,<EOF>"


# LX-047: Valid float literal 8
def test_LX_047_valid_float_literal_8():
    tokenizer = Tokenizer("1.")
    assert tokenizer.get_tokens_as_string() == "1.,<EOF>"


# LX-048: Valid float literal 9
def test_LX_048_valid_float_literal_9():
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"


# LX-049: Valid float literal 10
def test_LX_049_valid_float_literal_10():
    tokenizer = Tokenizer(".3E123443")
    assert tokenizer.get_tokens_as_string() == ".3E123443,<EOF>"


# LX-050: Valid float literal 11
def test_LX_050_valid_float_literal_11():
    tokenizer = Tokenizer(".5e1432")
    assert tokenizer.get_tokens_as_string() == ".5e1432,<EOF>"


# LX-051: Valid float literal 12
def test_LX_051_valid_float_literal_12():
    tokenizer = Tokenizer(".2e+343242")
    assert tokenizer.get_tokens_as_string() == ".2e+343242,<EOF>"


# LX-052: Valid float literal 13
def test_LX_052_valid_float_literal_13():
    tokenizer = Tokenizer(".4e-234234")
    assert tokenizer.get_tokens_as_string() == ".4e-234234,<EOF>"


# LX-053: Valid float literal 14
def test_LX_053_valid_float_literal_14():
    tokenizer = Tokenizer(".6E-342432")
    assert tokenizer.get_tokens_as_string() == ".6E-342432,<EOF>"


# LX-054: Valid float literal 15
def test_LX_054_valid_float_literal_15():
    tokenizer = Tokenizer(".8E+2657")
    assert tokenizer.get_tokens_as_string() == ".8E+2657,<EOF>"


# LX-055: Valid float literal 16
def test_LX_055_valid_float_literal_16():
    tokenizer = Tokenizer("3E14")
    assert tokenizer.get_tokens_as_string() == "3E14,<EOF>"


# LX-056: Valid float literal 17
def test_LX_056_valid_float_literal_17():
    tokenizer = Tokenizer("123E+04")
    assert tokenizer.get_tokens_as_string() == "123E+04,<EOF>"


# LX-057: Valid float literal 18
def test_LX_057_valid_float_literal_18():
    tokenizer = Tokenizer("22E-212")
    assert tokenizer.get_tokens_as_string() == "22E-212,<EOF>"


# LX-058: Valid float literal 19
def test_LX_058_valid_float_literal_19():
    tokenizer = Tokenizer("5e2")
    assert tokenizer.get_tokens_as_string() == "5e2,<EOF>"


# LX-059: Valid float literal 20
def test_LX_059_valid_float_literal_20():
    tokenizer = Tokenizer("10e-2")
    assert tokenizer.get_tokens_as_string() == "10e-2,<EOF>"


# LX-060: Valid float literal 21
def test_LX_060_valid_float_literal_21():
    tokenizer = Tokenizer("43e+123")
    assert tokenizer.get_tokens_as_string() == "43e+123,<EOF>"


# LX-061: Valid float literal 22
def test_LX_061_valid_float_literal_22():
    tokenizer = Tokenizer("1.00E+00")
    assert tokenizer.get_tokens_as_string() == "1.00E+00,<EOF>"


# LX-062: Invalid float literal 1
def test_LX_062_invalid_float_literal_1():
    tokenizer = Tokenizer("1.23e")
    assert tokenizer.get_tokens_as_string() == "1.23,e,<EOF>"


# LX-063: Invalid float literal 2
def test_LX_063_invalid_float_literal_2():
    tokenizer = Tokenizer("1.23E-")
    assert tokenizer.get_tokens_as_string() == "1.23,E,-,<EOF>"


# LX-064: Invalid float literal 3
def test_LX_064_invalid_float_literal_3():
    tokenizer = Tokenizer("0..1")
    assert tokenizer.get_tokens_as_string() == "0.,.1,<EOF>"


# LX-065: Invalid float literal 4
def test_LX_065_invalid_float_literal_4():
    tokenizer = Tokenizer("1.2.3")
    assert tokenizer.get_tokens_as_string() == "1.2,.3,<EOF>"


# LX-066: Invalid float literal 5 (negative float)
def test_LX_066_negative_float_literal():
    tokenizer = Tokenizer("-1.5")
    assert tokenizer.get_tokens_as_string() == "-1.5,<EOF>"


## Test Cases for Keywords ##
# LX-067: All keywords
def test_LX_067_all_keywords():
    tokenizer = Tokenizer("auto break case continue default else float for if int return string struct switch void while") 
    assert tokenizer.get_tokens_as_string() == "auto,break,case,continue,default,else,float,for,if,int,return,string,struct,switch,void,while,<EOF>"


# LX-068: Arithmetic operators
def test_LX_068_arithmetic_operators():
    tokenizer = Tokenizer("+ - * / %")
    assert tokenizer.get_tokens_as_string() == "+,-,*,/,%,<EOF>"


# LX-069: Relational operators
def test_LX_069_relational_operators():
    tokenizer = Tokenizer("== != < > <= >=")
    assert tokenizer.get_tokens_as_string() == "==,!=,<,>,<=,>=,<EOF>"


# LX-070: Logical operators
def test_LX_070_logical_operators():
    tokenizer = Tokenizer("|| && !")
    assert tokenizer.get_tokens_as_string() == "||,&&,!,<EOF>"


# LX-071: Unary / assignment / member access
def test_LX_071_unary_assignment_member_access():
    tokenizer = Tokenizer("++ -- = .")
    assert tokenizer.get_tokens_as_string() == "++,--,=,.,<EOF>"


# LX-072: Separators
def test_LX_072_separators():
    tokenizer = Tokenizer("{ } ( ) ; : ,")
    assert tokenizer.get_tokens_as_string() == "{,},(,),;,:,,,<EOF>"



## Test Cases for String Literals ##
# LX-073: Empty String
def test_LX_073_empty_string():
    tokenizer = Tokenizer("\"\"")
    assert tokenizer.get_tokens_as_string() == ",<EOF>"


# LX-074: Simple String
def test_LX_074_simple_string():
    tokenizer = Tokenizer("\"Hello World\"")
    assert tokenizer.get_tokens_as_string() == "Hello World,<EOF>"


# LX-075: Long String
def test_LX_075_long_string():
    tokenizer = Tokenizer("\"Very very very very very very very very very very very very very very  very very very  long string\"")
    assert tokenizer.get_tokens_as_string() == "Very very very very very very very very very very very very very very  very very very  long string,<EOF>"


# LX-076: String with Escapes
def test_LX_076_string_with_escapes():
    tokenizer = Tokenizer("\"Line\\nTab\\t\"")
    assert tokenizer.get_tokens_as_string() == "Line\\nTab\\t,<EOF>"


# LX-077: Escaped Quote/Slash
def test_LX_077_escaped_quote_and_backslash():
    tokenizer = Tokenizer("\"He said \\\"Hi\\\" \\\\\"")
    assert tokenizer.get_tokens_as_string() == "He said \\\"Hi\\\" \\\\,<EOF>"


# LX-078: Extended ASCII
def test_LX_078_extended_ascii():
    tokenizer = Tokenizer("\"\x80\xFF\"")
    assert tokenizer.get_tokens_as_string() == "\x80\xFF,<EOF>"

    # LX-079: Error: Illegal Escape (Checks for invalid escape char)
def test_LX_079_illegal_escape_invalid_char():
    tokenizer = Tokenizer("\"Bad escape: \\a\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: Bad escape: \\a"


# LX-080: Error: Illegal Escape Priority (Illegal escape detected before unclosed)
def test_LX_080_illegal_escape_priority_over_unclosed():
    tokenizer = Tokenizer("\"Invalid \\a and unclosed")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: Invalid \\a"


# LX-081: Error: Unclosed String (Newline) (CRLF encountered before closing quote)
def test_LX_081_unclosed_string_newline():
    tokenizer = Tokenizer("\"Unclosed string\r\nwith newline")
    assert tokenizer.get_tokens_as_string() == "Unclosed String: Unclosed string\r"


# LX-082: Error: Unclosed String (EOF)
def test_LX_082_unclosed_string_eof():
    tokenizer = Tokenizer("\"End of file")
    assert tokenizer.get_tokens_as_string() == "Unclosed String: End of file"


# LX-083: Escape Backspace
def test_LX_083_escape_backspace():
    tokenizer = Tokenizer("\"Test\\bCase\"")
    assert tokenizer.get_tokens_as_string() == "Test\\bCase,<EOF>"


# LX-084: Escape Formfeed
def test_LX_084_escape_formfeed():
    tokenizer = Tokenizer("\"Page\\fBreak\"")
    assert tokenizer.get_tokens_as_string() == "Page\\fBreak,<EOF>"

# LX-085: Escape Carriage Return
def test_LX_085_escape_carriage_return():
    tokenizer = Tokenizer("\"Line\\rReturn\"")
    assert tokenizer.get_tokens_as_string() == "Line\\rReturn,<EOF>"


# LX-086: Escape Newline
def test_LX_086_escape_newline():
    tokenizer = Tokenizer("\"New\\nLine\"")
    assert tokenizer.get_tokens_as_string() == "New\\nLine,<EOF>"


# LX-087: Escape Horizontal Tab
def test_LX_087_escape_horizontal_tab():
    tokenizer = Tokenizer("\"Col1\\tCol2\"")
    assert tokenizer.get_tokens_as_string() == "Col1\\tCol2,<EOF>"


# LX-088: Escape Double Quote
def test_LX_088_escape_double_quote():
    tokenizer = Tokenizer("\"Quote: \\\"\"")
    assert tokenizer.get_tokens_as_string() == "Quote: \\\",<EOF>"


# LX-089: Escape Backslash
def test_LX_089_escape_backslash():
    tokenizer = Tokenizer("\"Path\\\\to\"")
    assert tokenizer.get_tokens_as_string() == "Path\\\\to,<EOF>"


# LX-090: All Legal Escapes Mixed
def test_LX_090_all_legal_escapes_mixed():
    tokenizer = Tokenizer("\"A\\bB\\fC\\rD\\nE\\tF\\\"G\\\\\"")
    assert tokenizer.get_tokens_as_string() == "A\\bB\\fC\\rD\\nE\\tF\\\"G\\\\,<EOF>"


# LX-091: Illegal: Bell/Alert (\a)
def test_LX_091_illegal_escape_bell():
    tokenizer = Tokenizer("\"Ring \\a bell\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: Ring \\a"


# LX-092: Illegal: Vertical Tab (\v)
def test_LX_092_illegal_escape_vertical_tab():
    tokenizer = Tokenizer("\"Vertical \\v Tab\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: Vertical \\v"


# LX-093: Illegal: Single Quote (\')
def test_LX_093_illegal_escape_single_quote():
    tokenizer = Tokenizer("\"It\\'s invalid\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: It\\'"


# LX-094: Illegal: Question Mark (\?)
def test_LX_094_illegal_escape_question_mark():
    tokenizer = Tokenizer("\"What\\?\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: What\\?"


# LX-095: Illegal: Null Character (\0)
def test_LX_095_illegal_escape_null_char():
    tokenizer = Tokenizer("\"Null \\0 byte\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: Null \\0"


# LX-096: Illegal: Unknown Char (\z)
def test_LX_096_illegal_escape_unknown_char():
    tokenizer = Tokenizer("\"Random \\z escape\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: Random \\z"


# LX-097: Illegal: Number (\1)
def test_LX_097_illegal_escape_number():
    tokenizer = Tokenizer("\"Number \\1 escape\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: Number \\1"


# LX-098: Illegal Priority Case 1 (first illegal escape wins)
def test_LX_098_illegal_escape_priority_case_1():
    tokenizer = Tokenizer("\"Valid \\n but \\a then \\t\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: Valid \\n but \\a"


# LX-099: Illegal Priority Case 2 (illegal escape beats unclosed)
def test_LX_099_illegal_escape_priority_case_2():
    tokenizer = Tokenizer("\"Unclosed and \\a illegal")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: Unclosed and \\a"

# LX-100: String with unprintable ASCII characters (0-31)
def test_LX_100_string_with_ascii_0_31():
    tokenizer = Tokenizer("\"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\\n\x0B\x0C\\r\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F\"")
    assert tokenizer.get_tokens_as_string() == "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\\n\x0B\x0C\\r\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F,<EOF>"
   

# LX-101: Unclosed String with direct \n character    
def test_LX_101_direct_newline_in_string_1():
    tokenizer = Tokenizer("\"This string contains a direct newline \n character\"")
    assert tokenizer.get_tokens_as_string() == "Unclosed String: This string contains a direct newline \n"

# LX-102: Unclosed String with direct \r character
def test_LX_102_direct_newline_in_string_2():
    tokenizer = Tokenizer("\"Another string with direct newline \r here\"")
    assert tokenizer.get_tokens_as_string() == "Unclosed String: Another string with direct newline \r"


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
