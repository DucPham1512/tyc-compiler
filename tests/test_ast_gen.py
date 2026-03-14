"""
AST generation test cases for TyC compiler.
100 test cases following TestExpectedGot pattern.
"""

import pytest
from tests.utils import ASTGenerator


def _generate(source: str):
    ast = ASTGenerator(source).generate()
    assert not isinstance(ast, str), ast
    return str(ast)


# ===========================================================================
# AX_001 - Program and Struct Declarations
# ===========================================================================

def test_AX_001_empty_program():
    assert _generate("") == "Program([])"


def test_AX_002_struct_no_members():
    assert _generate("struct Empty {};") == \
        "Program([StructDecl(Empty, [])])"


def test_AX_003_struct_single_int_member():
    assert _generate("struct S { int x; };") == \
        "Program([StructDecl(S, [MemberDecl(IntType(), x)])])"


def test_AX_004_struct_single_float_member():
    assert _generate("struct S { float x; };") == \
        "Program([StructDecl(S, [MemberDecl(FloatType(), x)])])"


def test_AX_005_struct_single_string_member():
    assert _generate("struct S { string x; };") == \
        "Program([StructDecl(S, [MemberDecl(StringType(), x)])])"


def test_AX_006_struct_multiple_members():
    assert _generate("struct Point { int x; int y; };") == \
        "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"


def test_AX_007_struct_mixed_members():
    assert _generate("struct Person { string name; int age; float height; };") == \
        "Program([StructDecl(Person, [MemberDecl(StringType(), name), MemberDecl(IntType(), age), MemberDecl(FloatType(), height)])])"


def test_AX_008_struct_member_is_struct_type():
    assert _generate("struct A { Point p; };") == \
        "Program([StructDecl(A, [MemberDecl(StructType(Point), p)])])"


def test_AX_009_multiple_struct_declarations():
    assert _generate("struct A { int x; }; struct B { float y; };") == \
        "Program([StructDecl(A, [MemberDecl(IntType(), x)]), StructDecl(B, [MemberDecl(FloatType(), y)])])"


def test_AX_010_struct_and_function_order():
    assert _generate("struct S { int x; }; void main() {}") == \
        "Program([StructDecl(S, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], [])])"


# ===========================================================================
# AX_011 - Function Declarations
# ===========================================================================

def test_AX_011_void_function_no_params():
    assert _generate("void main() {}") == \
        "Program([FuncDecl(VoidType(), main, [], [])])"


def test_AX_012_int_function_no_params():
    assert _generate("int f() { return 1; }") == \
        "Program([FuncDecl(IntType(), f, [], [ReturnStmt(return IntLiteral(1))])])"


def test_AX_013_float_function_no_params():
    assert _generate("float f() { return 1.0; }") == \
        "Program([FuncDecl(FloatType(), f, [], [ReturnStmt(return FloatLiteral(1.0))])])"


def test_AX_014_string_function_no_params():
    assert _generate('string f() { return "hi"; }') == \
        'Program([FuncDecl(StringType(), f, [], [ReturnStmt(return StringLiteral(\'hi\'))])])'


def test_AX_015_type_infer_function_return_none():
    assert _generate("f() { return 1; }") == \
        "Program([FuncDecl(auto, f, [], [ReturnStmt(return IntLiteral(1))])])"


def test_AX_016_void_function_one_param():
    assert _generate("void f(int x) {}") == \
        "Program([FuncDecl(VoidType(), f, [Param(IntType(), x)], [])])"


def test_AX_017_function_two_params():
    assert _generate("int add(int x, int y) { return x + y; }") == \
        "Program([FuncDecl(IntType(), add, [Param(IntType(), x), Param(IntType(), y)], [ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))])])"


def test_AX_018_function_struct_param():
    assert _generate("void f(Point p) {}") == \
        "Program([FuncDecl(VoidType(), f, [Param(StructType(Point), p)], [])])"


def test_AX_019_function_struct_return_type():
    assert _generate("Point f() { return p; }") == \
        "Program([FuncDecl(StructType(Point), f, [], [ReturnStmt(return Identifier(p))])])"


def test_AX_020_multiple_functions():
    assert _generate("void f() {} void g() {}") == \
        "Program([FuncDecl(VoidType(), f, [], []), FuncDecl(VoidType(), g, [], [])])"


# ===========================================================================
# AX_021 - Variable Declarations
# ===========================================================================

