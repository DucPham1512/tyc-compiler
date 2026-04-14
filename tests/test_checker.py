"""
Test cases for TyC Static Semantic Checker

This module contains 105 test cases covering all aspects of static semantic analysis
for the TyC programming language, as required by the Assignment 3 specification.
"""

from tests.utils import Checker

# ============================================================================
# Valid Programs (001 - 030)
# ============================================================================

def test_001():
    """Valid: Basic variable and arithmetic"""
    source = "void main() { int x = 5; int y = x + 10; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_002():
    """Valid: Float arithmetic"""
    source = "void main() { float f = 1.5; float g = f * 2.0; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_003():
    """Valid: String variable"""
    source = "void main() { string s = \"hello\"; printString(s); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_004():
    """Valid: Empty main"""
    source = "void main() {}"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_005():
    """Valid: Mixed int and float arithmetic"""
    source = "void main() { int x = 5; float f = x + 1.5; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_006():
    """Valid: Boolean-like int usage in if"""
    source = "void main() { int x = 1; if (x) { x = 0; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_007():
    """Valid: Nested blocks"""
    source = "void main() { { int x = 5; } { float x = 10.0; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_008():
    """Valid: Prefix and postfix increment"""
    source = "void main() { int x = 0; ++x; x++; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_009():
    """Valid: Modulo operator"""
    source = "void main() { int x = 10 % 3; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_010():
    """Valid: Multiple declarations in one function"""
    source = "void main() { int a; float b; string c; a=1; b=1.0; c=\"1\"; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_011():
    """Valid: auto with init"""
    source = "void main() { auto x = 5; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_012():
    """Valid: auto inferred from assignment"""
    source = "void main() { auto x; x = 5; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_013():
    """Valid: auto inferred from expression"""
    source = "void main() { auto x; int y = 10; x = y + 5; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_014():
    """Valid: auto inferred from function call"""
    source = "int get() { return 1; } void main() { auto x = get(); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_015():
    """Valid: chained auto inference"""
    source = "void main() { auto x = 5; auto y = x; auto z = y; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_016():
    """Valid: auto in for loop init"""
    source = "void main() { for (auto i = 0; i < 10; ++i) {} }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_017():
    """Valid: auto inferred as float"""
    source = "void main() { auto f; f = 1.5; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_018():
    """Valid: auto inferred from printString"""
    source = "void main() { auto s; s = \"hi\"; printString(s); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_019():
    """Valid: complex auto inference in expression"""
    source = "void main() { auto x; auto y = (x = 5) + 3; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_020():
    """Valid: Struct declaration and use"""
    source = "struct S { int x; }; void main() { S s; s.x = 1; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_021():
    """Valid: Function with parameters"""
    source = "int add(int a, int b) { return a + b; } void main() { add(1, 2); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_022():
    """Valid: Struct literal initialization"""
    source = "struct P { int x; int y; }; void main() { P p = {1, 2}; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_023():
    """Valid: Nested struct"""
    source = "struct A { int x; }; struct B { A a; }; void main() { B b = {{1}}; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_024():
    """Valid: auto return type inference"""
    source = "foo(int x) { return x + 1; } void main() { int y = foo(5); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_025():
    """Valid: recursion"""
    source = "int fib(int n) { if(n <= 1) return n; return fib(n - 1) + fib(n - 2); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_026():
    """Valid: built-in constants and IO"""
    source = "void main() { printInt(readInt()); printFloat(readFloat()); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_027():
    """Valid: complex for loop"""
    source = "void main() { int i; for(i=0; i<10; i = i + 1) { printInt(i); } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_028():
    """Valid: switch case fallthrough"""
    source = "void main() { switch(1) { case 1: case 2: printInt(1); break; default: printInt(0); } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_029():
    """Valid: shadowing outer variable"""
    source = "void main() { int x = 1; { float x = 1.0; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_030():
    """Valid: struct returning function call in member access"""
    source = "struct S{int x;}; S get() { S s = {1}; return s; } void main() { int y = get().x; }"
    assert Checker(source).check_from_source() == "Static checking passed"

# ============================================================================
# Redeclared Errors (031 - 045)
# ============================================================================

def test_031():
    """Error: Redeclared Variable"""
    source = "void main() { int x; int x; }"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_032():
    """Error: Redeclared Function"""
    source = "void f(){} void f(){}"
    assert "Redeclared(Function, f)" in Checker(source).check_from_source()

def test_033():
    """Error: Redeclared Struct"""
    source = "struct S{}; struct S{};"
    assert "Redeclared(Struct, S)" in Checker(source).check_from_source()

