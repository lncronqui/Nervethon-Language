import ply.lex as lex
from ply.lex import TOKEN


# list of tokens
tokens = [
    'comment',
    'space',
    
    #(?= )
    'Integer',
    'Decimal',
    'String',
    'Boolean',
    'Struct',
    'Generate',
    'Absorb',
    'Discharge',
    'Switch',
    'For',
    'In',
    'Sys',
    'Sys_Call',
    'Execute',
    'Fixed',
    'Return',
    
    #(?=\:)
    'Default',
    'Else',
    
    #(?=[ (])
    'If',
    'Elif',
    'And',
    'Or',
    'Not',
    'While',
    
    #(?=\n|$)
    'Link_End',
    
    #(?=\n)
    'Link_Start',
    'End_Switch',
    'Break',
    'Continue',
    'Avoid',
    
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
    
    'minus_equal',
    'plus_equal',
    'times_equal',
    'divide_equal',
    'times_times_equal',
    'modulo_equal',
    'divide_divide_equal',
    'equal',

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

    #dots
    'comma',
    'colon', 
    'period',
    
    #identifier
    'id'
]

def t_ignore_comment(t):
    r'(\/\*)[\s\S]*?(\*\/)'

t_Integer = r'Integer'
t_Decimal = r'Decimal'
t_String = r'String'
t_Boolean = r'Boolean'
t_Struct = r'Struct'
t_Generate = r'Generate'
t_Absorb = r'Absorb'
t_Discharge = r'Discharge'
t_Switch = r'Switch'
t_For = r'For'
t_In = r'In'
t_Sys = r'Sys'
t_Sys_Call = r'Sys_Call'
t_Execute = r'Execute'
t_Fixed = r'Fixed'
t_Return = r'Return'


t_Default = r'Default'
t_Else = r'Else'


t_If = r'If'
t_Elif = r'Elif'
t_And = r'And'
t_Or = r'Or'
t_Not = r'Not'
t_While = r'While'


t_Link_End = r'Link\.End'


t_Link_Start = r'Link\.Start'
t_End_Switch = r'End\.Switch'
t_Break = r'Break'
t_Continue = r'Continue'
t_Avoid = r'Avoid'


def t_lit_decposi(t):
    r'(([0-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))'
    t.value = float(t.value)
    return t
def t_lit_decnega(t):
    r'\-(([0-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))'
    t.value = float(t.value)
    return t
def t_lit_intposi(t):
    r'([0-9]\d{0,8})'
    t.value = int(t.value)
    return t
def t_lit_intnega(t):
    r'(\-[1-9]\d{0,8})'
    t.value = int(t.value)
    return t
t_lit_str = r'[\"\“]{1}(([^\"^\n^\“^\”])*)?[\"\”]{1}'
t_lit_bool = r'(True|False)'



#relational
t_less_than_equal = r'\<\='
t_great_than_equal = r'\>\='
t_not_equal = r'\!\='
t_less_than = r'\<'
t_greater_than = r'\>'
t_equal_equal = r'\=\='


#assignment
def t_minus_equal(t):
    r'\-\='
    return t
def t_plus_equal(t):
    r'\+\='
    return t
def t_times_equal(t):
    r'\*\='
    return t
def t_divide_equal(t):
    r'\/\='
    return t
def t_times_times_equal(t):
    r'\*\*\='
    return t
def t_modulo_equal(t):
    r'\%\='
    return t
def t_divide_divide_equal(t):
    r'\/\/\='
    return t
t_equal = r'\='

#arithmetic
def t_plus(t):
    r'\+'
    return t
def t_minus(t):
    r'\-'
    return t
def t_times(t):
    r'\*' 
    return t
def t_times_times(t):
    r'\*\*'
    return t
def t_divide(t):
    r'\/'
    return t
def t_divide_divide(t):
    r'\/\/'
    return t
def t_modulo(t):
    r'\%'
    return t


t_open_par = r'\('
t_close_par = r'\)'
t_open_brace = r'\{'
t_close_brace = r'\}'
t_open_bracket = r'\['
t_close_bracket =  r'\]'


t_comma = r'\,'
t_colon = r'\:'
t_period =  r'\.'

t_id = r'([a-z]\w{0,19})'



def t_ignore_space(t):
    r'[ \t]'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)


def t_error(t):
     t.lexer.skip(1)
     return t

lexer_syntax = lex.lex()