import pytest
from tests.utils import Parser


# ========== Basic programs & declarations ==========
def test_PX_001_empty_program():
    assert Parser("").parse() == "success"


def test_PX_002_program_with_only_main():
    assert Parser("void main() {}").parse() == "success"


def test_PX_003_struct_simple():
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_PX_004_function_no_params():
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_PX_005_var_decl_auto_with_init():
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_PX_006_if_simple():
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_PX_007_while_simple():
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_PX_008_for_simple():
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_PX_009_switch_simple():
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_PX_010_assignment_simple():
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"


# ========== Functions (valid & invalid forms) ==========
def test_PX_011_empty_program():
    assert Parser("").parse() == "success"


def test_PX_012_only_main_function():
    assert Parser("void main() {}").parse() == "success"


def test_PX_013_single_struct_declaration():
    assert Parser("struct Point { int x; int y; };").parse() == "success"


def test_PX_014_function_no_params_with_builtin_call():
    assert Parser('void greet() { printString("Hello"); }').parse() == "success"


def test_PX_015_auto_var_with_init_in_main():
    assert Parser("void main() { auto x = 5; }").parse() == "success"


def test_PX_016_simple_if_statement():
    assert Parser("void main() { if (1) printInt(1); }").parse() == "success"


def test_PX_017_simple_while_statement():
    assert Parser("void main() { while (1) printInt(1); }").parse() == "success"


def test_PX_018_function_declaration_with_return_type_return_literal():
    assert Parser("int f() { return 1; }").parse() == "success"


def test_PX_019_function_with_parameters():
    assert Parser("int add(int a, int b) { return a + b; }").parse() == "success"


def test_PX_020_void_function_with_return_edge_success():
    assert Parser("void early() { return; }").parse() == "success"


def test_PX_021_multiple_functions_in_one_program():
    source = "int inc(int x){return x+1;} void main(){int a; a=inc(1);}"
    assert Parser(source).parse() == "success"


def test_PX_022_function_with_nested_block():
    assert Parser("void main() { int x; { x = 1; } }").parse() == "success"


def test_PX_023_function_missing_name():
    assert Parser("int (int a) { return a; }").parse() == "Error on line 1 col 4: ("


def test_PX_024_function_missing_body_braces():
    assert Parser("int f();").parse() == "Error on line 1 col 7: ;"


def test_PX_025_function_missing_closing_brace():
    assert Parser("int f(){ return 1;").parse() == "Error on line 1 col 18: <EOF>"


def test_PX_026_function_missing_closing_paren():
    assert Parser("int f( { return 1; }").parse() == "Error on line 1 col 7: {"


def test_PX_027_param_missing_type():
    assert Parser("int f(x) { return x; }").parse() == "Error on line 1 col 7: )"


def test_PX_028_param_missing_name():
    assert Parser("int f(int) { return 1; }").parse() == "Error on line 1 col 9: )"


def test_PX_029_param_list_missing_comma():
    assert Parser("int f(int a int b) { return a+b; }").parse() == "Error on line 1 col 12: int"


def test_PX_030_trailing_comma_in_params():
    assert Parser("int f(int a, ) { return a; }").parse() == "Error on line 1 col 13: )"


def test_PX_031_no_return_type_but_has_return():
    assert Parser("f() { return 1; }").parse() == "success"


def test_PX_032_no_return_type_and_no_return():
    assert Parser("f() { int x; x = 1; }").parse() == "success"


def test_PX_033_void_function_returning_expression():
    assert Parser("void f() { return 1; }").parse() == "Error on line 1 col 18: 1"


def test_PX_034_non_void_function_missing_return_statement():
    assert Parser("int f() { int x; x = 1; }").parse() == "Error on line 1 col 24: }"


# ========== Structs ==========
def test_PX_035_struct_with_3_fields():
    assert Parser("struct S { int a; float b; bool c; };").parse() == "success"


