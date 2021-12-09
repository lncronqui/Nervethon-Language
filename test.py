import re
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

#UNARY OPERATORS#
unary_plus		    = "^[+]$"
unary_minus         = "^[-]$"

#ARITHMETIC OPERATORS#
arithop_mul         = "^[*]$"
arithop_div         = "^[/]$"
arithop_per         = "^[%]$"
arithop_mod         = "^[*][*]$"
arithop_exp         = "^[/][/]$"

#RELATIONAL OPERATORS#
relateop_gthan          = "^[<]$"
relateop_lthan          = "^[>]$"
relateop_eqto           = "^[=][=]$"
relateop_noteqto        = "^[!][=]$"
relateop_gthanoreqto    = "^[>][=]$"
relateop_lthanoreqto    = "^[<][=]$"

#ASSIGNMENT OPERATORS#
assignop_simple     = "^[=]$"
assignop_addAND     = "^[+][=]$"
assignop_subAND     = "^[-][=]$"
assignop_multAND    = "^[*][=]$"
assignop_divAND     = "^[/][=]$"
assignop_floorAND   = "^[/][/][=]$"
assignop_modAND     = "^[%][=]$"
assignop_exAND      = "^[*][*][=]$"

#LOGICAL OPERATORS#
logicalop_and   = "(^And)"
logicalop_or    = "(^Or)"
logicalop_not   = "(^Not)"

#OPEN SYMBOLS#
open_parenthesis    = "^\($"
open_curly          = "^\{$"
open_bracket        = "^\[$"
open_quotation      = "^\"$"

#CLOSE SYMBOLS#
close_parenthesis    = "^\)$"
close_curly          = "^\}$"
close_bracket        = "^\]$"
close_quotation      = "^\"$"

#COMMENT SYMBOLS#
comment_full     = "^[/][*]\w*[*][/]$"
comment_open        = "^[/][*]"
comment_close       = "\*\/$"

#ESCAPE SEQUENCES SYMBOLS#
newline         = "^\n$"
tab             = "^\t$"
double_quote    = "^\"$"
single_quote    = "^\'$"
backslash       = "^\\$"

#OTHER SYMBOLS#
colon        = "^[:]$"
period       = "^[.]$"
semicolon    = "^[;]$"
comma        = "^[,]$"

#IDENTIFIERS#
identifier   = "^[a-z]\w{0,19}$"

#LITERALS#
lit_intposi     = "^[1-9][\d]{0,8}$"
lit_intnega     = "^\-[1-9][\d]{0,8}$"   
lit_decposi     = "^[0-9]{1,9}\.[0-9]{1,6}"
lit_decnega     = "^\-[0-9]{1,9}\.[0-9]{1,6}"
lit_string      = "^\"[a-zA-Z]\"&"
lit_bool        = "(True|False)"

space           = "\s{0,1}"

def keyword(input):
    reserved = [start, end, generate, sys, syscall, discharge, absorb, if_statement, elif_statement, else_statement, switch, execute, default, for_loop, while_loop, exit_statement, continue_statement, avoid, fixed, struct, void, return_statement]
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

def unary(input):
    unary_op = [unary_minus, unary_plus]
    for x in unary_op:
        if(re.search(x, input)):
            return True
        else:
            continue
    return False

def arith(input):
    arith_op = [arithop_mul, arithop_div, arithop_per, arithop_mod, arithop_exp]
    for x in arith_op:
        if(re.search(x, input)):
            return True
        else:
            continue
    return False

def rel(input):
    relational_op = [relateop_gthan, relateop_lthan, relateop_eqto, relateop_noteqto, relateop_gthanoreqto, relateop_lthanoreqto]
    for x in relational_op:
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

def logical(input):
    logic_op = [logicalop_and, logicalop_or, logicalop_not]
    for x in logic_op:
        if(re.search(x, input)):
            return True
        else:
            continue
    return False

def symbols(input):
    symbol_op = [open_parenthesis, open_curly, open_bracket, open_quotation, close_parenthesis, close_curly, close_bracket, close_quotation, newline, tab, backslash, colon, period, semicolon, comma, single_quote, double_quote]
    for x in symbol_op:
        if(re.search(x, input)):
            return True
        else:
            continue
    return False

def check_comment(input):
    if (re.search(comment_close, input)):
        return True
    else:
        return False

#######################################
# REGEX
#######################################

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
    
    #OPERATORS#
    elif(unary(current_char)==True):
        print(current_char + "\t-\tUnary Operator")
    elif(arith(current_char)==True):
        print(current_char + "\t-\tArithmetic Operator")
    elif(rel(current_char)==True):
        print(current_char + "\t-\tRelational Operator")
    elif(assign(current_char)==True):
        print(current_char + "\t-\tAssignment Operator")
    elif(logical(current_char)==True):
        print(current_char + "\t-\tLogical Operator")

    #SYMBOLS#
    elif(symbols(current_char)==True):
        print(current_char + "\t-\tSymbol")
    elif(re.search("N_L", current_char)):
        print("\\n" + "\t-\tNew Line")
    elif(re.search(identifier, current_char)):
        print(current_char + "\t-\tid")
    elif(re.search(comment_open, current_char)):
        comment_str = current_char
        c = check_comment(current_char)
        while (c == False):
            count += 1
            if(count >= len(lexeme)):
                break
            current_char = lexeme[count]
            comment_str += " " + current_char
            c = check_comment(current_char)
            if(c == True):
                break
        print(comment_str + "\t-\tComment")
            
    
    #INTEGERS#
    elif(re.search(lit_intposi, current_char)):
        print(current_char + "\t-\tPositive Integer Literal")
    elif(re.search(lit_intnega, current_char)):
        print(current_char + "\t-\tNegative Integer Literal")
    elif(re.search(lit_decposi, current_char)):
        print(current_char + "\t-\tPositive Decimal Literal")
    elif(re.search(lit_decnega, current_char)):
        print(current_char + "\t-\tNegative Decimal Literal")
    elif(re.search(lit_string, current_char)):
        print(current_char + "\t-\tString Literal")
    elif(re.search(lit_bool, current_char)):
        print(current_char + "\t-\tBoolean Literal")
    elif(re.search(space, current_char)):
        print("Space" + "\t-\tWhitespace")
    else:
        print(current_char + "\t-\tInvalid Input")
        