def test_034():
    """Error: Redeclared Parameter"""
    source = "void f(int x, int x){}"
    assert "Redeclared(Parameter, x)" in Checker(source).check_from_source()

def test_035():
    """Error: Redeclared variable in same block"""
    source = "void main() { { int x; float x; } }"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_036():
    """Error: Redeclared variable shadowing parameter in outermost block"""
    source = "void f(int x) { int x; }"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_037():
    """Error: Redeclared struct member"""
    source = "struct S { int x; float x; };"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_038():
    """Error: Redeclared variable in nested blocks (re-declaring in inner block)"""
    source = "void main() { { int y; int y; } }"
    assert "Redeclared(Variable, y)" in Checker(source).check_from_source()

def test_039():
    """Valid: Shadowing in nested loop (allowed in TyC)"""
    source = "void main() { for(int i=0;i<10;i++) { { int i = 5; } } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_040():
    """Valid: Different variables in different switch cases using blocks"""
    source = "void main() { switch(1) { case 1: { int x; } case 2: { int x; } } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_041():
    """Valid: Shadowing in for loop body"""
    source = "void main() { for(int i=0; i<10; i++) { int i = 100; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

# ============================================================================
# Undeclared Errors (046 - 060)
# ============================================================================

def test_046():
    """Error: Undeclared Identifier"""
    source = "void main() { x = 1; }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

def test_047():
    """Error: Undeclared Function"""
    source = "void main() { unknown(); }"
    assert "UndeclaredFunction(unknown)" in Checker(source).check_from_source()

def test_048():
    """Error: Undeclared Struct"""
    source = "void main() { Unknown u; }"
    assert "UndeclaredStruct(Unknown)" in Checker(source).check_from_source()

def test_049():
    """Error: Undeclared variable in expression"""
    source = "void main() { int y = x + 1; }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

def test_050():
    """Error: Undeclared identifier in nested scope"""
    source = "void main() { { int x; } x = 1; }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

def test_051():
    """Error: Function called before declaration"""
    source = "void main() { f(); } void f(){}"
    assert "UndeclaredFunction(f)" in Checker(source).check_from_source()

def test_052():
    """Error: Struct used before declaration"""
    source = "void main() { S s; } struct S{};"
    assert "UndeclaredStruct(S)" in Checker(source).check_from_source()

def test_053():
    """Error: Member access on undeclared variable"""
    source = "struct S{int x;}; void main() { s.x = 1; }"
    assert "UndeclaredIdentifier(s)" in Checker(source).check_from_source()

def test_054():
    """Error: Function called with undeclared identifier as arg"""
    source = "void f(int x){} void main() { f(y); }"
    assert "UndeclaredIdentifier(y)" in Checker(source).check_from_source()

def test_055():
    """Error: Using variable from another function"""
    source = "void a() { int x; } void b() { x = 1; }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

# ============================================================================
# Type Cannot Be Inferred (061 - 069)
# ============================================================================

def test_061():
    """Error: auto with no info"""
    source = "void main() { auto x; }"
    assert "TypeCannotBeInferred(x)" in Checker(source).check_from_source()

def test_062():
    """Error: auto x = y where both are auto"""
    source = "void main() { auto x; auto y; x = y; }"
    assert "TypeCannotBeInferred(x)" in Checker(source).check_from_source()

def test_063():
    """Error: auto result = x + y where both are auto"""
    source = "void main() { auto x; auto y; auto z = x + y; }"
    assert "TypeCannotBeInferred(x)" in Checker(source).check_from_source()

def test_064():
    """Error: auto used in if condition but never inferred"""
    source = "void main() { auto flag; if(flag) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_065():
    """Error: auto never inferred at end of block"""
    source = "void main() { auto x; { int y; } }"
    assert "TypeCannotBeInferred(x)" in Checker(source).check_from_source()

def test_067():
    """Error: auto member access base unknown"""
    source = "void main() { auto x; x.m = 1; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_068():
    """Error: Circular auto inference"""
    source = "void main() { auto x; auto y; x = y; y = x; }"
    assert "TypeCannotBeInferred(x)" in Checker(source).check_from_source()

def test_069():
    """Error: auto inferred from undeclared identifier"""
    source = "void main() { auto x = y; }"
    assert "UndeclaredIdentifier(y)" in Checker(source).check_from_source()

# ============================================================================
# Type Mismatch In Statement (070 - 085)
# ============================================================================

