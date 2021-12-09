import re

start               = "(^Link)+\.(Start)"
end                 = "(^Link)+\.(End)"
generate            = "(^Generate)"
sys                 = "(^Sys)"
syscall             = "(^Sys)+\.(Call)"
discharge           = "(^Discharge)"
absorb		        = "(^Absorb)"
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

reserved_words = [start, end, generate, sys, syscall, discharge, absorb, if_statement, elif_statement, else_statement, switch, execute, default, for_loop, while_loop, exit_statement, continue_statement, avoid, fixed, struct, void, return_statement]

TT_KW   = 'KEYWORD'

class Token:
    def __init__(token, type_, value=None):
        token.type = type_
        token.value = value
        
    def __repr__(token):
        if token.value: return f'{token.value}\t{token.type}'
        return f'token.type'
    
class Lexer:
    def __init__(user_input, text):
        user_input.text = text
        user_input.pos = -1
        user_input.current_char = None
        user_input.advance()
        
    def advance(user_input):
        user_input.pos += 1
        user_input.current_char = user_input.text[user_input.pos] if user_input.pos < len(user_input.text) else None
        
    def make_tokens(user_input):
        tokens = []
        
        while user_input.current_char != None:
        	#Reserved Words#
            for x in reserved_words:
                tt_rw = False
                if(re.search(x, user_input.current_char)):
                        tokens.append(Token(TT_KW, user_input.current_char))
                        user_input.advance()
                        tt_rw = True
            if tt_rw == True:
                tokens.append(Token(TT_KW, user_input.current_char))
                user_input.advance()
            else:
                tokens.append(Token("invalid", user_input.current_char))
                user_input.advance()
        return tokens

#MAIN FUNCTION#
def run(lexeme):
    lexer = Lexer(lexeme)
    print(" ".join(lexeme))
    tokens = lexer.make_tokens()
    return tokens