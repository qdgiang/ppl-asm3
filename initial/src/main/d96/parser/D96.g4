// STUDENT ID: 1952044
// STUDENT NAME: QUACH DANG GIANG

// FINAL CHECK

grammar D96;

@lexer::header {
from lexererr import *
}

/* 
@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}*/


options {
	language = Python3;
}

/* PARSER */

// 2.1
program: classdecl* EOF;
classdecl: CLASS ID (COLON ID)? LCB member_list RCB;
member_list: member*;
member: attribute | method;

method: (ID | DOLLARID) LP paralist? RP block_statement 
| cons_method 
| dest_method;

cons_method: CONSTRUCTOR LP paralist? RP block_statement;

dest_method: DESTRUCTOR LP RP block_statement;

paralist: parameter (SEMI parameter)*;
parameter: id_list COLON typename;

block_statement: LCB statement_list? RCB; // TODO
statement_list: statement+;
statement: var_dec | assign_sta | if_statement
| for_in_statement | break_statement | continue_statement
| return_statement | method_statement | block_statement;

var_dec: (VAL | VAR) id_list COLON typename (ASSIGNOP expr_list)? SEMI;
//assign_sta: 
//(ID 
//| DOLLARID 
//| expr index_operator 
//| expr DOT ID
//| expr DOUBLECOLON DOLLARID) 
assign_sta: expr ASSIGNOP expr SEMI;
if_statement: if_clause elseif_clause? else_clause? ;
if_clause: IF LP expr RP block_statement;
elseif_clause: (ELSEIF LP expr RP block_statement)+;
else_clause: ELSE block_statement;


//for_in_statement: FOREACH LP (ID | DOLLARID) IN INTLIT DOUBLEDOT INTLIT
//(BY INTLIT)? RP block_statement;

for_in_statement: FOREACH LP (ID | DOLLARID) IN expr DOUBLEDOT expr
(BY expr)? RP block_statement;

break_statement: BREAK SEMI;
continue_statement: CONTINUE SEMI;
return_statement: RETURN expr? SEMI;

method_statement: expr DOT ID LP expr_list? RP SEMI
| expr DOUBLECOLON DOLLARID LP expr_list? RP SEMI;

//indexedarray: ARRAY LP lit (CM lit)* RP;
indexedarray: ARRAY LP expr_list? RP;
multiarray: ARRAY LP arr_list RP;
arr_list: (multiarray | indexedarray) (CM arr_list)?;
//arr_list: arr (CM arr_list)?;
//arr: multiarray | indexedarray;

attribute: (VAL | VAR) id_list COLON typename (ASSIGNOP expr_list)? SEMI;
id_list: (ID | DOLLARID) (CM (ID | DOLLARID))*;

expr_list: expr (CM expr)*;
// expr(CM expr_list)?;


expr: LP expr RP
| create_object
| expr DOUBLECOLON DOLLARID 
| expr DOUBLECOLON DOLLARID LP expr_list? RP
| expr DOT ID 
| expr DOT ID LP expr_list? RP
//| expr element_expression
//| expr LP expr_list? RP
| expr index_operator
| <assoc=right> SUBOP expr
| <assoc=right> NOTOP expr
| expr (MULOP | DIVOP | PERCENTOP) expr
| expr (ADDOP | SUBOP) expr
| expr (ANDOP | OROP) expr
| expr (EQ_OP | NOT_EQ_OP | SM_OP | GR_OP | SM_EQ_OP | GR_EQ_OP) expr
| expr (ADD_DOT_OP | EQ_DOT_OP) expr
| lit
| SELF
| indexedarray | multiarray
| NULL
| ID
| DOLLARID;
/* 
expr: expr1 (ADD_DOT_OP | EQ_DOT_OP) expr1 | expr1;
expr1: expr2 (EQ_OP | NOT_EQ_OP | SM_OP | GR_OP | SM_EQ_OP | GR_EQ_OP) expe2 | expr2;
expr2: expr3 (ANDOP | OROP) expr3 | expr3;
expr3: */
create_object:  NEW ID LP expr_list? RP;
//element_expression: expr index_operator;
//index_operator: LSB expr RSB index_operator?;
index_operator: (LSB expr RSB)+;
//instance_attribute_access: expr DOT ID;
//static_attribute_access: expr DOUBLECOLON DOLLARID;
//instance_method_call: expr DOT ID LP expr_list? RP;
//static_method_call: expr DOUBLECOLON DOLLARID LP expr_list? RP;

lit: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT;
typename: INTTYPE | FLOATTYPE| STRINGTYPE | BOOLTYPE | arr_decl | ID;
arr_decl: ARRAY LSB (typename | arr_decl) CM  INTLIT RSB;
//array_type: ARRAY LSB (typename | array_type) CM INTLIT RSB;

/* LEXER */
// 3.2
COMMENT : '##' (.)*?  '##' -> skip;  // -> channel(HIDDEN);


// 3.4
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';

FOREACH: 'Foreach';
fragment TRUE: 'True';
fragment FALSE: 'False'; // else boolit wont get recognized
ARRAY: 'Array';
IN: 'In';

INTTYPE: 'Int';
FLOATTYPE: 'Float';
BOOLTYPE: 'Boolean';
STRINGTYPE: 'String';
RETURN: 'Return';

NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
SELF: 'Self';

CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';

// 3.5
ADDOP:'+';
SUBOP:'-';
MULOP:'*';
DIVOP:'/';
PERCENTOP: '%';

NOTOP: '!';
ANDOP: '&&';
OROP: '||';
EQ_OP: '==';
ASSIGNOP: '=';

NOT_EQ_OP: '!=';
GR_OP: '>';
SM_EQ_OP: '<=';
SM_OP: '<';
GR_EQ_OP: '>=';

EQ_DOT_OP: '==.';
ADD_DOT_OP: '+.';
COLON: ':';
DOUBLECOLON: '::';
fragment UNDERSCORE: '_';

// 3.6 SEPERATORS
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
DOT: '.';
CM:',';
SEMI: ';';
LCB: '{';
RCB: '}';
DOUBLEDOT:'..';

// 3.7 lITERALS
INTLIT: EIGHT {self.text = self.text.replace("_", "")}
| SIXTEEN {self.text = self.text.replace("_", "")}
| TWO {self.text = self.text.replace("_", "")}
| TEN {self.text = self.text.replace("_", "")}
| '0';

fragment EIGHT: '0' [0-7] [0-7]* ('_'[0-7]+)*  ;
fragment SIXTEEN: ('0X' | '0x' ) [0-9A-F][0-9A-F]* ('_'[0-9A-F]+)* ;
fragment TWO: ('0b' | '0B') [0-1]+ ('_'[0-1]+)* ;
fragment TEN: [1-9] [0-9]*('_' [0-9]+)* ;
//fragment ZERO: '0';

FLOATLIT: INTLIT DECIMAL_PART{self.text = self.text.replace("_", "")} 
| INTLIT EXPONENTIAL_PART{self.text = self.text.replace("_", "")} 
| INTLIT DECIMAL_PART EXPONENTIAL_PART{self.text = self.text.replace("_", "")}
| DECIMAL_PART EXPONENTIAL_PART{self.text = self.text.replace("_", "")};
fragment DECIMAL_PART: DOT INTLIT?;
fragment EXPONENTIAL_PART: ('e' | 'E') (SUBOP | ADDOP)? INTLIT;

BOOLLIT: TRUE | FALSE;

//fragment BACKSPACE: '\b';
//fragment FORMFEED: '\f';
//fragment CARRETURN: '\r';
//fragment NEWLINE: '\n';
//fragment HORTAB: '\t';
fragment DOUBLEQUOTE: '"';
fragment BACKSLASH: '\\';
fragment EscapeSequence: BACKSLASH [btnfr'\\];
fragment IN_STRING_DOUBLEQUOTE:'\'"';
fragment SINGLEQUOTE: '\'';
//STRINGLIT: DOUBLEQUOTE CHARACTER* DOUBLEQUOTE ;
//STRINGLIT: DOUBLEQUOTE (~["\\\r\n] | EscapeSequence |   )* DOUBLEQUOTE {self.text = self.text[1:-1]};
//STRINGLIT: DOUBLEQUOTE (EscapeSequence | Letter | WS)* DOUBLEQUOTE; 
STRINGLIT: DOUBLEQUOTE (EscapeSequence | ~["\\\r\n] | IN_STRING_DOUBLEQUOTE)* DOUBLEQUOTE{self.text = self.text[1:-1]};   // ~[\b\t\f\r\n\\"]
//CHARACTER: Letter | SPECIAL_CHARACTER ;
//SPECIAL_CHARACTER: WHITESPACE_CHARACTER | BACKSLASH SINGLEQUOTE | BACKSLASH BACKSLASH;  // todo: fix whitespace priorty here


// 3.3
DOLLARID: '$'([a-zA-Z] |UNDERSCORE |[0-9])+;

ID: ([a-zA-Z] | UNDERSCORE)([a-zA-Z] | UNDERSCORE | [0-9])*;
// NOT PARSER, EACH ID SHOULD BE A TOKEN



// FRAGMENTS

//fragment PositiveDigit: [1-9];
//fragment Digit: [0-9];
//fragment Letter: [a-zA-Z];
//fragment DOUBLEQUOTE: '"';
//fragment TRUE: 'True';
//fragment FALSE: 'False';
/*fragment IllegalString
    : '\\' ~[bfrnt'\\]
    | '\\'
    ;*/

// 3.1
WS: [ \f\t\r\b\n]+ -> skip; // skip spaces, tabs, newlines, backspace, form feed, carriage return and newline
ERROR_CHAR: .{raise ErrorToken(self.text)};

//ILLEGAL_ESCAPE: DOUBLEQUOTE ('\\' ~[btnfr"'\\] | ~'\\')* '\\' ~[bfrnt'\\]
ILLEGAL_ESCAPE: 
DOUBLEQUOTE (EscapeSequence | ~["\\\r\n] | IN_STRING_DOUBLEQUOTE)* BACKSLASH ~[bfrnt'\\]
    {
        illegal_str = str(self.text)
        raise IllegalEscape(illegal_str[1:])
    };
UNCLOSE_STRING
    : DOUBLEQUOTE (EscapeSequence | ~["\\\r\n] | IN_STRING_DOUBLEQUOTE)* ([\n\r] | EOF)
    {
        unclose_str = str(self.text)
        raise UncloseString(unclose_str[1:])
    }
    ;