"""
Test cases for TyC Static Semantic Checker

Generated using Weak Robust Black-Box Testing with
Equivalence Class Partitioning (ECP) and Boundary Value Analysis (BVA),
covering all requirement sections in the TyC language specification.

Total: 135 test cases (001-135)
"""

from tests.utils import Checker

# ============================================================================
# Section 1: Redeclared (001 - 020)
# ============================================================================

def test_001():
    """Valid: Single variable declaration - no redeclaration"""
    source = "void main() { int x; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_002():
    """Error: Redeclared Variable - same name, same type, same block"""
    source = "void main() { int x; int x; }"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_003():
    """Error: Redeclared Variable - same name, different types, same block"""
    source = "void main() { int x; float x; }"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_004():
    """Valid: Same name in sequential blocks - each is a separate scope"""
    source = "void main() { { int x; } { float x; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_005():
    """Valid: Shadowing - inner block reuses name from outer block"""
    source = "void main() { int x = 1; { float x = 2.0; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_006():
    """Valid: Deeply nested shadowing across three levels"""
    source = "void main() { int x = 1; { int x = 2; { int x = 3; } } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_007():
    """Error: Redeclared Function in global scope"""
    source = "void f() {} void f() {}"
    assert "Redeclared(Function, f)" in Checker(source).check_from_source()

def test_008():
    """Error: Redeclared Struct in global scope"""
    source = "struct S { int x; }; struct S { float y; };"
    assert "Redeclared(Struct, S)" in Checker(source).check_from_source()

def test_009():
    """Error: Redeclared Parameter - two params with same name"""
    source = "void f(int x, float x) {}"
    assert "Redeclared(Parameter, x)" in Checker(source).check_from_source()

def test_010():
    """Error: Redeclared Parameter - BVA: last param duplicates first"""
    source = "int f(int a, float b, int a) { return a; }"
    assert "Redeclared(Parameter, a)" in Checker(source).check_from_source()

def test_011():
    """Error: Redeclared struct member - same name within struct"""
    source = "struct S { int x; float x; };"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_012():
    """Error: Variable in function body same name as parameter (shared scope)"""
    source = "void f(int x) { int x; }"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_013():
    """Valid: Same variable name in different functions - no conflict"""
    source = "void f() { int x; } void main() { int x; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_014():
    """Valid: For-loop body shadows for-init variable (body is nested scope)"""
    source = "void main() { for (int i = 0; i < 10; i++) { int i = 5; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_015():
    """Error: Redeclared variable within same nested block"""
    source = "void main() { { int y; int y; } }"
    assert "Redeclared(Variable, y)" in Checker(source).check_from_source()

def test_016():
    """Valid: Same parameter name in different functions - no conflict"""
    source = "void f(int x) {} void g(int x) {}"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_017():
    """Error: Redeclared variable in switch scope (two decls in same case)"""
    source = "void main() { switch(1) { case 1: {int x = 1; int x = 2;} } }"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_018():
    """Valid: Same variable name in different case blocks (separate scopes)"""
    source = "void main() { switch(1) { case 1: { int x; } case 2: { int x; } } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_019():
    """Error: Redeclared struct member with different types"""
    source = "struct Point { int x; string x; };"
    assert "Redeclared(Variable, x)" in Checker(source).check_from_source()

def test_020():
    """Valid: Single parameter - BVA boundary: only one param, no redeclaration"""
    source = "void f(int x) { x = 1; }"
    assert Checker(source).check_from_source() == "Static checking passed"

# ============================================================================
# Section 2: UndeclaredIdentifier (021 - 032)
# ============================================================================

def test_021():
    """Error: Undeclared variable used in assignment"""
    source = "void main() { x = 1; }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

def test_022():
    """Error: Undeclared variable used in expression"""
    source = "void main() { int y = x + 1; }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

