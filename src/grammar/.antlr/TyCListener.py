# Generated from c:/Users/USER/OneDrive/my files/Year 3/Sem 2/PPL/Assignment/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete listener for a parse tree produced by TyCParser.
class TyCListener(ParseTreeListener):

    # Enter a parse tree produced by TyCParser#program.
    def enterProgram(self, ctx:TyCParser.ProgramContext):
        pass

    # Exit a parse tree produced by TyCParser#program.
    def exitProgram(self, ctx:TyCParser.ProgramContext):
        pass


    # Enter a parse tree produced by TyCParser#voidFuncDecl.
    def enterVoidFuncDecl(self, ctx:TyCParser.VoidFuncDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#voidFuncDecl.
    def exitVoidFuncDecl(self, ctx:TyCParser.VoidFuncDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#funcDecl.
    def enterFuncDecl(self, ctx:TyCParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#funcDecl.
    def exitFuncDecl(self, ctx:TyCParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#paramList.
    def enterParamList(self, ctx:TyCParser.ParamListContext):
        pass

    # Exit a parse tree produced by TyCParser#paramList.
    def exitParamList(self, ctx:TyCParser.ParamListContext):
        pass


    # Enter a parse tree produced by TyCParser#param.
    def enterParam(self, ctx:TyCParser.ParamContext):
        pass

    # Exit a parse tree produced by TyCParser#param.
    def exitParam(self, ctx:TyCParser.ParamContext):
        pass


    # Enter a parse tree produced by TyCParser#type.
    def enterType(self, ctx:TyCParser.TypeContext):
        pass

    # Exit a parse tree produced by TyCParser#type.
    def exitType(self, ctx:TyCParser.TypeContext):
        pass


    # Enter a parse tree produced by TyCParser#structDecl.
    def enterStructDecl(self, ctx:TyCParser.StructDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#structDecl.
    def exitStructDecl(self, ctx:TyCParser.StructDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#structMemberDecl.
    def enterStructMemberDecl(self, ctx:TyCParser.StructMemberDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#structMemberDecl.
    def exitStructMemberDecl(self, ctx:TyCParser.StructMemberDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#varDecl.
    def enterVarDecl(self, ctx:TyCParser.VarDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#varDecl.
    def exitVarDecl(self, ctx:TyCParser.VarDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#exprStmt.
    def enterExprStmt(self, ctx:TyCParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#exprStmt.
    def exitExprStmt(self, ctx:TyCParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#exprList.
    def enterExprList(self, ctx:TyCParser.ExprListContext):
        pass

    # Exit a parse tree produced by TyCParser#exprList.
    def exitExprList(self, ctx:TyCParser.ExprListContext):
        pass


    # Enter a parse tree produced by TyCParser#expr.
    def enterExpr(self, ctx:TyCParser.ExprContext):
        pass

    # Exit a parse tree produced by TyCParser#expr.
    def exitExpr(self, ctx:TyCParser.ExprContext):
        pass


    # Enter a parse tree produced by TyCParser#assignExpr.
    def enterAssignExpr(self, ctx:TyCParser.AssignExprContext):
        pass

    # Exit a parse tree produced by TyCParser#assignExpr.
    def exitAssignExpr(self, ctx:TyCParser.AssignExprContext):
        pass


    # Enter a parse tree produced by TyCParser#lvalue.
    def enterLvalue(self, ctx:TyCParser.LvalueContext):
        pass

    # Exit a parse tree produced by TyCParser#lvalue.
    def exitLvalue(self, ctx:TyCParser.LvalueContext):
        pass


    # Enter a parse tree produced by TyCParser#logicalOr.
    def enterLogicalOr(self, ctx:TyCParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by TyCParser#logicalOr.
    def exitLogicalOr(self, ctx:TyCParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by TyCParser#logicalAnd.
    def enterLogicalAnd(self, ctx:TyCParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by TyCParser#logicalAnd.
    def exitLogicalAnd(self, ctx:TyCParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by TyCParser#equality.
    def enterEquality(self, ctx:TyCParser.EqualityContext):
        pass

    # Exit a parse tree produced by TyCParser#equality.
    def exitEquality(self, ctx:TyCParser.EqualityContext):
        pass


    # Enter a parse tree produced by TyCParser#relational.
    def enterRelational(self, ctx:TyCParser.RelationalContext):
        pass

    # Exit a parse tree produced by TyCParser#relational.
    def exitRelational(self, ctx:TyCParser.RelationalContext):
        pass


    # Enter a parse tree produced by TyCParser#additive.
    def enterAdditive(self, ctx:TyCParser.AdditiveContext):
        pass

    # Exit a parse tree produced by TyCParser#additive.
    def exitAdditive(self, ctx:TyCParser.AdditiveContext):
        pass


    # Enter a parse tree produced by TyCParser#multiplicative.
    def enterMultiplicative(self, ctx:TyCParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by TyCParser#multiplicative.
    def exitMultiplicative(self, ctx:TyCParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by TyCParser#unary.
    def enterUnary(self, ctx:TyCParser.UnaryContext):
        pass

    # Exit a parse tree produced by TyCParser#unary.
    def exitUnary(self, ctx:TyCParser.UnaryContext):
        pass


    # Enter a parse tree produced by TyCParser#postfix.
    def enterPostfix(self, ctx:TyCParser.PostfixContext):
        pass

    # Exit a parse tree produced by TyCParser#postfix.
    def exitPostfix(self, ctx:TyCParser.PostfixContext):
        pass


    # Enter a parse tree produced by TyCParser#primary.
    def enterPrimary(self, ctx:TyCParser.PrimaryContext):
        pass

    # Exit a parse tree produced by TyCParser#primary.
    def exitPrimary(self, ctx:TyCParser.PrimaryContext):
        pass


    # Enter a parse tree produced by TyCParser#postfixOp.
    def enterPostfixOp(self, ctx:TyCParser.PostfixOpContext):
        pass

    # Exit a parse tree produced by TyCParser#postfixOp.
    def exitPostfixOp(self, ctx:TyCParser.PostfixOpContext):
        pass


    # Enter a parse tree produced by TyCParser#ifStmt.
    def enterIfStmt(self, ctx:TyCParser.IfStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#ifStmt.
    def exitIfStmt(self, ctx:TyCParser.IfStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#whileStmt.
    def enterWhileStmt(self, ctx:TyCParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#whileStmt.
    def exitWhileStmt(self, ctx:TyCParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#forStmt.
    def enterForStmt(self, ctx:TyCParser.ForStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#forStmt.
    def exitForStmt(self, ctx:TyCParser.ForStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#forInit.
    def enterForInit(self, ctx:TyCParser.ForInitContext):
        pass

    # Exit a parse tree produced by TyCParser#forInit.
    def exitForInit(self, ctx:TyCParser.ForInitContext):
        pass


    # Enter a parse tree produced by TyCParser#forCond.
    def enterForCond(self, ctx:TyCParser.ForCondContext):
        pass

    # Exit a parse tree produced by TyCParser#forCond.
    def exitForCond(self, ctx:TyCParser.ForCondContext):
        pass


    # Enter a parse tree produced by TyCParser#forUpdate.
    def enterForUpdate(self, ctx:TyCParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by TyCParser#forUpdate.
    def exitForUpdate(self, ctx:TyCParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by TyCParser#varDeclNoSemi.
    def enterVarDeclNoSemi(self, ctx:TyCParser.VarDeclNoSemiContext):
        pass

    # Exit a parse tree produced by TyCParser#varDeclNoSemi.
    def exitVarDeclNoSemi(self, ctx:TyCParser.VarDeclNoSemiContext):
        pass


    # Enter a parse tree produced by TyCParser#structInitNoSemi.
    def enterStructInitNoSemi(self, ctx:TyCParser.StructInitNoSemiContext):
        pass

    # Exit a parse tree produced by TyCParser#structInitNoSemi.
    def exitStructInitNoSemi(self, ctx:TyCParser.StructInitNoSemiContext):
        pass


    # Enter a parse tree produced by TyCParser#initElem.
    def enterInitElem(self, ctx:TyCParser.InitElemContext):
        pass

    # Exit a parse tree produced by TyCParser#initElem.
    def exitInitElem(self, ctx:TyCParser.InitElemContext):
        pass


    # Enter a parse tree produced by TyCParser#initList.
    def enterInitList(self, ctx:TyCParser.InitListContext):
        pass

    # Exit a parse tree produced by TyCParser#initList.
    def exitInitList(self, ctx:TyCParser.InitListContext):
        pass


    # Enter a parse tree produced by TyCParser#structLit.
    def enterStructLit(self, ctx:TyCParser.StructLitContext):
        pass

    # Exit a parse tree produced by TyCParser#structLit.
    def exitStructLit(self, ctx:TyCParser.StructLitContext):
        pass


    # Enter a parse tree produced by TyCParser#switchStmt.
    def enterSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#switchStmt.
    def exitSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#switchSection.
    def enterSwitchSection(self, ctx:TyCParser.SwitchSectionContext):
        pass

    # Exit a parse tree produced by TyCParser#switchSection.
    def exitSwitchSection(self, ctx:TyCParser.SwitchSectionContext):
        pass


    # Enter a parse tree produced by TyCParser#caseSection.
    def enterCaseSection(self, ctx:TyCParser.CaseSectionContext):
        pass

    # Exit a parse tree produced by TyCParser#caseSection.
    def exitCaseSection(self, ctx:TyCParser.CaseSectionContext):
        pass


    # Enter a parse tree produced by TyCParser#defaultSection.
    def enterDefaultSection(self, ctx:TyCParser.DefaultSectionContext):
        pass

    # Exit a parse tree produced by TyCParser#defaultSection.
    def exitDefaultSection(self, ctx:TyCParser.DefaultSectionContext):
        pass


    # Enter a parse tree produced by TyCParser#caseLabel.
    def enterCaseLabel(self, ctx:TyCParser.CaseLabelContext):
        pass

    # Exit a parse tree produced by TyCParser#caseLabel.
    def exitCaseLabel(self, ctx:TyCParser.CaseLabelContext):
        pass


    # Enter a parse tree produced by TyCParser#continueStmt.
    def enterContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#continueStmt.
    def exitContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#breakStmt.
    def enterBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#breakStmt.
    def exitBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#returnStmt.
    def enterReturnStmt(self, ctx:TyCParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#returnStmt.
    def exitReturnStmt(self, ctx:TyCParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#stmt.
    def enterStmt(self, ctx:TyCParser.StmtContext):
        pass

    # Exit a parse tree produced by TyCParser#stmt.
    def exitStmt(self, ctx:TyCParser.StmtContext):
        pass


    # Enter a parse tree produced by TyCParser#blockStmt.
    def enterBlockStmt(self, ctx:TyCParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#blockStmt.
    def exitBlockStmt(self, ctx:TyCParser.BlockStmtContext):
        pass



del TyCParser