def test_070():
    """Error: If condition float"""
    source = "void main() { if(1.5) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_071():
    """Error: While condition string"""
    source = "void main() { while(\"hi\") {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_072():
    """Error: For condition float"""
    source = "void main() { for(;1.5;) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_073():
    """Error: Return type mismatch int -> float"""
    source = "int f() { return 1.5; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_074():
    """Error: Return type mismatch void -> int"""
    source = "void f() { return 1; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_075():
    """Error: Return type mismatch int -> void"""
    source = "int f() { return; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_076():
    """Error: Assignment mismatch int = float (as statement)"""
    source = "void main() { int x; x = 1.5; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_077():
    """Error: Assignment mismatch float = string"""
    source = "void main() { float f; f = \"hi\"; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_078():
    """Error: Switch expression float"""
    source = "void main() { float f; switch(f) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_079():
    """Error: Var init mismatch"""
    source = "void main() { int x = \"hi\"; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_080():
    """Error: float = int assignment"""
    source = "void main() { float f; f = 1; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_081():
    """Error: string = int assignment"""
    source = "void main() { string s; s = 42; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_082():
    """Error: struct = int assignment"""
    source = "struct S{}; void main() { S s; s = 1; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_083():
    """Error: int = struct assignment"""
    source = "struct S{}; void main() { S s; int x; x = s; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

# ============================================================================
# Type Mismatch In Expression (086 - 100)
# ============================================================================

def test_086():
    """Error: Binary + mismatch (int + string)"""
    source = "void main() { auto x = 5 + \"hi\"; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_087():
    """Error: Modulo on float"""
    source = "void main() { int x = 10; float f = 2.0; int z = x % f; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_088():
    """Error: Logical NOT on float"""
    source = "void main() { int x = !1.5; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_089():
    """Error: Logical AND on float"""
    source = "void main() { int x = 1 && 1.5; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_090():
    """Error: Relational mismatch (int == string)"""
    source = "void main() { int b = (1 == \"1\"); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_091():
    """Error: Prefix ++ on float"""
    source = "void main() { float f; ++f; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_092():
    """Error: Postfix -- on float"""
    source = "void main() { float f; f--; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_093():
    """Error: Struct assignment mismatch (as expression)"""
    source = "struct A{}; struct B{}; void main(){ A a; B b; int x = (a = b); }"
    # Assignment expression returns its type. If a = b fails, it's TypeMismatchInExpression.
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_094():
    """Error: Func call arg count mismatch"""
    source = "void f(int x){} void main(){ f(1, 2); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_095():
    """Error: Func call arg type mismatch"""
    source = "void f(int x){} void main(){ f(1.5); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_096():
    """Error: Member access on int"""
    source = "void main() { int x; x.m = 1; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_097():
    """Error: Unknown member of struct"""
    source = "struct S{int x;}; void main() { S s; s.y = 1; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_099():
    """Error: Increment on expression"""
    source = "void main() { int x; (x + 1)++; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_100():
    """Error: Type mismatch in nested struct literal"""
    source = "struct A{int x;}; struct B{A a;}; void main() { B b = {\"hi\"}; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

# ============================================================================
# Must In Loop (101 - 110)
# ============================================================================

def test_101():
    """Error: Break outside loop/switch"""
    source = "void main() { break; }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_102():
    """Error: Continue outside loop"""
    source = "void main() { continue; }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_103():
    """Error: Continue in switch"""
    source = "void main() { switch(1) { case 1: continue; } }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_104():
    """Valid: Break in nested if in loop"""
    source = "void main() { while(1) { if(1) break; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_105():
    """Error: Break in function called from loop (context not transferred)"""
    source = "void f() { break; } void main() { while(1) f(); }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_106():
    """Valid: Complex nested loops and breaks"""
    source = "void main() { for(auto i=0; i<10; i++) { while(1) { break; } continue; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_107():
    """Error: Continue in if outside loop"""
    source = "void main() { if(1) continue; }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_108():
    """Valid: Switch inside loop with both break kinds"""
    source = "void main() { while(1) { switch(1) { case 1: break; } break; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_110():
    """Valid: Complete programs"""
    source = "int f(int x) { if(x == 0) return 1; return x * f(x - 1); } void main() { printInt(f(5)); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_111():
    source = """	
Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(None, "x"),  # auto without initialization
                VarDecl(None, "y"),  # auto without initialization
                VarDecl(None, "z", BinaryOp(Identifier("x"), "+", Identifier("y")))
            ])
        )
    ])"""
    assert Checker(source).check_from_source() == "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(y)))"