def test_PX_036_struct_with_empty_body_edge_success():
    assert Parser("struct Empty {};").parse() == "success"


def test_PX_037_two_struct_declarations():
    assert Parser("struct A{int x;}; struct B{int y;};").parse() == "success"


def test_PX_038_struct_variable_declaration():
    assert Parser("struct Point { int x; int y; }; void main(){ Point p; }").parse() == "success"


def test_PX_039_struct_variable_declaration_multiple():
    source = "struct Point { int x; int y; }; void main(){ Point p1; Point p2; }"
    assert Parser(source).parse() == "success"


def test_PX_040_struct_initialization_with_braces():
    source = "struct Point { int x; int y; }; void main(){ Point p = {1, 2}; }"
    assert Parser(source).parse() == "success"


def test_PX_041_struct_initialization_with_spaces_newlines_edge_success():
    source = "struct P{int x; int y;}; void main(){ P p = { 1 , 2 }; }"
    assert Parser(source).parse() == "success"


def test_PX_042_struct_member_access_read():
    source = "struct P{int x; int y;}; void main(){ P p; printInt(p.x); }"
    assert Parser(source).parse() == "success"


def test_PX_043_struct_member_access_assign():
    source = "struct P{int x; int y;}; void main(){ P p; p.x = 1; }"
    assert Parser(source).parse() == "success"


def test_PX_044_struct_member_access_chain_in_expr():
    source = "struct P{int x; int y;}; void main(){ P p; p.x = p.y = 1; }"
    assert Parser(source).parse() == "success"


def test_PX_045_struct_missing_semicolon_after_declaration():
    assert Parser("struct P{int x; int y;}").parse() == "Error on line 1 col 23: <EOF>"


def test_PX_046_struct_missing_closing_brace():
    assert Parser("struct P{int x; int y;").parse() == "Error on line 1 col 22: <EOF>"


def test_PX_047_struct_field_missing_semicolon():
    assert Parser("struct P{int x int y;};").parse() == "Error on line 1 col 15: int"


def test_PX_048_struct_variable_before_struct_declared_edge_expect_fail():
    assert Parser("struct P{int x; int y;}; void main(){ P p; }").parse() == "success"


def test_PX_049_struct_init_wrong_arity():
    source = "struct P{int x; int y;}; void main(){ P p = {1, 2, 3}; }"
    assert Parser(source).parse() == "success"


def test_PX_050_struct_member_access_missing_identifier():
    source = "struct P{int x;}; void main(){ P p; p. = 1; }"
    assert Parser(source).parse() == "Error on line 1 col 39: ="


def test_PX_051_struct_member_access_missing_dot():
    source = "struct P{int x;}; void main(){ P p; p.x = 1; }"
    assert Parser(source).parse() == "success"


# ========== Variable declarations ==========
def test_PX_052_auto_with_init_int_literal():
    assert Parser("void main() { auto x = 5; }").parse() == "success"


def test_PX_053_auto_with_init_float_literal():
    assert Parser("void main() { auto x = 3.14; }").parse() == "success"


def test_PX_054_auto_with_init_bool_literal():
    assert Parser("void main() { auto x = true; }").parse() == "success"


def test_PX_055_auto_with_init_string_literal():
    assert Parser('void main() { auto s = "Hi"; }').parse() == "success"


def test_PX_056_auto_with_init_from_expression():
    assert Parser("void main() { auto x = 1 + 2; }").parse() == "success"


def test_PX_057_auto_without_init_should_fail_per_plan():
    assert Parser("void main() { auto x; }").parse() == "success"


def test_PX_058_explicit_type_with_init():
    assert Parser("void main() { int x = 5; }").parse() == "success"


def test_PX_059_explicit_type_without_init():
    assert Parser("void main() { int x; }").parse() == "success"


def test_PX_060_explicit_float_with_init():
    assert Parser("void main() { float f = 1.0; }").parse() == "success"


