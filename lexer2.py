import ply.lex as lex

# reservedwords
reserved_words = {
    'Integer': 'Integer',
    'Decimal': 'Decimal',
    'String': 'String',
    'Boolean': 'Boolean',
    'Struct': 'Struct',
    'Generate': 'Generate',
    'Absorb': 'Absorb',
    'Discharge': 'Discharge',
    'Switch': 'Switch',
    'For': 'For',
    'In': 'In',
    'Sys': 'Sys',
    'Sys.Call': 'Sys_Call',
    'Execute': 'Execute',
    'Fixed': 'Fixed',
    'Return': 'Return',
    'Default': 'Default',
    'Else': 'Else',
    'If': 'If',
    'Elif': 'Elif',
    'Switch': 'Switch',
    'And': 'And',
    'Or': 'Or',
    'Not': 'Not',
    'While': 'While',
    'End.Switch': 'End_Switch',
    'Break': 'Break',
    'Continue': 'Continue',
    'Avoid': 'Avoid',
    'Link.Start' : 'Link_Start',
    'Link.End' : 'Link_End'
}

# list of tokens
tokens = [
    #comment
	'comment',

    #literals
    'lit_decposi',
    'lit_decnega',
    'lit_intposi',
    'lit_intnega',
    'lit_str', 
    'lit_bool',

    #relational
    'less_than_equal',
    'great_than_equal',
    'not_equal',
    'less_than',
    'greater_than',
    'equal_equal',
    
    #assignment
    'equal',
    'minus_equal',
    'plus_equal',
    'times_equal',
    'divide_equal',
    'times_times_equal',
    'modulo_equal',
    'divide_divide_equal',

    #arithemetic
    'plus',
    'minus',
    'divide_divide',
    'times_times',
    'times',
    'divide',
    'modulo',

    #parenthesis and bracket
    'open_par',
    'close_par',
    'open_brace',
    'close_brace',
    'open_bracket',
    'close_bracket',

    #dots nsht
    'comma',
    'colon', 
    'period',
    
    'space',
    'newline',

    #identifier
    'id', 
    'reserved_words',
    'error',
    'error1'
] + list(reserved_words.values())