def test_023():
    """Error: Variable used before declaration in same scope"""
    source = "void main() { int x = y + 5; int y = 10; }"
    assert "UndeclaredIdentifier(y)" in Checker(source).check_from_source()

def test_024():
    """Error: Variable out of scope after its block exits"""
    source = "void main() { { int x = 1; } x = 2; }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

def test_025():
    """Error: Variable declared in one function used in another"""
    source = "void f() { int x = 1; } void main() { x = 2; }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

def test_026():
    """Error: Undeclared struct variable used in member access"""
    source = "struct S { int x; }; void main() { s.x = 1; }"
    assert "UndeclaredIdentifier(s)" in Checker(source).check_from_source()

def test_027():
    """Error: Undeclared identifier passed as function argument"""
    source = "void f(int x) {} void main() { f(y); }"
    assert "UndeclaredIdentifier(y)" in Checker(source).check_from_source()

def test_028():
    """Valid: Parameter is visible throughout the function body"""
    source = "int f(int x) { return x; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_029():
    """Valid: Variable in enclosing scope accessible from inner block"""
    source = "void main() { int x = 1; { int y = x + 1; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_030():
    """Valid: Variable declared before use"""
    source = "void main() { int x = 5; int y = x + 3; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_031():
    """Error: Undeclared variable in for-loop condition"""
    source = "void main() { for (; x < 10; ) {} }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

def test_032():
    """Error: Undeclared variable in return statement"""
    source = "int f() { return x; }"
    assert "UndeclaredIdentifier(x)" in Checker(source).check_from_source()

# ============================================================================
# Section 3: UndeclaredFunction (033 - 042)
# ============================================================================

def test_033():
    """Error: Function never declared"""
    source = "void main() { unknown(); }"
    assert "UndeclaredFunction(unknown)" in Checker(source).check_from_source()

def test_034():
    """Error: Function called before its declaration"""
    source = "void main() { f(); } void f() {}"
    assert "UndeclaredFunction(f)" in Checker(source).check_from_source()

def test_035():
    """Error: Undeclared function used in variable initialization"""
    source = "void main() { int x = compute(5); }"
    assert "UndeclaredFunction(compute)" in Checker(source).check_from_source()

def test_036():
    """Valid: Function declared before use"""
    source = "int add(int a, int b) { return a + b; } void main() { add(1, 2); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_037():
    """Valid: Built-in readInt is implicitly declared"""
    source = "void main() { int x = readInt(); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_038():
    """Valid: Built-in printInt is implicitly declared"""
    source = "void main() { printInt(1); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_039():
    """Valid: Built-in readFloat and printFloat"""
    source = "void main() { float f = readFloat(); printFloat(f); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_040():
    """Valid: Built-in readString and printString"""
    source = "void main() { string s = readString(); printString(s); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_041():
    """Error: Undeclared function used in if condition"""
    source = "void main() { if (check()) {} }"
    assert "UndeclaredFunction(check)" in Checker(source).check_from_source()

def test_042():
    """Valid: Recursive function call"""
    source = "int f(int n) { if (n <= 0) return 0; return f(n - 1) + 1; }"
    assert Checker(source).check_from_source() == "Static checking passed"

# ============================================================================
# Section 4: UndeclaredStruct (043 - 052)
# ============================================================================

def test_043():
    """Error: Struct type used as variable type before declaration"""
    source = "void main() { Point p; } struct Point { int x; int y; };"
    assert "UndeclaredStruct(Point)" in Checker(source).check_from_source()

def test_044():
    """Error: Struct type never declared"""
    source = "void main() { Unknown u; }"
    assert "UndeclaredStruct(Unknown)" in Checker(source).check_from_source()

def test_045():
    """Error: Struct member references undeclared struct type"""
    source = "struct Address { string street; City city; }; struct City { string name; };"
    assert "UndeclaredStruct(City)" in Checker(source).check_from_source()

