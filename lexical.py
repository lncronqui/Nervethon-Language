#######################################
# CONSTANTS
#######################################

lowercase         = "[:lower]" 
uppercase         = "[:upper:]"
letters           = "[:alpha:]"
nonzero           = "[1-9]"
numbers           = "[0-9]"
ascii_input       = "[:word:]"

#######################################
# TOKENS
#######################################

#RESERVED WORDS#
start               = "(^Link)+\.(Start)"
end                 = "(^Link)+\.(End)"
generate            = "(^Generate)"
sys                 = "(^Sys)"
syscall             = "(^Sys)+\.(Call)"
discharge           = "(^Discharge)"
absorb		        = "(^Absorb)"
boolean		        = "(^Boolean)"
integer		        = "(^Integer)"
decimal		        = "(^Decimal)"
string		        = "(^String)"
if_statement        = "(^If)"
elif_statement      = "(^Elif)"
else_statement	    = "(^Else)"
switch		        = "(^Switch)"
execute		        = "(^Execute)"
default		        = "(^Default)"
for_loop		    = "(^For)"
while_loop          = "(^While)"
exit_statement      = "(^Exit)"
continue_statement	= "(^Continue)"
avoid		        = "(^Avoid)"
fixed		        = "(^Fixed)"
struct		        = "(^Struct)"
void		        = "(^Void)"
return_statement    = "(^Return)"
boolean_true		= "(^True)"
boolean_false		= "(^False)"

#UNARY OPERATORS#
unary_plus		    = "+"
unary_minus         = "-"

#ARITHMETIC OPERATORS#
arithop_mul         = "*"
arithop_div         = "/"
arithop_per         = "%"
arithop_mod         = "**"
arithop_exp         = "//"

#RELATIONAL OPERATORS#
relateop_gthan          = "<"
relateop_lthan          = ">"
relateop_eqto           = "=="
relateop_noteqto        = "!="
relateop_gthanoreqto    = ">="
relateop_lthanoreqto    = "<="

#ASSIGNMENT OPERATORS#
assignop_simple     = "="
assignop_addAND     = "+="
assignop_subAND     = "-="
assignop_multAND    = "*="
assignop_divAND     = "/="
assignop_floorAND   = "//="
assignop_modAND     = "%="
assignop_exAND      = "**="

#LOGICAL OPERATORS#
logicalop_and   = "(^And)"
logicalop_or    = "(^Or)"
logicalop_not   = "(^Not)"

#OPEN SYMBOLS#
open_parenthesis    = "("
open_curly          = "{"
open_bracket        = "["
open_quotation      = '"'

#CLOSE SYMBOLS#
close_parenthesis    = ")"
close_curly          = "}"
close_bracket        = "]"
close_quotation      = '"'

#COMMENT SYMBOLS#
opening_comment     = '/*'
closing_comment     = '*/'

#ESCAPE SEQUENCES SYMBOLS#
newline         = "\n"
tab             = '\t'
double_quote    = '\"'
single_quote    = '\''
backslash       = '\\'

#OTHER SYMBOLS#
color        = ":"
period       = "."
semicolon    = ";"
comma        = ","

#IDENTIFIERS#
identifier   = "([a-z]+[:word:]){1,19}"

#LITERALS#
lit_intposi     = "[1-9]{1,9}"
lit_intnega     = "-+[1-9]{1,9}"   
lit_decposi     = "[1-9]{1,9}+\.[1-9]{1,9}"
lit_decnega     = "^-+[1-9]{1,9}+\.[1-9]{1,9}"
lit_string      = "(:alpha:)"
lit_bool        = "(True | False)"

#######################################
# REGEX
#######################################

import re

with open('C:\Users\mE\Downloads\FirstCode.txt', encoding='utf8') as f:
    lines = [line.rstrip('\n') for line in f]

#RESERVED WORDS#

if(re.search(TT_START, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_END, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_GENERATE, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_SYS, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_SYSCALL, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ABSORB, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_BOOLEAN, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_INTEGER, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_DECIMAL, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_STRING, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_IF, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ELIF, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ELSE, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_SWITCH, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_EXECUTE, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_DEFAULT, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_FOR, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_DO, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_WHILE, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_EXIT, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_CONTINUE, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_AVOID, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_FIXED, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_STRUCT, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_VOID, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_RETURN, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_TRUE, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_FALSE, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_FALSE, lines)):
    print(lines + "- " + "Reserved Word")

#UNARY OPERATORS#
elif(re.search(TT_UNARY1, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_UNARY2, lines)):
    print(lines + "- " + "Reserved Word")

#ARITHMETIC OPERATORS#
elif(re.search(TT_ARITHOP1, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ARITHOP2, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ARITHOP3, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ARITHOP4, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ARITHOP5, lines)):
    print(lines + "- " + "Reserved Word")

#RELATIONAL OPERATORS#
elif(re.search(TT_RELATEOP1, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_RELATEOP2, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_RELATEOP3, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_RELATEOP4, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_RELATEOP5, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_RELATEOP6, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_RELATEOP7, lines)):
    print(lines + "- " + "Reserved Word")

#ASSIGNMENT OPERATORS#
elif(re.search(TT_ASSIGNOP1, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ASSIGNOP2, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ASSIGNOP3, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ASSIGNOP4, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ASSIGNOP5, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ASSIGNOP6, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ASSIGNOP7, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ASSIGNOP8, lines)):
    print(lines + "- " + "Reserved Word")

#LOGICAL OPERATORS#
elif(re.search(TT_LOGICALOP1, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_LOGICALOP2, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_LOGICALOP3, lines)):
    print(lines + "- " + "Reserved Word")

#OPEN SYMBOLS#
elif(re.search(TT_OPENSYM1, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_OPENSYM2, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_OPENSYM3, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_OPENSYM4, lines)):
    print(lines + "- " + "Reserved Word")

#CLOSE SYMBOLS#
elif(re.search(TT_CLOSESYM1, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_CLOSESYM2, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_CLOSESYM3, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_CLOSESYM4, lines)):
    print(lines + "- " + "Reserved Word")

#COMMENT SYMBOLS#
elif(re.search(TT_COMMENT1, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_COMMENT2, lines)):
    print(lines + "- " + "Reserved Word")

#ESCAPE SEQUENCES SYMBOLS#
elif(re.search(TT_ESCAPESEQ1, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ESCAPESEQ2, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ESCAPESEQ3, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ESCAPESEQ4, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_ESCAPESEQ5, lines)):
    print(lines + "- " + "Reserved Word")

#OTHER SYMBOLS#
elif(re.search(TT_COLON, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_PERIOD, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_SEMICOLON, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_COMMA, lines)):
    print(lines + "- " + "Reserved Word")
elif(re.search(TT_SPACE, lines)):
    print(lines + "- " + "Reserved Word")

#IDENTIFIERS#
elif(re.search(TT_IDENTIFIER, lines)):
    print(lines + "- " + "id")

#LITERALS#
else:
    print("Invalid Token")