delimDict = {
    'Integer' : ['space'],
    'Decimal' : ['space'],
    'String' : ['space'],
    'Boolean' : ['space'],
    'Struct' : ['space'],
    'Generate' : ['space'],
    'Absorb' : ['space'],
    'Discharge' : ['space'],
    'Switch' : ['space'],
    'For' : ['space'],
    'In' : ['space'],
    'Sys' : ['space'],
    'Sys.Call' : ['space'],
    'Execute' : ['space'],
    'Fixed' : ['space'],
    'Return' : ['space'],
    'Default' : [':'],
    'Else' : [':'],
    'If' : ['space', '('],
    'Elif' : ['space', '('],
    'And' : ['space', '('],
    'Or' : ['space', '('],
    'Not' : ['space', '('],
    'While' : ['space', '('],
    'End.Switch' : ['newline'],
    'Break' : ['newline'],
    'Continue' : ['newline'],
    'Avoid' : ['newline'],
    'Link_Start' : ['newline'],
    'Link_End' : ['newline', ''],
    'lit_decposi' : ['space', 'newline', '>=', '<=', '!=', 
                     '>', '<', '==', ':', ',', 
                     '+', '-', '//', '**', '*', '/', 
                     '%', ')', ']', '}'],
    'lit_decnega' : ['space', 'newline', '>=', '<=', '!=', 
                     '>', '<', '==', ':', ',', 
                     '+', '-', '//', '**', '*', '/', 
                     '%', ')', ']', '}'],
    'lit_intposi' : ['space', 'newline', '>=', '<=', '!=', 
                     '>', '<', '==', ':', ',', 
                     '+', '-', '//', '**', '*', '/', 
                     '%', ')', ']', '}', ':'],
    'lit_intnega' : ['space', 'newline', '>=', '<=', '!=', 
                     '>', '<', '==', ':', ',', 
                     '+', '-', '//', '**', '*', '/', 
                     '%', ')', ']', '}', ':'],
    'lit_str' : ['id', 'reserved_word', ',', '(', ')', '[', ']', '{', '}', ':'], 
    'lit_bool' : ['id', 'reserved_word', ',', '(', ')', '[', ']', '{', '}'],
    'less_than_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'great_than_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'not_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'less_than' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'greater_than' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'equal_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-', 'lit_str'],
    'minus_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-', 'lit_str'],
    'plus_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-', 'lit_str'],
    'times_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-', 'lit_str'],
    'divide_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-', 'lit_str'],
    'times_times_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-', 'lit_str'],
    'modulo_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-', 'lit_str'],
    'divide_divide_equal' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-', 'lit_str'],
    'plus' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'minus' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'times' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'divide' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'times_times' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'divide_divide' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'modulo' : ['space', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', '(', '-'],
    'open_par' : ['lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', 'And', 'Or', 'Not', '(', ')'],
    'close_par' : ['space', '[', '+', '-', '*', '/', '%', '**', '//', '>', '<', '==', '!=', '>=', '<=', 'And', 'Or', 'Not', ':', ')'],
    'open_brace' : ['id', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', 'lit_str', '}'],
    'close_brace' : ['id', 'reserved_word', ')', '+', '-', '//', '**', '*', '/', '%', '=', '-=', '+=', '*=', '/=', '**=', '%=', '//=', '<=', '>=', '!=', '>', '<', '==', 'And', 'Or', 'Not'],
    'open_bracket' : ['id', 'reserved_word', 'id', '\"', '\“', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega'],
    'close_bracket' : ['space', 'newline', ''],
    'comma' : ['space', 'id', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega'],
    'colon' : ['id', 'reserved_word', '['], 
    'period' : ['id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega'],
    'id' : ['space', 'newline', '.', ',', '(', ')', '[', ']', 
            '+', '-', '//', '**', '*', '/', '%', '=', 
            '-=', '+=', '*=', '/=', '**=', 
            '%=', '//=', '>=', '<=', '!=', 
            '>', '<', '==', ':', '{']
}



t_ignore_comment = r'(\/\*)[\s\S]*?(\*\/)'
t_less_than_equal = r'\<='
t_great_than_equal = r'\>='
t_not_equal = r'\!='
t_less_than = r'\<'
t_greater_than = r'\>'
t_equal_equal = r'=='
t_equal = r'='
t_minus_equal = r'\-='
t_plus_equal = r'\+='
t_times_equal = r'\*='
t_divide_equal = r'\/='
t_times_times_equal = r'\*\*='
t_modulo_equal = r'%='
t_divide_divide_equal = r'\/\/='
t_plus = r'\+'
t_minus = r'-'
t_times = r'\*' 
t_times_times = r'\*\*'
t_divide = r'/'
t_divide_divide = r'//'
t_modulo = r'%'
t_open_par = r'\('
t_close_par = r'\)'
t_open_brace = r'\['
t_close_brace = r'\}'
t_open_bracket = r'\['
t_close_bracket = r'\]'
t_comma = r','
t_colon = r':'
t_period = r'\.'
t_ignore_tab = r' \t'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_id(t):
	r'([a-z]\w{0,19})'
    
	return t

def t_reserved_words(t):
    r'((Integer|Decimal|String|Boolean|Struct|Generate|Absorb|Discharge|Switch|For|In|Sys|Sys\.Call|Execute|Fixed|Return)(?= ))|((Default|Else)(?=\:))|((If|Elif|And|Or|Not|While)(?=[ \(]))|Link\.End(?=\n|$)|(Link\.Start|End\.Switch|Break|Continue|Avoid)(?=\n)'
    t.type = reserved_words.get(t.value, 'error1') #t.value will be error if not within reserved words list
    return t


symbols = {
    #relational
    '<=',
    '>=',
    '!=',
    '<',
    '>',
    '==',
    
    #equal
    '=',

    #assignment
    '-=',
    '+=',
    '*=',
    '/=',
    '**=',
    '%=',
    '//=',

    #arithmetic
    '+',
    '-',
    '//',
    '**',
    '*',
    '/',
    '%',

    #open_par
    '(',

    #close_par
    ')',

    #open_brace
    '{',

    #close_brace
    '}',

    #open_bracket
    '[',

    #close_bracket
    ']',

    #comma
    ',',

    #colon
    ':',

    #period
    '.',

    #extra buusht
    '\n',
    '\t',
    ' '
}



def t_space(t):
    r'[ \t]'
    return t

def t_lit_decposi(t):
	r'(([0-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))'
	return t

def t_lit_decnega(t):
	r'\-(([0-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))'
	return t

def t_lit_intposi(t):
	r'([0-9]\d{0,8})'
	return t

def t_lit_intnega(t):
	r'(\-[1-9]\d{0,8})'
	return t

def t_lit_str(t):
    r'[\"\“]{1}([^\"^\n^\“^\”])*?[\"\”]{1}'
    return t

def t_lit_bool(t):
	r'(True|False)'
	return t

def t_error1(t):
     r'\s'
     t.lexer.skip(1)
     return t
 
    
def t_error(t):
     t.lexer.skip(1)
     return t



lexi = lex.lex()