def test_PX_061_explicit_bool_without_init():
    assert Parser("void main() { bool b; }").parse() == "success"


def test_PX_062_multiple_declarations_in_one_line():
    assert Parser("void main() { int a; int b; }").parse() == "success"


def test_PX_063_declaration_missing_semicolon():
    assert Parser("void main() { int x }").parse() == "Error on line 1 col 20: }"


def test_PX_064_init_missing_expression():
    assert Parser("void main() { int x = ; }").parse() == "Error on line 1 col 22: ;"


def test_PX_065_auto_init_with_struct_literal_edge_success():
    source = "struct P{int x; int y;}; void main(){ auto p = {1,2}; }"
    assert Parser(source).parse() == "success"


# ========== Expressions & precedence ==========
def test_PX_066_arithmetic_expression_in_assignment():
    assert Parser("void main() { int x; x = 1 + 2 - 3; }").parse() == "success"


def test_PX_067_arithmetic_with_precedence():
    assert Parser("void main() { int x; x = 1 + 2 * 3; }").parse() == "success"


def test_PX_068_arithmetic_with_parentheses():
    assert Parser("void main() { int x; x = (1 + 2) * 3; }").parse() == "success"


def test_PX_069_modulo_operator():
    assert Parser("void main() { int x; x = 10 % 3; }").parse() == "success"


def test_PX_070_relational_expression():
    assert Parser("void main() { bool b; b = 1 < 2; }").parse() == "success"


def test_PX_071_relational_chaining():
    assert Parser("void main() { bool b; b = 1 < 2 < 3; }").parse() == "success"


def test_PX_072_logical_AND_OR_NOT():
    assert Parser("void main() { bool b; b = !(1 < 2) || (1 && 0); }").parse() == "success"


def test_PX_073_expression_missing_operand():
    assert Parser("void main() { int x; x = 1 + ; }").parse() == "Error on line 1 col 29: ;"


def test_PX_074_expression_missing_closing_paren():
    assert Parser("void main() { int x; x = (1 + 2; }").parse() == "Error on line 1 col 31: ;"


def test_PX_075_expression_invalid_operator_sequence():
    assert Parser("void main() { int x; x = 1 ** 2; }").parse() == "Error on line 1 col 28: *"


# ========== Calls ==========
def test_PX_076_function_call_statement_no_args():
    assert Parser("void main() { foo(); }").parse() == "success"


def test_PX_077_function_call_with_args():
    assert Parser("void main() { printInt(1); }").parse() == "success"


def test_PX_078_function_call_used_in_expression():
    source = "int inc(int x){return x+1;} void main(){int a; a = inc(1);}"
    assert Parser(source).parse() == "success"


def test_PX_079_call_with_many_args():
    assert Parser("void main() { bar(1,2,3,4); }").parse() == "success"


def test_PX_080_call_with_trailing_comma():
    assert Parser("void main() { foo(1,); }").parse() == "Error on line 1 col 20: )"


def test_PX_081_call_missing_closing_paren():
    assert Parser("void main() { foo(1,2; }").parse() == "Error on line 1 col 21: ;"


def test_PX_082_call_missing_comma_between_args():
    assert Parser("void main() { foo(1 2); }").parse() == "Error on line 1 col 20: 2"


def test_PX_083_call_in_condition():
    source = "int ok(){return 1;} void main(){ if (ok()) printInt(1); }"
    assert Parser(source).parse() == "success"


# ========== More precedence & grouping ==========
def test_PX_084_operator_precedence_mul_binds_tighter_than_add():
    assert Parser("void main() { int x; x = 1 + 2 * 3 + 4; }").parse() == "success"


def test_PX_085_operator_precedence_relational_vs_arithmetic():
    assert Parser("void main() { bool b; b = 1 + 2 < 3 * 4; }").parse() == "success"


