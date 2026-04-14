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
    def __init__(self, kind: str, name: str, mtype: Optional[TyCType] = None, is_auto: bool = False):
        self.kind = kind  # 'Variable', 'Function', 'Struct', 'Parameter'
        self.name = name
        self.mtype = mtype
        self.is_auto = is_auto

class CheckEnv:
    def __init__(self):
        # List of scopes, each scope is a dict: name -> Symbol
        self.scopes: List[Dict[str, Symbol]] = [{}]
        self.funcs: Dict[str, FuncDecl] = {}
        self.structs: Dict[str, StructDecl] = {}
        self.current_func: Optional[FuncDecl] = None
        self.inferred_return_type: Optional[TyCType] = None
        self.loop_level = 0
        self.switch_level = 0
        
        # Add built-in functions
        self.add_builtin("readInt", [], IntType())
        self.add_builtin("printInt", [IntType()], VoidType())
        self.add_builtin("readFloat", [], FloatType())
        self.add_builtin("printFloat", [FloatType()], VoidType())
        self.add_builtin("readString", [], StringType())
        self.add_builtin("printString", [StringType()], VoidType())

    def add_builtin(self, name: str, param_types: List[TyCType], return_type: TyCType):
        params = [Param(pt, f"p{i}") for i, pt in enumerate(param_types)]
        # Use a dummy block for built-ins
        fdecl = FuncDecl(return_type, name, params, BlockStmt([]))
        self.funcs[name] = fdecl

    def lookup(self, name: str, kind: str = None) -> Optional[Symbol]:
        for scope in reversed(self.scopes):
            if name in scope:
                sym = scope[name]
                if kind is None or sym.kind == kind:
                    return sym
        return None

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def declare(self, kind: str, name: str, mtype: Optional[TyCType] = None, is_auto: bool = False):
        if name in self.scopes[-1]:
            raise Redeclared(kind, name)
        sym = Symbol(kind, name, mtype, is_auto)
        self.scopes[-1][name] = sym
        return sym

def type_eq(t1: Optional[TyCType], t2: Optional[TyCType]) -> bool:
    if t1 is None or t2 is None:
        return t1 == t2
    if type(t1) is not type(t2):
        return False
    if isinstance(t1, StructType):
        return t1.struct_name == t2.struct_name
    return True

