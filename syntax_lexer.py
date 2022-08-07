import ply.lex as lex
from ply.lex import TOKEN


# list of tokens
tokens = [
    'comment',
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
    'Sys_Call',
    'Sys',
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

def t_Integer(t):
    r'Integer'
    return t
def t_Decimal(t):
    r'Decimal'
    return t
def t_String(t):
    r'String'
    return t
def t_Boolean(t):
    r'Boolean'
    return t
def t_Struct(t):
    r'Struct'
    return t
def t_Generate(t):
    r'Generate'
    return t
def t_Absorb(t):
    r'Absorb'
    return t
def t_Discharge(t):
    r'Discharge'
    return t
def t_Switch(t):
    r'Switch'
    return t
def t_For(t):
    r'For'
    return t
def t_In(t):
    r'In'
    return t
def t_Sys_Call(t):
    r'Sys\.Call'
    return t
def t_Sys(t):
    r'Sys'
    return t
def t_Execute(t):
    r'Execute'
    return t
def t_Fixed(t):
    r'Fixed'
    return t
def t_Return(t):
    r'Return'
    return t
def t_Default(t):
    r'Default'
    return t
def t_Else(t):
    r'Else'
    return t
def t_If(t):
    r'If'
    return t
def t_Elif(t):
    r'Elif'
    return t
def t_And(t):
    r'And'
    return t
def t_Or(t):
    r'Or'
    return t
def t_Not(t):
    r'Not'
    return t
def t_While(t):
    r'While'
    return t
def t_Link_End(t):
    r'Link\.End'
    return t
def t_Link_Start(t):
    r'Link\.Start'
    return t
def t_End_Switch(t):
    r'End\.Switch'
    return t
def t_Break(t):
    r'Break'
    return t
def t_Continue(t):
    r'Continue'
    return t
def t_Avoid(t):
    r'Avoid'
    return t

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
def t_lit_str(t):
    r'[\"\“]{1}(([^\"^\n^\“^\”])*)?[\"\”]{1}'
    return t

def t_lit_bool(t): 
    r'(True|False)'
    return t

#relational
def t_less_than_equal(t):
    r'\<\='
    return t
def t_great_than_equal(t):
    r'\>\='
    return t
def t_not_equal(t):
    r'\!\='
    return t
def t_less_than(t):
    r'\<'
    return t
def t_greater_than(t):
    r'\>'
    return t
def t_equal_equal(t):
    r'\=\='
    return t


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
def t_equal(t):
    r'[=]'
    return t

#arithmetic
def t_plus(t):
    r'\+'
    return t
def t_minus(t):
    r'\-'
    return t
def t_times_times(t):
    r'\*\*'
    return t
def t_times(t):
    r'\*' 
    return t
def t_divide_divide(t):
    r'\/\/'
    return t
def t_divide(t):
    r'\/'
    return t
def t_modulo(t):
    r'\%'
    return t

def t_open_par(t):
    r'\('
    return t
def t_close_par(t):
    r'\)'
    return t
def t_open_brace(t):
    r'\{'
    return t
def t_close_brace(t):
    r'\}'
    return t
def t_open_bracket(t):
    r'\['
    return t
def t_close_bracket(t):
    r'\]'
    return t

def t_comma(t):
    r'\,'
    return t
def t_colon(t):
    r'\:'
    return t
def t_period(t):
    r'\.'
    return t
    
t_id = r'([a-z]\w{0,19})'

def t_space(t):
    r'[ \t]'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_error(t):
     t.lexer.skip(1)

lexer_syntax = lex.lex()