def test_PX_086_operator_precedence_logical_vs_relational():
    assert Parser("void main() { bool b; b = 1 == 2 && 3 < 4 || 0; }").parse() == "success"


def test_PX_087_operator_precedence_with_unary_minus():
    assert Parser("void main() { int x; x = -1 * 2 + 3; }").parse() == "success"


def test_PX_088_ambiguous_precedence_without_operator():
    assert Parser("void main() { int x; x = 1 2; }").parse() == "Error on line 1 col 27: 2"


def test_PX_089_deeply_nested_parentheses_edge_success():
    assert Parser("void main() { int x; x = (((1+2)*3)*-4); }").parse() == "success"


# ========== Blocks & conditionals ==========
def test_PX_090_block_statement_empty():
    assert Parser("void main() { {} }").parse() == "success"


def test_PX_091_block_statement_multiple_statements():
    assert Parser("void main() { { int x = 1; printInt(x); } }").parse() == "success"


def test_PX_092_if_with_else():
    assert Parser("void main() { if (1) printInt(1); else printInt(0); }").parse() == "success"


def test_PX_093_if_with_block_bodies():
    source = "void main() { if (1) { printInt(1); } else { printInt(0); } }"
    assert Parser(source).parse() == "success"


def test_PX_094_if_missing_condition_parens():
    assert Parser("void main() { if 1 printInt(1); }").parse() == "Error on line 1 col 17: 1"


def test_PX_095_if_missing_statement():
    assert Parser("void main() { if (1) }").parse() == "Error on line 1 col 21: }"


# ========== Loops ==========
def test_PX_096_while_with_block():
    assert Parser("void main() { while (1) { break; } }").parse() == "success"


def test_PX_097_while_missing_closing_paren():
    assert Parser("void main() { while (1 printInt(1); }").parse() == "Error on line 1 col 23: printInt"


def test_PX_098_for_loop_full_form():
    assert Parser("void main() { for (auto i = 0; i < 10; ++i) printInt(i); }").parse() == "success"


def test_PX_099_for_loop_with_block_body():
    assert Parser("void main() { for (auto i = 0; i < 10; ++i) { printInt(i); } }").parse() == "success"


def test_PX_100_for_missing_semicolons():
    assert Parser("void main() { for (auto i=0 i<10 ++i) printInt(i); }").parse() == "Error on line 1 col 28: i"


def test_PX_101_for_missing_parens():
    assert Parser("void main() { for auto i=0; i<10; ++i printInt(i); }").parse() == "Error on line 1 col 18: auto"


# ========== Switch / break / continue / return ==========
def test_PX_102_switch_with_one_case():
    assert Parser("void main() { switch(1) { case 1: printInt(1); break; } }").parse() == "success"


def test_PX_103_switch_with_multiple_cases_and_default():
    source = "void main() { switch(1) { case 1: break; case 2: break; default: break; } }"
    assert Parser(source).parse() == "success"


def test_PX_104_switch_case_missing_colon():
    assert Parser("void main() { switch(1){ case 1 printInt(1); break; } }").parse() == "Error on line 1 col 32: printInt"


def test_PX_105_switch_missing_break_edge_success():
    assert Parser("void main() { switch(1){ case 1: printInt(1); } }").parse() == "success"


def test_PX_106_break_outside_loop_switch_edge_expect_fail():
    assert Parser("void main() { break; }").parse() == "Error on line 1 col 14: break"


def test_PX_107_continue_inside_while():
    assert Parser("void main() { while(1) { continue; } }").parse() == "success"


def test_PX_108_continue_outside_loop_edge_expect_fail():
    assert Parser("void main() { continue; }").parse() == "Error on line 1 col 14: continue"


def test_PX_109_return_with_expression_in_int_function():
    assert Parser("int f() { return 1+2*3; }").parse() == "success"


def test_PX_110_expression_statement():
    assert Parser("void main() { 1 + 2 * 3; }").parse() == "success"
