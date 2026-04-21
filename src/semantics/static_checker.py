"""
Static Semantic Checker for TyC Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the TyC procedural programming language. It performs type checking,
scope management, type inference, and detects all semantic errors as
specified in the TyC language specification.
"""

from functools import reduce
from typing import (
    Dict,
    List,
    Set,
    Optional,
    Any,
    Tuple,
    NamedTuple,
    Union,
    TYPE_CHECKING,
)
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode,
    Program,
    StructDecl,
    MemberDecl,
    FuncDecl,
    Param,
    VarDecl,
    IfStmt,
    WhileStmt,
    ForStmt,
    BreakStmt,
    ContinueStmt,
    ReturnStmt,
    BlockStmt,
    SwitchStmt,
    CaseStmt,
    DefaultStmt,
    Type,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    BinaryOp,
    PrefixOp,
    PostfixOp,
    AssignExpr,
    MemberAccess,
    FuncCall,
    Identifier,
    StructLiteral,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    ExprStmt,
    Expr,
    Stmt,
    Decl,
)

# Type aliases for better type hints
TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]
from .static_error import (
    StaticError,
    Redeclared,
    UndeclaredIdentifier,
    UndeclaredFunction,
    UndeclaredStruct,
    TypeCannotBeInferred,
    TypeMismatchInStatement,
    TypeMismatchInExpression,
    MustInLoop,
)


class Symbol:
    def __init__(self, kind: str, p_strName: str, p_tType: Optional[TyCType] = None, p_blIs_auto: bool = False):
        self.m_strKind = kind  # 'Variable', 'Function', 'Struct', 'Parameter'
        self.m_strName = p_strName
        self.m_tType = p_tType
        self.m_blIs_auto = p_blIs_auto

class CheckEnv:
    def __init__(self):
        # List of scopes, each scope is a dict: name -> Symbol
        self.m_arrScopes: List[Dict[str, Symbol]] = [{}]
        self.m_dicFuncs: Dict[str, FuncDecl] = {}
        self.m_dicStructs: Dict[str, StructDecl] = {}
        self.m_objCurrent_func: Optional[FuncDecl] = None
        self.m_tInferred_return_type: Optional[TyCType] = None
        self.m_iLoop_level = 0
        self.m_iSwitch_level = 0
        
        # Add built-in functions
        self.add_builtin("readInt", [], IntType())
        self.add_builtin("printInt", [IntType()], VoidType())
        self.add_builtin("readFloat", [], FloatType())
        self.add_builtin("printFloat", [FloatType()], VoidType())
        self.add_builtin("readString", [], StringType())
        self.add_builtin("printString", [StringType()], VoidType())

    def add_builtin(self, p_strName: str, p_arrParam_types: List[TyCType], p_tReturn_type: TyCType):
        v_arrParams = [Param(pt, f"p{i}") for i, pt in enumerate(p_arrParam_types)]
        # Use a dummy block for built-ins
        v_objFunc_decl = FuncDecl(p_tReturn_type, p_strName, v_arrParams, BlockStmt([]))
        self.m_dicFuncs[p_strName] = v_objFunc_decl

    def lookup(self, p_strName: str, p_strKind: str = None) -> Optional[Symbol]:
        for v_dicScope in reversed(self.m_arrScopes):
            if p_strName in v_dicScope:
                v_objSymbol = v_dicScope[p_strName]
                if p_strKind is None or v_objSymbol.m_strKind == p_strKind:
                    return v_objSymbol
        return None

    def enter_scope(self):
        self.m_arrScopes.append({})

    def exit_scope(self):
        self.m_arrScopes.pop()

    def declare(self, p_strKind: str, v_strName: str, p_tType: Optional[TyCType] = None, p_blIs_auto: bool = False):
        if v_strName in self.m_arrScopes[-1]:
            raise Redeclared(p_strKind, v_strName)
        if p_strKind == "Variable":
            for scope in self.m_arrScopes[:-1]:
                if v_strName in scope and scope[v_strName].m_strKind == "Parameter":
                    raise Redeclared(p_strKind, v_strName)
        v_objSymbol = Symbol(p_strKind, v_strName, p_tType, p_blIs_auto)
        self.m_arrScopes[-1][v_strName] = v_objSymbol
        return v_objSymbol

