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
unary_plus		    = "^[+]$"
unary_minus         = "^[-]$"

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
assignop_simple     = "[=]"
assignop_addAND     = "[+][=]"
assignop_subAND     = "[-][=]"
assignop_multAND    = "[*=]"
assignop_divAND     = "[/=]"
assignop_floorAND   = "[//=]"
assignop_modAND     = "[%=]"
assignop_exAND      = "[**=]"

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
identifier   = "^[a-z][a-zA-Z0-9]{0,19}"

#LITERALS#
lit_intposi     = "^[1-9]{1,9}$"
lit_intnega     = "^\-([1-9]{1,9})$"   
lit_decposi     = "^[0-9]{1,9}\.[0-9]{1,6}"
lit_decnega     = "^\-([0-9]{1,9})\.[0-9]{1,6}"
lit_string      = "(:alpha:)"
lit_bool        = "(True|False)"

def keyword(input):
    reserved = [start, end, generate, sys, syscall, discharge, absorb, if_statement, elif_statement, else_statement, switch, execute, default, for_loop, while_loop, exit_statement, continue_statement, avoid, fixed, struct, void, return_statement, boolean_true, boolean_false]
    for x in reserved:
        if(re.search(x, input)):
            return True
        else:
            continue
    return False

def datatype(input):
    types = [integer, string, boolean, decimal]
    for x in types:
        if(re.search(x, input)):
            return True
        else:
            continue
    return False

def arith(input):
    arith_op = [unary_minus, unary_plus]
    for x in arith_op:
        if(re.search(x, input)):
            return True
        else:
            continue
    return False

def assign(input):
    assign_op = [assignop_addAND, assignop_divAND, assignop_exAND, assignop_floorAND, assignop_modAND, assignop_multAND, assignop_simple, assignop_subAND]
    for x in assign_op:
        if(re.search(x, input)):
            return True
        else:
            continue
    return False
#######################################
# REGEX
#######################################

import re

with open('user_input.txt', 'r') as file:
    user_input = file.read().replace('\n', ' N_L ').replace('\t', '')#\n
lexeme = user_input.split() #splitting based on whitespace -- array of String
#i like cats --> [i, like, cats]
count = -1

while(count < len(lexeme)):
    count += 1
    if(count >= len(lexeme)):
        break
    current_char = lexeme[count]
    if(keyword(current_char)==True):
        print(current_char + "\t-\tKeyword")
    elif(datatype(current_char)==True):
        print(current_char + "\t-\tData Type")
    
    elif(arith(current_char)==True):
        print(current_char + "\t-\tArithmetic Operator")
    elif(assign(current_char)==True):
        print(current_char + "\t-\tAssignment Operator")
    elif(re.search("N_L", current_char)):
        print("\\n" + "\t-\tNew Line")
    elif(re.search(identifier, current_char)):
        print(current_char + "\t-\tid")
    elif(re.search(lit_intposi, current_char)):
        print(current_char + "\t-\tPositive Integer Literal")
    elif(re.search(lit_intnega, current_char)):
        print(current_char + "\t-\tNegative Integer Literal")
    elif(re.search(lit_decposi, current_char)):
        print(current_char + "\t-\tPositive Decimal Literal")
    elif(re.search(lit_decnega, current_char)):
        print(current_char + "\t-\tNegative Decimal Literal")
    else:
        print(current_char + "\t-\tInvalid Input")
        
          