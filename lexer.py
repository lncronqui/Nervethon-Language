import re




class Token:
    def __init__(token, type_, value):
        token.type = type_
        token.value = value
        
    def __repr__(token):
        if token.value:
            return f'token.type\t-\ttoken.value'
        return f'token.type'
    
class Lexer:
    def __init__(user_input, text):
        user_input.text = text
        user_input.pos = -1
        user_input.current_char = None
        user_input.advance()
        
    def advance(user_input):
        user_input.pos += 1
        user_input.current_char = user_input.text[pos] if user_input.pos < len(user_input.text) else None
        