def test_AX_021_var_decl_int_no_init():
    assert _generate("void main() { int x; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x)])])"


def test_AX_022_var_decl_float_no_init():
    assert _generate("void main() { float x; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(FloatType(), x)])])"


def test_AX_023_var_decl_string_no_init():
    assert _generate("void main() { string x; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(StringType(), x)])])"


def test_AX_024_var_decl_int_with_init():
    assert _generate("void main() { int x = 5; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5))])])"


def test_AX_025_var_decl_auto_with_init():
    assert _generate("void main() { auto x = 10; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, x = IntLiteral(10))])])"


def test_AX_026_var_decl_auto_no_init():
    assert _generate("void main() { auto x; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, x)])])"


def test_AX_027_var_decl_struct_no_init():
    assert _generate("void main() { Point p; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p)])])"


def test_AX_028_var_decl_struct_with_init():
    assert _generate("void main() { Point p = {1, 2}; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)}))])])"


def test_AX_029_var_decl_float_with_init():
    assert _generate("void main() { float x = 3.14; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(FloatType(), x = FloatLiteral(3.14))])])"


def test_AX_030_multiple_var_decls():
    assert _generate("void main() { int x; int y; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x), VarDecl(IntType(), y)])])"


# ===========================================================================
# AX_031 - Return Statements
# ===========================================================================

def test_AX_031_void_return():
    assert _generate("void main() { return; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ReturnStmt(return)])])"


def test_AX_032_return_int_literal():
    assert _generate("int f() { return 1; }") == \
        "Program([FuncDecl(IntType(), f, [], [ReturnStmt(return IntLiteral(1))])])"


def test_AX_033_return_float_literal():
    assert _generate("float f() { return 1.5; }") == \
        "Program([FuncDecl(FloatType(), f, [], [ReturnStmt(return FloatLiteral(1.5))])])"


def test_AX_034_return_string_literal():
    assert _generate('string f() { return "hello"; }') == \
        "Program([FuncDecl(StringType(), f, [], [ReturnStmt(return StringLiteral('hello'))])])"


def test_AX_035_return_identifier():
    assert _generate("int f(int x) { return x; }") == \
        "Program([FuncDecl(IntType(), f, [Param(IntType(), x)], [ReturnStmt(return Identifier(x))])])"


def test_AX_036_return_binary_expr():
    assert _generate("int f(int x) { return x + 1; }") == \
        "Program([FuncDecl(IntType(), f, [Param(IntType(), x)], [ReturnStmt(return BinaryOp(Identifier(x), +, IntLiteral(1)))])])"


def test_AX_037_return_negative_int():
    assert _generate("int f() { return -5; }") == \
        "Program([FuncDecl(IntType(), f, [], [ReturnStmt(return IntLiteral(-5))])])"


def test_AX_038_return_function_call():
    assert _generate("int f() { return g(); }") == \
        "Program([FuncDecl(IntType(), f, [], [ReturnStmt(return FuncCall(g, []))])])"


def test_AX_039_return_member_access():
    assert _generate("int f(Point p) { return p.x; }") == \
        "Program([FuncDecl(IntType(), f, [Param(StructType(Point), p)], [ReturnStmt(return MemberAccess(Identifier(p).x))])])"


def test_AX_040_return_assign_expr():
    assert _generate("int f() { int x; return x = 1; }") == \
        "Program([FuncDecl(IntType(), f, [], [VarDecl(IntType(), x), ReturnStmt(return AssignExpr(Identifier(x) = IntLiteral(1)))])])"


# ===========================================================================
# AX_041 - If Statements
# ===========================================================================

def test_AX_041_if_no_else_braceless():
    assert _generate("void main() { if (1) x = 1; }") == \
        "Program([FuncDecl(VoidType(), main, [], [IfStmt(if IntLiteral(1) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))])])"


def test_AX_042_if_with_else_braceless():
    assert _generate("void main() { if (1) x = 1; else x = 2; }") == \
        "Program([FuncDecl(VoidType(), main, [], [IfStmt(if IntLiteral(1) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), else ExprStmt(AssignExpr(Identifier(x) = IntLiteral(2))))])])"


def test_AX_043_if_with_block_body():
    assert _generate("void main() { if (1) { x = 1; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [IfStmt(if IntLiteral(1) then BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))]))])])"


def test_AX_044_if_else_with_blocks():
    assert _generate("void main() { if (1) { x = 1; } else { x = 2; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [IfStmt(if IntLiteral(1) then BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))]), else BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(2)))]))])])"


def test_AX_045_nested_if():
    assert _generate("void main() { if (1) if (2) x = 1; }") == \
        "Program([FuncDecl(VoidType(), main, [], [IfStmt(if IntLiteral(1) then IfStmt(if IntLiteral(2) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"


def test_AX_046_if_with_return_in_block():
    assert _generate("int f() { if (1) { return 1; } return 0; }") == \
        "Program([FuncDecl(IntType(), f, [], [IfStmt(if IntLiteral(1) then BlockStmt([ReturnStmt(return IntLiteral(1))])), ReturnStmt(return IntLiteral(0))])])"


# ===========================================================================
# AX_047 - While Statements
# ===========================================================================

def test_AX_047_while_braceless():
    assert _generate("void main() { while (1) x = 1; }") == \
        "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while IntLiteral(1) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))])])"


def test_AX_048_while_with_block():
    assert _generate("void main() { while (1) { x = 1; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while IntLiteral(1) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))]))])])"


def test_AX_049_while_empty_block():
    assert _generate("void main() { while (1) {} }") == \
        "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while IntLiteral(1) do BlockStmt([]))])])"


def test_AX_050_while_with_break():
    assert _generate("void main() { while (1) { break; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while IntLiteral(1) do BlockStmt([BreakStmt()]))])])"


def test_AX_051_while_with_continue():
    assert _generate("void main() { while (1) { continue; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while IntLiteral(1) do BlockStmt([ContinueStmt()]))])])"


# ===========================================================================
# AX_052 - For Statements
# ===========================================================================

def test_AX_052_for_empty_parts():
    assert _generate("void main() { for (;;) {} }") == \
        "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; None do BlockStmt([]))])])"


def test_AX_053_for_with_var_init():
    assert _generate("void main() { for (auto i = 0; i < 3; i++) {} }") == \
        "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(auto, i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do BlockStmt([]))])])"


def test_AX_054_for_with_expr_init():
    assert _generate("void main() { int i; for (i = 0; i < 3; ++i) {} }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i), ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PrefixOp(++Identifier(i)) do BlockStmt([]))])])"


def test_AX_055_for_no_condition():
    assert _generate("void main() { for (auto i = 0;; i++) {} }") == \
        "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(auto, i = IntLiteral(0)); None; PostfixOp(Identifier(i)++) do BlockStmt([]))])])"


def test_AX_056_for_no_update():
    assert _generate("void main() { for (auto i = 0; i < 3;) {} }") == \
        "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(auto, i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(3)); None do BlockStmt([]))])])"


def test_AX_057_for_with_body_stmt():
    assert _generate("void main() { for (;;) x = 1; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; None do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))])])"


# ===========================================================================
# AX_058 - Switch Statements
# ===========================================================================

def test_AX_058_switch_empty():
    assert _generate("void main() { switch (x) {} }") == \
        "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(x) cases [])])])"


def test_AX_059_switch_single_case():
    assert _generate("void main() { switch (x) { case 1: x = 1; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))])])])])"


def test_AX_060_switch_case_with_break():
    assert _generate("void main() { switch (x) { case 1: break; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])])])])"


def test_AX_061_switch_with_default():
    assert _generate("void main() { switch (x) { default: x = 0; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(x) cases [], default DefaultStmt(default: [ExprStmt(AssignExpr(Identifier(x) = IntLiteral(0)))]))])])"


def test_AX_062_switch_case_and_default():
    assert _generate("void main() { switch (x) { case 1: break; default: x = 0; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])], default DefaultStmt(default: [ExprStmt(AssignExpr(Identifier(x) = IntLiteral(0)))]))])])"


def test_AX_063_switch_fallthrough_labels():
    assert _generate("void main() { switch (x) { case 1: case 2: x = 1; break; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): []), CaseStmt(case IntLiteral(2): [ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), BreakStmt()])])])])"


def test_AX_064_switch_multiple_cases():
    assert _generate("void main() { switch (x) { case 1: break; case 2: break; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])])])])"


# ===========================================================================
# AX_065 - Expressions
# ===========================================================================

def test_AX_065_binary_add():
    assert _generate("void main() { x = 1 + 2; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(IntLiteral(1), +, IntLiteral(2))))])])"


def test_AX_066_binary_sub():
    assert _generate("void main() { x = 1 - 2; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(IntLiteral(1), -, IntLiteral(2))))])])"


def test_AX_067_binary_mul():
    assert _generate("void main() { x = 2 * 3; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(IntLiteral(2), *, IntLiteral(3))))])])"


def test_AX_068_binary_div():
    assert _generate("void main() { x = 6 / 2; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(IntLiteral(6), /, IntLiteral(2))))])])"


def test_AX_069_binary_mod():
    assert _generate("void main() { x = 5 % 2; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(IntLiteral(5), %, IntLiteral(2))))])])"


def test_AX_070_binary_eq():
    assert _generate("void main() { x = a == b; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ==, Identifier(b))))])])"


def test_AX_071_binary_neq():
    assert _generate("void main() { x = a != b; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), !=, Identifier(b))))])])"


def test_AX_072_binary_lt():
    assert _generate("void main() { x = a < b; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), <, Identifier(b))))])])"


def test_AX_073_binary_logical_and():
    assert _generate("void main() { x = a && b; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), &&, Identifier(b))))])])"


def test_AX_074_binary_logical_or():
    assert _generate("void main() { x = a || b; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ||, Identifier(b))))])])"


def test_AX_075_prefix_not():
    assert _generate("void main() { x = !a; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = PrefixOp(!Identifier(a))))])])"


def test_AX_076_prefix_neg():
    assert _generate("void main() { x = -a; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = PrefixOp(-Identifier(a))))])])"


def test_AX_077_prefix_inc():
    assert _generate("void main() { ++x; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++Identifier(x)))])])"


def test_AX_078_prefix_dec():
    assert _generate("void main() { --x; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(--Identifier(x)))])])"


def test_AX_079_postfix_inc():
    assert _generate("void main() { x++; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(x)++))])])"


def test_AX_080_postfix_dec():
    assert _generate("void main() { x--; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(x)--))])])"


def test_AX_081_member_access():
    assert _generate("void main() { x = p.x; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = MemberAccess(Identifier(p).x)))])])"


def test_AX_082_chained_member_access():
    assert _generate("void main() { x = a.b.c; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = MemberAccess(MemberAccess(Identifier(a).b).c)))])])"


def test_AX_083_function_call_no_args():
    assert _generate("void main() { f(); }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, []))])])"


def test_AX_084_function_call_with_args():
    assert _generate("void main() { f(1, 2); }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, [IntLiteral(1), IntLiteral(2)]))])])"


# ===========================================================================
# AX_085 - Precedence and Associativity
# ===========================================================================

def test_AX_085_precedence_add_over_or():
    assert _generate("void main() { x = a || b + c; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ||, BinaryOp(Identifier(b), +, Identifier(c)))))])])"


def test_AX_086_precedence_mul_over_add():
    assert _generate("void main() { x = a + b * c; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c)))))])])"


def test_AX_087_left_associativity_add():
    assert _generate("void main() { x = a + b + c; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), +, Identifier(c))))])])"


def test_AX_088_right_associativity_assign():
    assert _generate("void main() { a = b = 1; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = IntLiteral(1))))])])"


def test_AX_089_parentheses_override_precedence():
    assert _generate("void main() { x = (a + b) * c; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, Identifier(c))))])])"


# ===========================================================================
# AX_090 - Block Statements and Nesting
# ===========================================================================

def test_AX_090_nested_block_in_void_func():
    assert _generate("void main() { { int x; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [BlockStmt([VarDecl(IntType(), x)])])])"


def test_AX_091_nested_block_with_return():
    assert _generate("int f() { { return 1; } }") == \
        "Program([FuncDecl(IntType(), f, [], [BlockStmt([ReturnStmt(return IntLiteral(1))])])])"


def test_AX_092_deeply_nested_blocks():
    assert _generate("void main() { { { x = 1; } } }") == \
        "Program([FuncDecl(VoidType(), main, [], [BlockStmt([BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))])])])])"


def test_AX_093_mixed_decls_and_stmts():
    assert _generate("void main() { int x; x = 1; int y; y = 2; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x), ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), VarDecl(IntType(), y), ExprStmt(AssignExpr(Identifier(y) = IntLiteral(2)))])])"


def test_AX_094_struct_literal_nested():
    assert _generate("void main() { auto p = {1, {2, 3}}; }") == \
        "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, p = StructLiteral({IntLiteral(1), StructLiteral({IntLiteral(2), IntLiteral(3)})}))])])"


def test_AX_095_member_assign_lvalue():
    assert _generate("void main() { p.x = 1; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = IntLiteral(1)))])])"


def test_AX_096_function_call_as_arg():
    assert _generate("void main() { f(g(1)); }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, [FuncCall(g, [IntLiteral(1)])]))])])"


def test_AX_097_chained_assign_three_vars():
    assert _generate("void main() { a = b = c = 1; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = IntLiteral(1)))))])])"


def test_AX_098_binary_ge():
    assert _generate("void main() { x = a >= b; }") == \
        "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), >=, Identifier(b))))])])"


def test_AX_099_for_with_decrement_update():
    assert _generate("void main() { for (auto i = 10; i > 0; i--) {} }") == \
        "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(auto, i = IntLiteral(10)); BinaryOp(Identifier(i), >, IntLiteral(0)); PostfixOp(Identifier(i)--) do BlockStmt([]))])])"


def test_AX_100_switch_default_empty_stmts():
    assert _generate("void main() { switch (x) { case 1: break; default: break; } }") == \
        "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])], default DefaultStmt(default: [BreakStmt()]))])])"