def test_046():
    """Error: Struct used as parameter type before declaration"""
    source = "void f(Point p) {} struct Point { int x; };"
    assert "UndeclaredStruct(Point)" in Checker(source).check_from_source()

def test_047():
    """Error: Struct used as return type before declaration"""
    source = "Point get() {} struct Point { int x; };"
    assert "UndeclaredStruct(Point)" in Checker(source).check_from_source()

def test_048():
    """Valid: Struct declared before use as variable"""
    source = "struct Point { int x; int y; }; void main() { Point p; p.x = 1; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_049():
    """Valid: Struct declared before use in struct literal"""
    source = "struct Point { int x; int y; }; void main() { Point p = {1, 2}; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_050():
    """Valid: Struct member uses previously declared struct"""
    source = "struct A { int x; }; struct B { A a; }; void main() { B b = {{1}}; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_051():
    """Valid: Struct used as function return type (declared before function)"""
    source = "struct S { int x; }; S get() { S s = {1}; return s; } void main() { get(); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_052():
    """Valid: Struct used as function parameter type (declared before function)"""
    source = "struct S { int x; }; void f(S s) {} void main() { S s = {1}; f(s); }"
    assert Checker(source).check_from_source() == "Static checking passed"

# ============================================================================
# Section 5: TypeCannotBeInferred (053 - 066)
# ============================================================================

def test_053():
    """Error: auto variable declared but never used"""
    source = "void main() { auto x; }"
    assert "TypeCannotBeInferred(x)" in Checker(source).check_from_source()

def test_054():
    """Error: auto variable declared, other code runs, still no type inferred"""
    source = "void main() { auto x; { int y = 1; } }"
    assert "TypeCannotBeInferred(x)" in Checker(source).check_from_source()

def test_055():
    """Error: auto = auto - both sides unknown"""
    source = "void main() { auto x; auto y; x = y; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_056():
    """Error: auto + auto - both operands unknown"""
    source = "void main() { auto x; auto y; auto z = x + y; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_057():
    """Error: Circular auto dependency"""
    source = "void main() { auto x; auto y; x = y; y = x; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_058():
    """Error: auto inferred from struct literal with no type hint"""
    source = "struct S { int x; }; void main() { auto s = {1}; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_059():
    """Valid: auto inferred from int literal"""
    source = "void main() { auto x = 5; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_060():
    """Valid: auto inferred from float literal"""
    source = "void main() { auto x = 3.14; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_061():
    """Valid: auto inferred from string literal"""
    source = 'void main() { auto x = "hello"; }'
    assert Checker(source).check_from_source() == "Static checking passed"

def test_062():
    """Valid: auto without init - inferred from first assignment"""
    source = "void main() { auto x; x = 10; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_063():
    """Valid: auto inferred from function return type"""
    source = "int get() { return 1; } void main() { auto x = get(); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_064():
    """Valid: auto inferred from binary expression with known operand"""
    source = "void main() { auto x; int y = 5; x = y + 3; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_065():
    """Valid: auto inferred via function argument type"""
    source = "void main() { auto x; printInt(x); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_066():
    """Valid: auto inferred from binary op where other operand is a known literal"""
    source = "void main() { auto x; auto y = x + 5; }"
    assert Checker(source).check_from_source() == "Static checking passed"

# ============================================================================
# Section 6: TypeMismatchInStatement (067 - 087)
# ============================================================================

