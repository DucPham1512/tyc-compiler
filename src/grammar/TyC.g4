grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
program: EOF ;

DIGITS : [0-9]+ ;

BLOCK_CMT : '/*' .*? '*/' -> skip ; // skip block comments

LINE_CMT : '//' .*? ~[\r\n]* -> skip ; // skip line comments

AUTO      : 'auto' ;
BREAK     : 'break' ;
CASE      : 'case' ;
CONTINUE  : 'continue' ;
DEFAULT   : 'default' ;
ELSE      : 'else' ;

FLOAT     : 'float' ;
FOR       : 'for' ;
IF        : 'if' ;
INT       : 'int' ;
RETURN    : 'return' ;
STRING    : 'string' ;
STRUCT    : 'struct' ;

SWITCH    : 'switch' ;
VOID      : 'void' ;
WHILE     : 'while' ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;

// Arithmetic
INC     : '++' ;
DEC     : '--' ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
MOD     : '%' ;

// Comparison
EQ      : '==' ;
NEQ     : '!=' ;
LE      : '<=' ;
GE      : '>=' ; 
LT      : '<' ;
GT      : '>' ;

// Logical
OR      : '||' ;
AND     : '&&' ;
NOT     : '!' ;

// Assignment
ASSIGN  : '=' ;

// Member access
DOT     : '.' ;

LBRACK   : '[' ;
RBRACK   : ']' ;
LBRACE   : '{' ;
RBRACE   : '}' ;
LPAREN   : '(' ;
RPAREN   : ')' ;
SEMI     : ';' ;
COMMA    : ',' ;

// Int Literal
INT_LIT: MINUS?DIGITS ;


// Float Literal
fragment EXP: [eE]MINUS?DIGITS;
// better (more standard): [eE] [+\-]? DIGITS

FLOAT_LIT
  : MINUS? (
        DIGITS '.'                         // 1.
      | DIGITS '.' DIGITS EXP?             // 1.23 or 1.23e4  (requires digits before EXP)
      | '.' DIGITS EXP?                    // .5 or .5e2
    )
  ;

// String Literal
fragment ESC : '\\' [bfnrt"\\] ;
fragment STR_CHAR : ~["\\\r\n] | ESC ;

STRING_LIT
  : '"' STR_CHAR* '"'
  ;

ILLEGAL_ESCAPE
  : '"' (STR_CHAR* '\\' ~[bfnrt"\\]) .*? '"'?   // bad escape after backslash
  ;

UNCLOSE_STRING
  : '"' STR_CHAR* (EOF | '\r' | '\n')
  ;

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs

ERROR_CHAR: .;
// ILLEGAL_ESCAPE:.;
// UNCLOSE_STRING:.;
