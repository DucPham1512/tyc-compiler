"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):

    def _build_left_associative(self, operands, operators):
        expr = operands[0]
        for op, right in zip(operators, operands[1:]):
            expr = BinaryOp(expr, op.getText(), right)
        return expr

    def _get_token_index(self, token):
        if hasattr(token, "tokenIndex"):
            return token.tokenIndex
        if hasattr(token, "getSymbol"):
            return token.getSymbol().tokenIndex
        return -1

    # ------------------------------------------------------------------
    # Program and declarations
    # ------------------------------------------------------------------

    def visitProgram(self, ctx: TyCParser.ProgramContext):
        decls = []
        for child in ctx.children or []:
            if isinstance(
                child,
                (
                    TyCParser.FuncDeclContext,
                    TyCParser.VoidFuncDeclContext,
                    TyCParser.StructDeclContext,
                ),
            ):
                decls.append(self.visit(child))
        return Program(decls)

    # Function declarations

    def visitVoidFuncDecl(self, ctx: TyCParser.VoidFuncDeclContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.paramList()) if ctx.paramList() else []
        body = self.visit(ctx.blockStmt())
        return FuncDecl(VoidType(), name, params, body)

    def visitFuncDecl(self, ctx: TyCParser.FuncDeclContext):
        return_type = self.visit(ctx.type_()) if ctx.type_() else None
        name = ctx.ID().getText()
        params = self.visit(ctx.paramList()) if ctx.paramList() else []
        body = self.visit(ctx.blockStmt())
        return FuncDecl(return_type, name, params, body)

    # Parameters

    def visitParamList(self, ctx: TyCParser.ParamListContext):
        return [self.visit(param) for param in ctx.param()]

    def visitParam(self, ctx: TyCParser.ParamContext):
        return Param(self.visit(ctx.type_()), ctx.ID().getText())

    # Types

    def visitType(self, ctx: TyCParser.TypeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        return StructType(ctx.ID().getText())

    # Struct declarations

    def visitStructDecl(self, ctx: TyCParser.StructDeclContext):
        members = [self.visit(member) for member in ctx.structMemberDecl()]
        return StructDecl(ctx.ID().getText(), members)

    def visitStructMemberDecl(self, ctx: TyCParser.StructMemberDeclContext):
        return MemberDecl(self.visit(ctx.type_()), ctx.ID().getText())

    # ------------------------------------------------------------------
    # Statements
    # ------------------------------------------------------------------

    def visitVarDecl(self, ctx: TyCParser.VarDeclContext):
        return self.visit(ctx.varDeclNoSemi())

    def visitVarDeclNoSemi(self, ctx: TyCParser.VarDeclNoSemiContext):
        if ctx.structInitNoSemi():
            return self.visit(ctx.structInitNoSemi())
        name = ctx.ID().getText()
        value = self.visit(ctx.expr()) if ctx.expr() else None
        if ctx.AUTO():
            return VarDecl(None, name, value)
        return VarDecl(self.visit(ctx.type_()), name, value)

    def visitStructInitNoSemi(self, ctx: TyCParser.StructInitNoSemiContext):
        var_type = self.visit(ctx.type_())
        name = ctx.ID().getText()
        values = self.visit(ctx.exprList()) if ctx.exprList() else []
        return VarDecl(var_type, name, StructLiteral(values))

    def visitExprStmt(self, ctx: TyCParser.ExprStmtContext):
        return ExprStmt(self.visit(ctx.expr()))

    def visitIfStmt(self, ctx: TyCParser.IfStmtContext):
        condition = self.visit(ctx.expr())
        blocks = ctx.blockStmt()
        stmts = ctx.stmt()

        # then branch: first blockStmt or first stmt
        if blocks:
            then_stmt = self.visit(blocks[0])
            else_stmt = self.visit(blocks[1]) if len(blocks) > 1 else None
            # if there's a stmt (braceless else after a braced then)
            if else_stmt is None and stmts:
                else_stmt = self.visit(stmts[0])
        else:
            then_stmt = self.visit(stmts[0])
            else_stmt = self.visit(stmts[1]) if len(stmts) > 1 else None

        return IfStmt(condition, then_stmt, else_stmt)

    def visitWhileStmt(self, ctx: TyCParser.WhileStmtContext):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.blockStmt()) if ctx.blockStmt() else self.visit(ctx.stmt())
        return WhileStmt(condition, body)

    def visitForStmt(self, ctx: TyCParser.ForStmtContext):
        init = self.visit(ctx.forInit()) if ctx.forInit() else None
        if isinstance(init, Expr):
            init = ExprStmt(init)
        condition = self.visit(ctx.forCond()) if ctx.forCond() else None
        update = self.visit(ctx.forUpdate()) if ctx.forUpdate() else None
        body = self.visit(ctx.blockStmt()) if ctx.blockStmt() else self.visit(ctx.stmt())
        return ForStmt(init, condition, update, body)

    def visitForInit(self, ctx: TyCParser.ForInitContext):
        if ctx.varDeclNoSemi():
            return self.visit(ctx.varDeclNoSemi())
        return self.visit(ctx.expr())

    def visitForCond(self, ctx: TyCParser.ForCondContext):
        return self.visit(ctx.expr())

    def visitForUpdate(self, ctx: TyCParser.ForUpdateContext):
        return self.visit(ctx.expr())

    def visitSwitchStmt(self, ctx: TyCParser.SwitchStmtContext):
        expr = self.visit(ctx.expr())
        cases = []
        default = None

        for section in ctx.switchSection():
            result = self.visit(section)
            if isinstance(result, DefaultStmt):
                default = result
            elif isinstance(result, list):
                cases.extend(result)
            else:
                cases.append(result)

        return SwitchStmt(expr, cases, default)

    def visitSwitchSection(self, ctx: TyCParser.SwitchSectionContext):
        if ctx.caseSection():
            return self.visit(ctx.caseSection())
        return self.visit(ctx.defaultSection())

    def visitCaseSection(self, ctx: TyCParser.CaseSectionContext):
        # caseLabel+ stmt* — take first label's expr for CaseStmt
        # multiple labels (fall-through grouping) each get their own CaseStmt
        # sharing the same statement list
        stmts = [self.visit(s) for s in ctx.stmt()]
        labels = [self.visit(label) for label in ctx.caseLabel()]
        # return list of CaseStmt, one per label, all sharing the same stmts
        return [CaseStmt(label_expr, list(stmts)) for label_expr in labels]

    def visitDefaultSection(self, ctx: TyCParser.DefaultSectionContext):
        stmts = [self.visit(s) for s in ctx.stmt()]
        return DefaultStmt(stmts)

    def visitCaseLabel(self, ctx: TyCParser.CaseLabelContext):
        return self.visit(ctx.expr())

    def visitContinueStmt(self, ctx: TyCParser.ContinueStmtContext):
        return ContinueStmt()

    def visitBreakStmt(self, ctx: TyCParser.BreakStmtContext):
        return BreakStmt()

    def visitReturnStmt(self, ctx: TyCParser.ReturnStmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return ReturnStmt(expr)

    def visitStmt(self, ctx: TyCParser.StmtContext):
        if ctx.exprStmt():
            return self.visit(ctx.exprStmt())
        if ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        if ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        if ctx.forStmt():
            return self.visit(ctx.forStmt())
        if ctx.switchStmt():
            return self.visit(ctx.switchStmt())
        if ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        if ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        if ctx.blockStmt():
            return self.visit(ctx.blockStmt())
        return self.visit(ctx.returnStmt())

    def visitBlockStmt(self, ctx: TyCParser.BlockStmtContext):
        stmts = []
        for child in ctx.children or []:
            if isinstance(child, TyCParser.VarDeclContext):
                stmts.append(self.visit(child))
            elif isinstance(child, TyCParser.StmtContext):
                stmts.append(self.visit(child))
        return BlockStmt(stmts)

    # ------------------------------------------------------------------
    # Expressions
    # ------------------------------------------------------------------

    def visitExprList(self, ctx: TyCParser.ExprListContext):
        return [self.visit(expr_ctx) for expr_ctx in ctx.expr()]

    def visitExpr(self, ctx: TyCParser.ExprContext):
        return self.visit(ctx.assignExpr())

    def visitAssignExpr(self, ctx: TyCParser.AssignExprContext):
        if ctx.lvalue():
            lhs = self.visit(ctx.lvalue())
            rhs = self.visit(ctx.assignExpr())
            return AssignExpr(lhs, rhs)
        return self.visit(ctx.logicalOr())

    def visitLvalue(self, ctx: TyCParser.LvalueContext):
        ids = ctx.ID()
        expr = Identifier(ids[0].getText())
        for member_token in ids[1:]:
            expr = MemberAccess(expr, member_token.getText())
        return expr

    def visitLogicalOr(self, ctx: TyCParser.LogicalOrContext):
        operands = [self.visit(and_ctx) for and_ctx in ctx.logicalAnd()]
        return self._build_left_associative(operands, ctx.OR())

    def visitLogicalAnd(self, ctx: TyCParser.LogicalAndContext):
        operands = [self.visit(eq_ctx) for eq_ctx in ctx.equality()]
        return self._build_left_associative(operands, ctx.AND())

    def visitEquality(self, ctx: TyCParser.EqualityContext):
        operands = [self.visit(rel_ctx) for rel_ctx in ctx.relational()]
        operators = ctx.EQ() + ctx.NEQ()
        operators = sorted(operators, key=self._get_token_index)
        return self._build_left_associative(operands, operators)

    def visitRelational(self, ctx: TyCParser.RelationalContext):
        operands = [self.visit(add_ctx) for add_ctx in ctx.additive()]
        operators = ctx.LT() + ctx.LE() + ctx.GT() + ctx.GE()
        operators = sorted(operators, key=self._get_token_index)
        return self._build_left_associative(operands, operators)

    def visitAdditive(self, ctx: TyCParser.AdditiveContext):
        operands = [self.visit(mul_ctx) for mul_ctx in ctx.multiplicative()]
        operators = ctx.PLUS() + ctx.MINUS()
        operators = sorted(operators, key=self._get_token_index)
        return self._build_left_associative(operands, operators)

    def visitMultiplicative(self, ctx: TyCParser.MultiplicativeContext):
        operands = [self.visit(unary_ctx) for unary_ctx in ctx.unary()]
        operators = ctx.MUL() + ctx.DIV() + ctx.MOD()
        operators = sorted(operators, key=self._get_token_index)
        return self._build_left_associative(operands, operators)

    def visitUnary(self, ctx: TyCParser.UnaryContext):
        if ctx.postfix():
            return self.visit(ctx.postfix())
        if ctx.PLUS():
            operator = ctx.PLUS().getText()
        elif ctx.MINUS():
            operator = ctx.MINUS().getText()
        elif ctx.NOT():
            operator = ctx.NOT().getText()
        elif ctx.INC():
            operator = ctx.INC().getText()
        else:
            operator = ctx.DEC().getText()
        return PrefixOp(operator, self.visit(ctx.unary()))

    def visitPostfix(self, ctx: TyCParser.PostfixContext):
        expr = self.visit(ctx.primary())
        for postfix_op_ctx in ctx.postfixOp():
            op_kind, op_value = self.visit(postfix_op_ctx)
            if op_kind == "call":
                func_name = expr.name if isinstance(expr, Identifier) else str(expr)
                expr = FuncCall(func_name, op_value)
            elif op_kind == "member":
                expr = MemberAccess(expr, op_value)
            elif op_kind == "post_inc":
                expr = PostfixOp("++", expr)
            else:
                expr = PostfixOp("--", expr)
        return expr

    def visitPrimary(self, ctx: TyCParser.PrimaryContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.ID():
            return Identifier(ctx.ID().getText())
        if ctx.expr():
            return self.visit(ctx.expr())
        return self.visit(ctx.structLit())

    def visitPostfixOp(self, ctx: TyCParser.PostfixOpContext):
        if ctx.LPAREN():
            args = self.visit(ctx.exprList()) if ctx.exprList() else []
            return ("call", args)
        if ctx.DOT():
            return ("member", ctx.ID().getText())
        if ctx.INC():
            return ("post_inc", None)
        return ("post_dec", None)

    def visitInitElem(self, ctx: TyCParser.InitElemContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        return self.visit(ctx.structLit())

    def visitInitList(self, ctx: TyCParser.InitListContext):
        return [self.visit(elem_ctx) for elem_ctx in ctx.initElem()]

    def visitStructLit(self, ctx: TyCParser.StructLitContext):
        values = self.visit(ctx.initList()) if ctx.initList() else []
        return StructLiteral(values)