def test_067():
    """Error: if condition is float"""
    source = "void main() { float f = 1.5; if (f) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_068():
    """Error: if condition is string"""
    source = 'void main() { string s = "hi"; if (s) {} }'
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_069():
    """Valid: if condition is int"""
    source = "void main() { int x = 1; if (x) {} }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_070():
    """Error: while condition is float"""
    source = "void main() { float f = 1.0; while (f) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_071():
    """Error: while condition is string"""
    source = 'void main() { string s = "loop"; while (s) {} }'
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_072():
    """Valid: while condition is int"""
    source = "void main() { int i = 0; while (i < 10) { i++; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_073():
    """Error: for condition is float"""
    source = "void main() { for (; 1.5; ) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_074():
    """Valid: for condition is int"""
    source = "void main() { for (int i = 0; i < 10; i++) {} }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_075():
    """Error: Assignment int = float (no coercion in assignment)"""
    source = "void main() { int x; x = 1.5; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_076():
    """Error: Assignment float = int (no coercion in assignment)"""
    source = "void main() { float f; f = 1; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_077():
    """Error: Assignment int = string"""
    source = 'void main() { int x; x = "hi"; }'
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_078():
    """Error: Assignment string = int"""
    source = "void main() { string s; s = 42; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_079():
    """Error: Variable initialization type mismatch (int = string)"""
    source = 'void main() { int x = "hello"; }'
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_080():
    """Error: Variable initialization mismatch (float = string)"""
    source = 'void main() { float f = "pi"; }'
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_081():
    """Error: Struct assigned to different struct type"""
    source = "struct A { int x; }; struct B { int x; }; void main() { A a; B b; a = b; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_082():
    """Error: Return mismatch - int function returns float"""
    source = "int f() { return 1.5; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_083():
    """Error: Return mismatch - int function returns string"""
    source = 'int f() { return "hi"; }'
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_084():
    """Error: Void function returns a value"""
    source = "void f() { return 1; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_085():
    """Error: Non-void function returns nothing (empty return)"""
    source = "int f() { return; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_086():
    """Error: Switch expression is float"""
    source = "void main() { float f = 1.0; switch (f) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_087():
    """Error: Switch expression is string"""
    source = 'void main() { string s = "a"; switch (s) {} }'
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

# ============================================================================
# Section 7: TypeMismatchInExpression (088 - 120)
# ============================================================================

def test_088():
    """Error: Binary + with int and string"""
    source = 'void main() { auto x = 1 + "hi"; }'
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_089():
    """Error: Binary * with float and string"""
    source = 'void main() { auto x = 1.5 * "hi"; }'
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_090():
    """Valid: Binary + with int and float (result is float)"""
    source = "void main() { float x = 1 + 2.0; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_091():
    """Valid: Binary + with both int (result is int)"""
    source = "void main() { int x = 1 + 2; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_092():
    """Error: Modulo with float left operand"""
    source = "void main() { int x = 1; float f = 1.5; int z = f % x; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_093():
    """Error: Modulo with float right operand"""
    source = "void main() { int x = 10; float f = 2.0; int z = x % f; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_094():
    """Valid: Modulo with both int operands"""
    source = "void main() { int x = 10 % 3; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_095():
    """Error: Relational < with string operand"""
    source = 'void main() { int b = 1 < "hi"; }'
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_096():
    """Valid: Relational < with int operands"""
    source = "void main() { int b = 1 < 2; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_097():
    """Error: Logical AND with float right operand"""
    source = "void main() { int b = 1 && 1.5; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_098():
    """Error: Logical OR with float left operand"""
    source = "void main() { int b = 1.5 || 0; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_099():
    """Error: Logical NOT on float"""
    source = "void main() { int b = !1.5; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_100():
    """Valid: Logical NOT on int"""
    source = "void main() { int b = !1; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_101():
    """Error: Prefix ++ on float"""
    source = "void main() { float f = 1.0; ++f; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_102():
    """Error: Postfix -- on float"""
    source = "void main() { float f = 1.0; f--; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_103():
    """Error: Prefix ++ on expression (not an lvalue)"""
    source = "void main() { int x = 1; ++(x + 1); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_104():
    """Error: Postfix ++ on expression (not an lvalue)"""
    source = "void main() { int x = 1; (x + 1)++; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_105():
    """Valid: Prefix ++ on int variable"""
    source = "void main() { int x = 0; ++x; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_106():
    """Valid: Postfix ++ on int variable"""
    source = "void main() { int x = 0; x++; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_107():
    """Error: Member access on non-struct (int)"""
    source = "void main() { int x = 1; x.field = 2; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_108():
    """Error: Access of unknown member of struct"""
    source = "struct S { int x; }; void main() { S s; s.z = 1; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_109():
    """Valid: Member access on declared struct with existing member"""
    source = "struct S { int x; }; void main() { S s; s.x = 1; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_110():
    """Error: Function call with too few arguments (BVA: one less than required)"""
    source = "int add(int a, int b) { return a + b; } void main() { add(1); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_111():
    """Error: Function call with too many arguments (BVA: one more than required)"""
    source = "void f(int x) {} void main() { f(1, 2); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_112():
    """Error: Function call with zero args when one required (BVA: boundary at 0)"""
    source = "void f(int x) {} void main() { f(); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_113():
    """Error: Function call with wrong argument type"""
    source = "void f(int x) {} void main() { f(1.5); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_114():
    """Valid: Function call with matching argument count and types"""
    source = "void f(int x, float y) {} void main() { f(1, 2.0); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_115():
    """Error: Assignment expression type mismatch used as sub-expression"""
    source = "void main() { int x; int y = (x = 1.5) + 1; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_116():
    """Valid: Assignment expression used in expression context"""
    source = "void main() { int x; int y = (x = 5) + 3; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_117():
    """Valid: Chained assignment (right-associative)"""
    source = "void main() { int a; int b; int c; a = b = c = 10; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_118():
    """Error: Nested struct literal type mismatch (string where int expected)"""
    source = 'struct A { int x; }; struct B { A a; }; void main() { B b = {"hi"}; }'
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_119():
    """Error: Struct literal with wrong number of values (too few)"""
    source = "struct S { int x; int y; }; void main() { S s = {1}; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_120():
    """Error: Struct literal value type mismatch (float where int expected)"""
    source = "struct S { int x; }; void main() { S s = {1.5}; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