def type_eq(p_tType1: Optional[TyCType], p_tType2: Optional[TyCType]) -> bool:
    if p_tType1 is None or p_tType2 is None:
        return p_tType1 == p_tType2
    if type(p_tType1) is not type(p_tType2):
        return False
    if isinstance(p_tType1, StructType):
        return p_tType1.struct_name == p_tType2.struct_name
    return True

class StaticChecker(ASTVisitor):
    def check_program(self, node: "Program"):
        checkEnv = CheckEnv()
        self.visit(node, checkEnv)

    def visit_program(self, node: "Program", o: CheckEnv):
        for v_objDecl in node.decls:
            self.visit(v_objDecl, o)

    def visit_struct_decl(self, node: "StructDecl", o: CheckEnv):
        if node.name in o.m_dicStructs:
            raise Redeclared("Struct", node.name)
        
        # Visit members
        o.enter_scope()
        for v_objMember in node.members:
            self.visit(v_objMember, o)
        o.exit_scope()
        
        o.m_dicStructs[node.name] = node

    def visit_member_decl(self, node: "MemberDecl", o: CheckEnv):
        # Members must have explicit types
        if node.member_type is None:
            raise TypeCannotBeInferred(node.name)
        self.visit(node.member_type, o)
        o.declare("Member", node.name, node.member_type)

    def visit_func_decl(self, node: "FuncDecl", o: CheckEnv):
        if node.name in o.m_dicFuncs:
            raise Redeclared("Function", node.name)
        o.m_dicFuncs[node.name] = node
        
        if node.return_type:
            self.visit(node.return_type, o)
            
        o.m_objCurrent_func = node
        o.m_tInferred_return_type = None
        
        o.enter_scope() # Scope for parameters AND outermost block
        for v_objParam in node.params:
            self.visit(v_objParam, o)
        # Tell visit_block_stmt NOT to enter a new scope for the body
        o.m_blEnter_new_scope = False
        self.visit(node.body, o)
        o.m_blEnter_new_scope = True
        
        # Determine actual return type
        v_objActual_return_type = None
        if node.return_type:
            v_objActual_return_type = node.return_type
        else:
            v_objActual_return_type = o.m_tInferred_return_type if o.m_tInferred_return_type else VoidType()
            node.return_type = v_objActual_return_type
                
        o.exit_scope()
        o.m_objCurrent_func = None

    def visit_param(self, node: "Param", o: CheckEnv):
        v_tParam_type = self.visit(node.param_type, o)
        o.declare("Parameter", node.name, v_tParam_type)

    # Type system
    def visit_int_type(self, node: "IntType", o: CheckEnv):
        return node

    def visit_float_type(self, node: "FloatType", o: CheckEnv):
        return node

    def visit_string_type(self, node: "StringType", o: CheckEnv):
        return node

    def visit_void_type(self, node: "VoidType", o: CheckEnv):
        return node

    def visit_struct_type(self, node: "StructType", o: CheckEnv):
        if node.struct_name not in o.m_dicStructs:
            raise UndeclaredStruct(node.struct_name)
        return node

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: CheckEnv):
        # Skip creating new scope if the block is a function body,
        # else entering new scope
        v_blEnter_scope = v_blOld_flag = getattr(o, 'm_blEnter_new_scope', True)
        o.m_blEnter_new_scope = True
        if v_blEnter_scope:
            o.enter_scope()
        
        for v_objStatement in node.statements:
            self.visit(v_objStatement, o)
        
        for v_strName, v_objSymbol in o.m_arrScopes[-1].items():
            if v_objSymbol.m_blIs_auto and v_objSymbol.m_tType is None:
                raise TypeCannotBeInferred(node)
        if v_blEnter_scope:
            o.exit_scope()
            
        o.m_blEnter_new_scope = v_blOld_flag

    def visit_var_decl(self, node: "VarDecl", o: CheckEnv):
        v_tVar_type = None
        v_blIs_auto = node.var_type is None
        if not v_blIs_auto:
            v_tVar_type = self.visit(node.var_type, o)
            
        v_tInit_type = None
        if node.init_value:
            # For struct literals, we need to pass the expected type
            v_tInit_type = self.visit(node.init_value, (o, v_tVar_type))
            if not v_blIs_auto:
                if not type_eq(v_tVar_type, v_tInit_type):
                    raise TypeMismatchInStatement(node)
            else:
                # auto x = init; -> type is inferred from init
                if v_tInit_type is None: # e.g. auto x = {1, 2}; unknown struct literal
                    raise TypeCannotBeInferred(node)
                v_tVar_type = v_tInit_type
                v_blIs_auto = False
                
        o.declare("Variable", node.name, v_tVar_type, v_blIs_auto)

    def visit_if_stmt(self, node: "IfStmt", o: CheckEnv):
        v_blCondition_type = self.visit(node.condition, o)
        if not isinstance(v_blCondition_type, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

    def visit_while_stmt(self, node: "WhileStmt", o: CheckEnv):
        v_blCondition_type = self.visit(node.condition, o)
        if not isinstance(v_blCondition_type, IntType):
            raise TypeMismatchInStatement(node)
        o.m_iLoop_level += 1
        self.visit(node.body, o)
        o.m_iLoop_level -= 1

    def visit_for_stmt(self, node: "ForStmt", o: CheckEnv):
        o.enter_scope()
        if node.init:
            self.visit(node.init, o)
        if node.condition:
            v_blCondition_type = self.visit(node.condition, o)
            if not isinstance(v_blCondition_type, IntType):
                raise TypeMismatchInStatement(node)
        if node.update:
            self.visit(node.update, o)
        
        o.m_iLoop_level += 1
        self.visit(node.body, o)
        
        # Check auto variables in for-loop scope
        for v_strName, v_objSymbol in o.m_arrScopes[-1].items():
            if v_objSymbol.m_blIs_auto and v_objSymbol.m_tType is None:
                raise TypeCannotBeInferred(node)
                
        o.m_iLoop_level -= 1
        o.exit_scope()

    def visit_switch_stmt(self, node: "SwitchStmt", o: CheckEnv):
        v_tExpr_type = self.visit(node.expr, o)
        if not isinstance(v_tExpr_type, IntType):
            raise TypeMismatchInStatement(node)
        
        o.m_iSwitch_level += 1
        o.enter_scope() # Scope for switch cases
        for v_objCase in node.cases:
            self.visit(v_objCase, o)
        if node.default_case:
            self.visit(node.default_case, o)
        o.exit_scope()
        o.m_iSwitch_level -= 1

    def visit_case_stmt(self, node: "CaseStmt", o: CheckEnv):
        v_tExpr_type = self.visit(node.expr, o)
        if not isinstance(v_tExpr_type, IntType):
            raise TypeMismatchInStatement(node)
        for v_objStatement in node.statements:
            self.visit(v_objStatement, o)

    def visit_default_stmt(self, node: "DefaultStmt", o: CheckEnv):
        for v_objStatement in node.statements:
            self.visit(v_objStatement, o)

    def visit_break_stmt(self, node: "BreakStmt", o: CheckEnv):
        if o.m_iLoop_level == 0 and o.m_iSwitch_level == 0:
            raise MustInLoop(node)

    def visit_continue_stmt(self, node: "ContinueStmt", o: CheckEnv):
        if o.m_iLoop_level == 0:
            raise MustInLoop(node)

    def visit_return_stmt(self, node: "ReturnStmt", o: CheckEnv):
        v_objCurrent_func = o.m_objCurrent_func
        v_tReturn_expr_type = None
        if node.expr:
            # For returning struct literals, use function return type as hint
            v_tExpected_return_type = v_objCurrent_func.return_type if v_objCurrent_func.return_type else o.m_tInferred_return_type
            v_tReturn_expr_type = self.visit(node.expr, (o, v_tExpected_return_type))
            if v_tReturn_expr_type is None:
                raise TypeCannotBeInferred(node)
        else:
            v_tReturn_expr_type = VoidType()
            
        if v_objCurrent_func.return_type is None:
            # auto return type inference
            if o.m_tInferred_return_type is None:
                o.m_tInferred_return_type = v_tReturn_expr_type
            else:
                if not type_eq(o.m_tInferred_return_type, v_tReturn_expr_type):
                    raise TypeMismatchInStatement(node)
        else:
            # explicit return type
            if not type_eq(v_objCurrent_func.return_type, v_tReturn_expr_type):
                raise TypeMismatchInStatement(node)

    def visit_expr_stmt(self, node: "ExprStmt", o: CheckEnv):
        v_blOld_is_stmt = getattr(o, 'm_blIs_stmt', False)
        o.m_blIs_stmt = True
        self.visit(node.expr, o)
        o.m_blIs_stmt = v_blOld_is_stmt

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        
        v_tLeft_type = self.visit(node.left, o)
        v_tRight_type = self.visit(node.right, o)
        
        v_strOperator = node.operator
        
        # Handle auto inference from binary op
        if v_tLeft_type is None and v_tRight_type is None:
            # Both unknown
            raise TypeCannotBeInferred(node)
        elif v_tLeft_type is None and v_tRight_type is not None:
            # Infer ltype from rtype
            if isinstance(node.left, Identifier):
                v_objSymbol = o.lookup(node.left.name)
                if v_objSymbol and v_objSymbol.m_blIs_auto:
                    v_objSymbol.m_tType = v_tRight_type
                    v_objSymbol.m_blIs_auto = False
                    v_tLeft_type = v_tRight_type
        elif v_tRight_type is None and v_tLeft_type is not None:
            # Infer rtype from ltype
            if isinstance(node.right, Identifier):
                v_objSymbol = o.lookup(node.right.name)
                if v_objSymbol and v_objSymbol.m_blIs_auto:
                    v_objSymbol.m_tType = v_tLeft_type
                    v_objSymbol.m_blIs_auto = False
                    v_tRight_type = v_tLeft_type

        if v_tLeft_type is None or v_tRight_type is None:
            raise TypeCannotBeInferred(node)
        
        # Check types
        if v_strOperator in ['&&', '||', '%']: # Operators that require int
            if isinstance(v_tLeft_type, IntType) and isinstance(v_tRight_type, IntType):
                return IntType()

        # Re-verify with resolved types
        elif v_strOperator in ['+', '-', '*', '/']:
            if isinstance(v_tLeft_type, (IntType, FloatType)) and isinstance(v_tRight_type, (IntType, FloatType)):
                return FloatType() if isinstance(v_tLeft_type, FloatType) or isinstance(v_tRight_type, FloatType) else IntType()

        elif v_strOperator in ['==', '!=', '<', '>', '<=', '>=']:
            if isinstance(v_tLeft_type, (IntType, FloatType)) and isinstance(v_tRight_type, (IntType, FloatType)):
                return IntType()
        
        raise TypeMismatchInExpression(node)

    def visit_prefix_op(self, node: "PrefixOp", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        v_tExpression_type = self.visit(node.operand, o)
        v_strOperator = node.operator
        
        if v_tExpression_type is None and isinstance(node.operand, Identifier):
            v_objSymbol = o.lookup(node.operand.name)
            if v_objSymbol and v_objSymbol.m_blIs_auto:
                if v_strOperator in ['++', '--', '!']:
                    v_objSymbol.m_tType = IntType() 
                    v_objSymbol.m_blIs_auto = False
                    v_tExpression_type = IntType()
                # for + / - we still don't know if it's int or float
        
        if v_tExpression_type is None: 
            raise TypeMismatchInExpression(node)

        if v_strOperator in ['++', '--']:
            if isinstance(v_tExpression_type, IntType) and isinstance(node.operand, (Identifier, MemberAccess)):
                return IntType()
        elif v_strOperator in ['+', '-']:
            if isinstance(v_tExpression_type, (IntType, FloatType)): 
                return v_tExpression_type
        elif v_strOperator == '!':
            if isinstance(v_tExpression_type, IntType): 
                return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_postfix_op(self, node: "PostfixOp", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        v_tExpression_type = self.visit(node.operand, o)
        v_strOperator = node.operator
        
        if v_tExpression_type is None and isinstance(node.operand, Identifier):
            v_objSymbol = o.lookup(node.operand.name)
            if v_objSymbol and v_objSymbol.m_blIs_auto:
                if v_strOperator in ['++', '--']:
                    v_objSymbol.m_tType = IntType()
                    v_objSymbol.m_blIs_auto = False
                    v_tExpression_type = IntType()

        if v_tExpression_type is None: 
            raise TypeMismatchInExpression(node)

        if v_strOperator in ['++', '--']:
            if isinstance(v_tExpression_type, IntType) and isinstance(node.operand, (Identifier, MemberAccess)):
                return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: "AssignExpr", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
            
        v_tLeft_type = self.visit(node.lhs, o)
        v_tRight_type = self.visit(node.rhs, (o, v_tLeft_type))
        
        if v_tLeft_type is None:
            if v_tRight_type is not None:
                # Infer LHS from RHS
                sym = o.lookup(node.lhs.name)
                if sym and sym.m_blIs_auto:
                    sym.m_tType = v_tRight_type
                    sym.m_blIs_auto = False
                    v_tLeft_type = v_tRight_type
            else:
                # Both unknown
                raise TypeCannotBeInferred(node)

        if not type_eq(v_tLeft_type, v_tRight_type):
            if getattr(o, 'm_blIs_stmt', False):
                raise TypeMismatchInStatement(node)
            raise TypeMismatchInExpression(node)
            
        return v_tLeft_type

    def visit_member_access(self, node: "MemberAccess", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        v_tObj_type = self.visit(node.obj, o)
        if not isinstance(v_tObj_type, StructType):
            raise TypeMismatchInExpression(node)
            
        v_objStruct = o.m_dicStructs.get(v_tObj_type.struct_name)
        if not v_objStruct: 
            raise UndeclaredStruct(v_tObj_type.struct_name)
            
        for v_objMember in v_objStruct.members:
            if v_objMember.name == node.member:
                return v_objMember.member_type
            
        raise TypeMismatchInExpression(node)

    def visit_func_call(self, node: "FuncCall", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        if node.name not in o.m_dicFuncs:
            raise UndeclaredFunction(node.name)

        v_objFunction = o.m_dicFuncs[node.name]
        if len(v_objFunction.params) != len(node.args):
            raise TypeMismatchInExpression(node)
            
        for v_objParam, v_objArgument in zip(v_objFunction.params, node.args):
            v_tArgument_type = self.visit(v_objArgument, (o, v_objParam.param_type))

            if v_tArgument_type is None and isinstance(v_objArgument, Identifier):
                v_objSymbol = o.lookup(v_objArgument.name)
                if v_objSymbol and v_objSymbol.m_blIs_auto:
                    v_objSymbol.m_tType = v_objParam.param_type
                    v_objSymbol.m_blIs_auto = False
                    v_tArgument_type = v_objParam.param_type

            if not type_eq(v_objParam.param_type, v_tArgument_type):
                raise TypeMismatchInExpression(node)
                
        return v_objFunction.return_type

    def visit_identifier(self, node: "Identifier", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        v_objSymbol = o.lookup(node.name)
        if not v_objSymbol:
            raise UndeclaredIdentifier(node.name)
            
        if v_objSymbol.m_blIs_auto and v_objSymbol.m_tType is None:
            return None

        return v_objSymbol.m_tType

    def visit_struct_literal(self, node: "StructLiteral", o_in: Any):
        if not isinstance(o_in, tuple) or o_in[1] is None or not isinstance(o_in[1], StructType):
            # No context hint or hint is not a struct
            return None
            
        o, v_tExpected_type = o_in
        v_objStruct = o.m_dicStructs.get(v_tExpected_type.struct_name)
        if not v_objStruct: 
            raise UndeclaredStruct(v_tExpected_type.struct_name)
            
        if len(v_objStruct.members) != len(node.values):
            raise TypeMismatchInExpression(node)
            
        for v_objMember, v_objExpression in zip(v_objStruct.members, node.values):
            v_tExpression_type = self.visit(v_objExpression, (o, v_objMember.member_type))
            if not type_eq(v_objMember.member_type, v_tExpression_type):
                raise TypeMismatchInExpression(node)
                
        return v_tExpected_type

    # Literals
    def visit_int_literal(self, node: "IntLiteral", o: CheckEnv):
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: CheckEnv):
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: CheckEnv):
        return StringType()