"""
Lexer test cases for TyC compiler
"""

import pytest

from build.lexererr import ErrorToken, IllegalEscape, UncloseString
from tests.utils import Tokenizer


def tokens(*pairs):
    return ",".join([f"{name},{text}" for name, text in pairs] + ["EOF"])


VALID_CASES = [
    pytest.param(
        "auto break case continue default else float for if int return string struct switch void while",
        tokens(
            ("AUTO", "auto"),
            ("BREAK", "break"),
            ("CASE", "case"),
            ("CONTINUE", "continue"),
            ("DEFAULT", "default"),
            ("ELSE", "else"),
            ("FLOAT", "float"),
            ("FOR", "for"),
            ("IF", "if"),
            ("INT", "int"),
            ("RETURN", "return"),
            ("STRING", "string"),
            ("STRUCT", "struct"),
            ("SWITCH", "switch"),
            ("VOID", "void"),
            ("WHILE", "while"),
        ),
        id="keywords",
    ),
    pytest.param("myVar_1", tokens(("ID", "myVar_1")), id="identifier-letters-digits"),
    pytest.param("_x9", tokens(("ID", "_x9")), id="identifier-leading-underscore"),
    pytest.param("0", tokens(("INT_LIT", "0")), id="int-zero"),
    pytest.param("12345", tokens(("INT_LIT", "12345")), id="int-positive"),
    pytest.param("-45", tokens(("INT_LIT", "-45")), id="int-negative"),
    pytest.param("3.14", tokens(("FLOAT_LIT", "3.14")), id="float-decimal"),
    pytest.param("-2.5", tokens(("FLOAT_LIT", "-2.5")), id="float-negative"),
    pytest.param("1.", tokens(("FLOAT_LIT", "1.")), id="float-trailing-dot"),
    pytest.param(".5", tokens(("FLOAT_LIT", ".5")), id="float-leading-dot"),
    pytest.param("1.23e4", tokens(("FLOAT_LIT", "1.23e4")), id="float-sci-lower-e"),
    pytest.param("5.67E-2", tokens(("FLOAT_LIT", "5.67E-2")), id="float-sci-upper-e"),
    pytest.param("0.0", tokens(("FLOAT_LIT", "0.0")), id="float-zero"),
    pytest.param(".5e2", tokens(("FLOAT_LIT", ".5e2")), id="float-leading-dot-sci"),
    pytest.param('"hello"', tokens(("STRING_LIT", '"hello"')), id="string-basic"),
    pytest.param('"tab\\t"', tokens(("STRING_LIT", '"tab\\t"')), id="string-escape-tab"),
    pytest.param('"quote: \\""', tokens(("STRING_LIT", '"quote: \\""')), id="string-escape-quote"),
    pytest.param("++x", tokens(("INC", "++"), ("ID", "x")), id="prefix-inc"),
    pytest.param("x++", tokens(("ID", "x"), ("INC", "++")), id="postfix-inc"),
    pytest.param("--y", tokens(("DEC", "--"), ("ID", "y")), id="prefix-dec"),
    pytest.param("y--", tokens(("ID", "y"), ("DEC", "--")), id="postfix-dec"),
    pytest.param("a+b", tokens(("ID", "a"), ("PLUS", "+"), ("ID", "b")), id="plus"),
    pytest.param("a*b", tokens(("ID", "a"), ("MUL", "*"), ("ID", "b")), id="mul"),
    pytest.param("a/b", tokens(("ID", "a"), ("DIV", "/"), ("ID", "b")), id="div"),
    pytest.param("a%2", tokens(("ID", "a"), ("MOD", "%"), ("INT_LIT", "2")), id="mod"),
    pytest.param("a==b", tokens(("ID", "a"), ("EQ", "=="), ("ID", "b")), id="eq"),
    pytest.param("a!=b", tokens(("ID", "a"), ("NEQ", "!="), ("ID", "b")), id="neq"),
    pytest.param("a<=b", tokens(("ID", "a"), ("LE", "<="), ("ID", "b")), id="le"),
    pytest.param("a>=b", tokens(("ID", "a"), ("GE", ">="), ("ID", "b")), id="ge"),
    pytest.param("a&&b", tokens(("ID", "a"), ("AND", "&&"), ("ID", "b")), id="and"),
    pytest.param("a||b", tokens(("ID", "a"), ("OR", "||"), ("ID", "b")), id="or"),
    pytest.param("!a", tokens(("NOT", "!"), ("ID", "a")), id="not"),
    pytest.param("x=y", tokens(("ID", "x"), ("ASSIGN", "="), ("ID", "y")), id="assign"),
    pytest.param("p.x", tokens(("ID", "p"), ("DOT", "."), ("ID", "x")), id="member-access"),
    pytest.param("(a)", tokens(("LPAREN", "("), ("ID", "a"), ("RPAREN", ")")), id="parens"),
    pytest.param("{ }", tokens(("LBRACE", "{"), ("RBRACE", "}")), id="braces"),
    pytest.param("[i]", tokens(("LBRACK", "["), ("ID", "i"), ("RBRACK", "]")), id="brackets"),
    pytest.param(
        "f(a,b)",
        tokens(
            ("ID", "f"),
            ("LPAREN", "("),
            ("ID", "a"),
            ("COMMA", ","),
            ("ID", "b"),
            ("RPAREN", ")"),
        ),
        id="call-comma",
    ),
    pytest.param("x; y,", tokens(("ID", "x"), ("SEMI", ";"), ("ID", "y"), ("COMMA", ",")), id="semi-comma"),
    pytest.param("/*c*/x", tokens(("ID", "x")), id="block-comment-skip"),
    pytest.param("//c\nx", tokens(("ID", "x")), id="line-comment-skip"),
    pytest.param(
        "auto x=1;",
        tokens(
            ("AUTO", "auto"),
            ("ID", "x"),
            ("ASSIGN", "="),
            ("INT_LIT", "1"),
            ("SEMI", ";"),
        ),
        id="decl-auto-init",
    ),
    pytest.param(
        "a = b + c * 2",
        tokens(
            ("ID", "a"),
            ("ASSIGN", "="),
            ("ID", "b"),
            ("PLUS", "+"),
            ("ID", "c"),
            ("MUL", "*"),
            ("INT_LIT", "2"),
        ),
        id="expr-spaces",
    ),
    pytest.param("1e2", tokens(("INT_LIT", "1"), ("ID", "e2")), id="int-then-id"),
    pytest.param(
        "1..2",
        tokens(("FLOAT_LIT", "1."), ("DOT", "."), ("INT_LIT", "2")),
        id="float-dot-dot",
    ),
    pytest.param(
        'string s="hi";',
        tokens(
            ("STRING", "string"),
            ("ID", "s"),
            ("ASSIGN", "="),
            ("STRING_LIT", '"hi"'),
            ("SEMI", ";"),
        ),
        id="string-decl",
    ),
    pytest.param(
        "struct S { int a; };",
        tokens(
            ("STRUCT", "struct"),
            ("ID", "S"),
            ("LBRACE", "{"),
            ("INT", "int"),
            ("ID", "a"),
            ("SEMI", ";"),
            ("RBRACE", "}"),
            ("SEMI", ";"),
        ),
        id="struct-decl",
    ),
]


ERROR_CASES = [
    pytest.param('"unterminated', UncloseString, id="unclosed-string"),
    pytest.param('"bad\\q"', IllegalEscape, id="illegal-escape"),
    pytest.param("@", ErrorToken, id="error-char"),
]


@pytest.mark.parametrize("source,expected", VALID_CASES)
def test_lexer_tokens(source, expected):
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == expected


@pytest.mark.parametrize("source,error_type", ERROR_CASES)
def test_lexer_errors(source, error_type):
    tokenizer = Tokenizer(source)
    with pytest.raises(error_type):
        tokenizer.get_tokens_as_string()