# ============================================================================
# Section 8: MustInLoop (121 - 135)
# ============================================================================

def test_121():
    """Error: Break outside loop and switch"""
    source = "void main() { break; }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_122():
    """Error: Continue outside loop"""
    source = "void main() { continue; }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_123():
    """Error: Break in if statement with no enclosing loop"""
    source = "void main() { if (1) { break; } }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_124():
    """Error: Continue in if statement with no enclosing loop"""
    source = "void main() { if (1) { continue; } }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_125():
    """Error: Continue inside switch (continue not valid in switch)"""
    source = "void main() { switch (1) { case 1: continue; } }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_126():
    """Error: Break in function - loop context not transferred across calls"""
    source = "void f() { break; } void main() { while (1) { f(); } }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_127():
    """Error: Continue in function - loop context not transferred"""
    source = "void f() { continue; } void main() { while (1) { f(); } }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_128():
    """Valid: Break inside while loop"""
    source = "void main() { while (1) { break; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_129():
    """Valid: Continue inside while loop"""
    source = "void main() { int i = 0; while (i < 10) { i++; continue; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_130():
    """Valid: Break inside for loop"""
    source = "void main() { for (int i = 0; i < 10; i++) { break; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_131():
    """Valid: Continue inside for loop"""
    source = "void main() { for (int i = 0; i < 10; i++) { continue; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_132():
    """Valid: Break inside switch statement"""
    source = "void main() { switch (1) { case 1: break; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_133():
    """Valid: Break in if inside loop"""
    source = "void main() { while (1) { if (1) { break; } } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_134():
    """Valid: Break in inner loop of nested loops"""
    source = "void main() { for (int i = 0; i < 5; i++) { for (int j = 0; j < 5; j++) { break; } } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_135():
    """Valid: Switch inside loop - break in switch, then break exits loop"""
    source = "void main() { while (1) { switch (1) { case 1: break; } break; } }"
    assert Checker(source).check_from_source() == "Static checking passed"