class StaticChecker(ASTVisitor):
    def check_program(self, node: "Program"):
        checkEnv = CheckEnv()
        self.visit(node, checkEnv)

    def visit_program(self, node: "Program", o: CheckEnv):
        for decl in node.decls:
            self.visit(decl, o)

    def visit_struct_decl(self, node: "StructDecl", o: CheckEnv):
        if node.name in o.structs:
            raise Redeclared("Struct", node.name)
        o.structs[node.name] = node
        
        # Visit members to check for Redeclared and UndeclaredStruct
        o.enter_scope()
        for member in node.members:
            self.visit(member, o)
        o.exit_scope()

    def visit_member_decl(self, node: "MemberDecl", o: CheckEnv):
        # Members must have explicit types
        self.visit(node.member_type, o)
        o.declare("Variable", node.name, node.member_type)

    def visit_func_decl(self, node: "FuncDecl", o: CheckEnv):
        if node.name in o.funcs:
            raise Redeclared("Function", node.name)
        o.funcs[node.name] = node
        
        if node.return_type:
            self.visit(node.return_type, o)
            
        o.current_func = node
        o.inferred_return_type = None
        
        o.enter_scope() # Scope for parameters AND outermost block
        for param in node.params:
            self.visit(param, o)
        
        # Tell visit_block_stmt NOT to enter a new scope for the body
        o.enter_new_scope = False
        self.visit(node.body, o)
        o.enter_new_scope = True
        
        # Determine actual return type
        actual_ret = None
        if node.return_type:
            actual_ret = node.return_type
        else:
            actual_ret = o.inferred_return_type if o.inferred_return_type else VoidType()
        
        node.return_type = actual_ret
            
        # Check auto variables in the shared param/body scope
        for name, sym in o.scopes[-1].items():
            if sym.is_auto and sym.mtype is None:
                raise TypeCannotBeInferred(name)
                
        o.exit_scope()
        o.current_func = None

    def visit_param(self, node: "Param", o: CheckEnv):
        ptype = self.visit(node.param_type, o)
        o.declare("Parameter", node.name, ptype)

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
        if node.struct_name not in o.structs:
            raise UndeclaredStruct(node.struct_name)
        return node

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: CheckEnv):
        # We might want to skip creating a new scope if this is a function body
        # or similar. But let's check a flag in 'o'.
        should_enter = getattr(o, 'enter_new_scope', True)
        if should_enter:
            o.enter_scope()
        
        # Reset flag for nested blocks
        old_flag = getattr(o, 'enter_new_scope', True)
        o.enter_new_scope = True
        
        for stmt in node.statements:
            self.visit(stmt, o)
        
        # Check auto variables
        if should_enter:
            for name, sym in o.scopes[-1].items():
                if sym.is_auto and sym.mtype is None:
                    raise TypeCannotBeInferred(name)
            o.exit_scope()
            
        o.enter_new_scope = old_flag

    def visit_var_decl(self, node: "VarDecl", o: CheckEnv):
        var_type = None
        is_auto = node.var_type is None
        if not is_auto:
            var_type = self.visit(node.var_type, o)
            
        init_type = None
        if node.init_value:
            # For struct literals, we need to pass the expected type
            init_type = self.visit(node.init_value, (o, var_type))
            if not is_auto:
                if not type_eq(var_type, init_type):
                    raise TypeMismatchInStatement(node)
            else:
                # auto x = init; -> type is inferred from init
                if init_type is None: # e.g. auto x = {1, 2}; unknown struct literal
                    raise TypeCannotBeInferred(node.name)
                var_type = init_type
                is_auto = False
                
        o.declare("Variable", node.name, var_type, is_auto)

    def visit_if_stmt(self, node: "IfStmt", o: CheckEnv):
        cond_type = self.visit(node.condition, o)
        if not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

    def visit_while_stmt(self, node: "WhileStmt", o: CheckEnv):
        cond_type = self.visit(node.condition, o)
        if not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        o.loop_level += 1
        self.visit(node.body, o)
        o.loop_level -= 1

    def visit_for_stmt(self, node: "ForStmt", o: CheckEnv):
        o.enter_scope()
        if node.init:
            self.visit(node.init, o)
        if node.condition:
            cond_type = self.visit(node.condition, o)
            if not isinstance(cond_type, IntType):
                raise TypeMismatchInStatement(node)
        if node.update:
            self.visit(node.update, o)
        
        o.loop_level += 1
        self.visit(node.body, o)
        
        # Check auto variables in for-loop scope (can happen if init is a VarDecl)
        for name, sym in o.scopes[-1].items():
            if sym.is_auto and sym.mtype is None:
                raise TypeCannotBeInferred(name)
                
        o.loop_level -= 1
        o.exit_scope()

    def visit_switch_stmt(self, node: "SwitchStmt", o: CheckEnv):
        expr_type = self.visit(node.expr, o)
        if not isinstance(expr_type, IntType):
            raise TypeMismatchInStatement(node)
        
        o.switch_level += 1
        # Switch has its own scope implicitly for cases? 
        # Actually TyC switch is C-like fallthrough, typically it doesn't have a new scope per case unless {}.
        # But variables declared in switch body (if allowed) are visible?
        # The grammar usually puts cases in a block.
        for case in node.cases:
            self.visit(case, o)
        if node.default_case:
            self.visit(node.default_case, o)
        o.switch_level -= 1

    def visit_case_stmt(self, node: "CaseStmt", o: CheckEnv):
        # Case expression must be int.
        self.visit(node.expr, o) # Must be IntType
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_default_stmt(self, node: "DefaultStmt", o: CheckEnv):
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_break_stmt(self, node: "BreakStmt", o: CheckEnv):
        if o.loop_level == 0 and o.switch_level == 0:
            raise MustInLoop(node)

    def visit_continue_stmt(self, node: "ContinueStmt", o: CheckEnv):
        if o.loop_level == 0:
            raise MustInLoop(node)

    def visit_return_stmt(self, node: "ReturnStmt", o: CheckEnv):
        func = o.current_func
        ret_expr_type = None
        if node.expr:
            # For returning struct literals, use function return type as hint
            expected = func.return_type if func.return_type else o.inferred_return_type
            ret_expr_type = self.visit(node.expr, (o, expected))
        else:
            ret_expr_type = VoidType()
            
        if func.return_type is None:
            # auto return type inference
            if o.inferred_return_type is None:
                o.inferred_return_type = ret_expr_type
            else:
                if not type_eq(o.inferred_return_type, ret_expr_type):
                    raise TypeMismatchInStatement(node)
        else:
            # explicit return type
            if not type_eq(func.return_type, ret_expr_type):
                raise TypeMismatchInStatement(node)

    def visit_expr_stmt(self, node: "ExprStmt", o: CheckEnv):
        old_is_stmt = getattr(o, 'is_stmt', False)
        o.is_stmt = True
        self.visit(node.expr, o)
        o.is_stmt = old_is_stmt

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        
        # We might need to propagate type hints down if one side is known and the other is auto
        ltype = self.visit(node.left, o)
        rtype = self.visit(node.right, o)
        
        op = node.operator
        
        if op in ['+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=', '&&', '||']:
            # Handle auto inference from binary op
            if ltype is None and rtype is None:
                # Both unknown
                pass 
            elif ltype is None and rtype is not None:
                # Infer ltype from rtype
                if isinstance(node.left, Identifier):
                    sym = o.lookup(node.left.name)
                    if sym and sym.is_auto:
                        sym.mtype = rtype
                        sym.is_auto = False
                        ltype = rtype
            elif rtype is None and ltype is not None:
                # Infer rtype from ltype
                if isinstance(node.right, Identifier):
                    sym = o.lookup(node.right.name)
                    if sym and sym.is_auto:
                        sym.mtype = ltype
                        sym.is_auto = False
                        rtype = ltype
            
            # Now check types
            if ltype is None or rtype is None:
                if op in ['&&', '||', '%', '!', '++', '--']: # Operators that REQUIRE int
                    # We could infer int here
                    if ltype is None and isinstance(node.left, Identifier):
                        sym = o.lookup(node.left.name)
                        if sym and sym.is_auto: sym.mtype = IntType(); sym.is_auto = False; ltype = IntType()
                    if rtype is None and isinstance(node.right, Identifier):
                        sym = o.lookup(node.right.name)
                        if sym and sym.is_auto: sym.mtype = IntType(); sym.is_auto = False; rtype = IntType()

            if ltype is None or rtype is None:
                # Still unknown. Raising TypeCannotBeInferred for the first auto operand found.
                if ltype is None and isinstance(node.left, Identifier):
                    raise TypeCannotBeInferred(node.left)
                if rtype is None and isinstance(node.right, Identifier):
                    raise TypeCannotBeInferred(node.right)
                raise TypeMismatchInExpression(node)

            # Re-verify with resolved types
            if op in ['+', '-', '*', '/']:
                if isinstance(ltype, (IntType, FloatType)) and isinstance(rtype, (IntType, FloatType)):
                    return FloatType() if isinstance(ltype, FloatType) or isinstance(rtype, FloatType) else IntType()
            elif op == '%':
                if isinstance(ltype, IntType) and isinstance(rtype, IntType): return IntType()
            elif op in ['==', '!=', '<', '>', '<=', '>=']:
                if isinstance(ltype, (IntType, FloatType)) and isinstance(rtype, (IntType, FloatType)): return IntType()
            elif op in ['&&', '||']:
                if isinstance(ltype, IntType) and isinstance(rtype, IntType): return IntType()
                
            raise TypeMismatchInExpression(node)
        
        raise TypeMismatchInExpression(node)

    def visit_prefix_op(self, node: "PrefixOp", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        etype = self.visit(node.operand, o)
        op = node.operator
        
        if etype is None and isinstance(node.operand, Identifier):
            sym = o.lookup(node.operand.name)
            if sym and sym.is_auto:
                if op in ['++', '--', '!']:
                    sym.mtype = IntType(); sym.is_auto = False; etype = IntType()
                # for + / - we still don't know if it's int or float
        
        if etype is None: raise TypeMismatchInExpression(node)

        if op in ['++', '--']:
            if not isinstance(etype, IntType) or not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            return IntType()
        elif op in ['+', '-']:
            if isinstance(etype, (IntType, FloatType)): return etype
        elif op == '!':
            if isinstance(etype, IntType): return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_postfix_op(self, node: "PostfixOp", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        etype = self.visit(node.operand, o)
        op = node.operator
        
        if etype is None and isinstance(node.operand, Identifier):
            sym = o.lookup(node.operand.name)
            if sym and sym.is_auto:
                if op in ['++', '--']:
                    sym.mtype = IntType(); sym.is_auto = False; etype = IntType()

        if etype is None: raise TypeMismatchInExpression(node)

        if op in ['++', '--']:
            if not isinstance(etype, IntType) or not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: "AssignExpr", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
            
        ltype = self.visit(node.lhs, o)
        
        # If LHS is unknown auto, we don't have a hint for RHS yet
        # But if LHS is known, we can use it as hint for RHS (especially for StructLiterals)
        rtype = self.visit(node.rhs, (o, ltype))
        
        if ltype is None:
            if rtype is not None:
                # Infer LHS from RHS
                if isinstance(node.lhs, Identifier):
                    sym = o.lookup(node.lhs.name)
                    if sym and sym.is_auto:
                        sym.mtype = rtype
                        sym.is_auto = False
                        ltype = rtype
            else:
                # Both unknown
                if isinstance(node.lhs, Identifier):
                    raise TypeCannotBeInferred(node.lhs)
                raise TypeMismatchInExpression(node)

        if not type_eq(ltype, rtype):
            if getattr(o, 'is_stmt', False):
                raise TypeMismatchInStatement(node)
            raise TypeMismatchInExpression(node)
            
        return ltype

    def visit_member_access(self, node: "MemberAccess", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        obj_type = self.visit(node.obj, o)
        if not isinstance(obj_type, StructType):
            raise TypeMismatchInExpression(node)
            
        struct_decl = o.structs.get(obj_type.struct_name)
        if not struct_decl: raise UndeclaredStruct(obj_type.struct_name)
            
        for member in struct_decl.members:
            if member.name == node.member: return member.member_type
                
        raise TypeMismatchInExpression(node)

    def visit_func_call(self, node: "FuncCall", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        if node.name not in o.funcs:
            raise UndeclaredFunction(node.name)
            
        func = o.funcs[node.name]
        if len(func.params) != len(node.args):
            raise TypeMismatchInExpression(node)
            
        for param, arg in zip(func.params, node.args):
            arg_type = self.visit(arg, (o, param.param_type))
            
            # auto param inference? 
            # TyC parameters CANNOT be auto. So param.param_type is always known.
            if arg_type is None and isinstance(arg, Identifier):
                sym = o.lookup(arg.name)
                if sym and sym.is_auto:
                    sym.mtype = param.param_type
                    sym.is_auto = False
                    arg_type = param.param_type

            if not type_eq(param.param_type, arg_type):
                raise TypeMismatchInExpression(node)
                
        # By the time we call a function, its return type should be fixed (no forward refs)
        return func.return_type

    def visit_identifier(self, node: "Identifier", o_in: Any):
        o = o_in[0] if isinstance(o_in, tuple) else o_in
        sym = o.lookup(node.name)
        if not sym:
            # Check if it's a function name? 
            # In TyC, functions are global, but identifiers are usually variables/params.
            # FuncCall is handled separately.
            raise UndeclaredIdentifier(node.name)
            
        if sym.is_auto and sym.mtype is None:
            # If we are here and we don't have a hint, we might return None
            # and let the caller decide if it's an error.
            return None
            
        return sym.mtype

    def visit_struct_literal(self, node: "StructLiteral", o_in: Any):
        if not isinstance(o_in, tuple) or o_in[1] is None or not isinstance(o_in[1], StructType):
            # No context hint or hint is not a struct
            return None
            
        o, expected_type = o_in
        struct_decl = o.structs.get(expected_type.struct_name)
        if not struct_decl: raise UndeclaredStruct(expected_type.struct_name)
            
        if len(struct_decl.members) != len(node.values):
            raise TypeMismatchInExpression(node)
            
        for member, val_expr in zip(struct_decl.members, node.values):
            val_type = self.visit(val_expr, (o, member.member_type))
            if not type_eq(member.member_type, val_type):
                raise TypeMismatchInExpression(node)
                
        return expected_type

    # Literals
    def visit_int_literal(self, node: "IntLiteral", o: CheckEnv):
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: CheckEnv):
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: CheckEnv):
        return StringType()
