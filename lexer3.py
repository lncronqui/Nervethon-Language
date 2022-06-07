import ply.lex as lex
from ply.lex import TOKEN


# list of tokens
tokens = [
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
    'id',
    
    #errors
    'error1', #non-keyword
    'error2' #incomplete word
]

t_Integer = r'Integer(?= )'
t_Decimal = r'Decimal(?= )'
t_String = r'String(?= )'
t_Boolean = r'Boolean(?= )'
t_Struct = r'Struct(?= )'
t_Generate = r'Generate(?= )'
t_Absorb = r'Absorb(?= )'
t_Discharge = r'Discharge(?= )'
t_Switch = r'Switch(?= )'
t_For = r'For(?= )'
t_In = r'In(?= )'
t_Sys = r'Sys(?= )'
t_Sys_Call = r'Sys_Call(?= )'
t_Execute = r'Execute(?= )'
t_Fixed = r'Fixed(?= )'
t_Return = r'Return(?= )'


t_Default = r'Default(?=\:)'
t_Else = r'Else(?=\:)'


t_If = r'If(?=[ \(])'
t_Elif = r'Elif(?=[ \(])'
t_And = r'And(?=[ \(])'
t_Or = r'Or(?=[ \(])'
t_Not = r'Not(?=[ \(])'
t_While = r'While(?=[ \(])'


t_Link_End = r'Link\.End(?=\n|$)'


t_Link_Start = r'Link\.Start(?=\n)'
t_End_Switch = r'End\.Switch(?=\n)'
t_Break = r'Break(?=\n)'
t_Continue = r'Continue(?=\n)'
t_Avoid = r'Avoid(?=\n)'


def t_lit_decposi(t):
    r'(([0-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\})'
    t.value = float(t.value)
    return t
def t_lit_decnega(t):
    r'\-(([0-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\})'
    t.value = float(t.value)
    return t
def t_lit_intposi(t):
    r'([0-9]\d{0,8})(?=[\s\,\(\)\[\]\{\}]|\<\=|\>\=|\!\=|\<|\>|\=\=|\+|\-|(\/\/)|(\*\*)|\*|\/|\%)'
    t.value = int(t.value)
    return t
def t_lit_intnega(t):
    r'(\-[1-9]\d{0,8})(?=[\s\,\(\)\[\]\{\}]|\<\=|\>\=|\!\=|\<|\>|\=\=|\+|\-|(\/\/)|(\*\*)|\*|\/|\%)'
    t.value = int(t.value)
    return t
t_lit_str = r'[\"\“]{1}([^\"^\n^\“^\”])*?[\"\”]{1}(?=[\s\,\(\)\[\]\{\}\:])'
t_lit_bool = r'(True|False)(?=[\s\,\(\)\[\]\{\}])'



#relational
t_less_than_equal = r'\<\=(?= |[a-z]|[0-9]|\()'
t_great_than_equal = r'\>\=(?= |[a-z]|[0-9]|\()'
t_not_equal = r'\!\=(?= |[a-z]|[0-9]|\()'
t_less_than = r'\<(?= |[a-z]|[0-9]|\()'
t_greater_than = r'\>(?= |[a-z]|[0-9]|\()'
t_equal_equal = r'\=\=(?= |[a-z]|[0-9]|\()'


#assignment
def t_minus_equal(t):
    r'\-\=(?= |[a-z]|[0-9]|\()'
    return t
def t_plus_equal(t):
    r'\+\=(?= |[a-z]|[0-9]|\()'
    return t
def t_times_equal(t):
    r'\*\=(?= |[a-z]|[0-9]|\()'
    return t
def t_divide_equal(t):
    r'\/\=(?= |[a-z]|[0-9]|\()'
    return t
def t_times_times_equal(t):
    r'\*\*\=(?= |[a-z]|[0-9]|\()'
    return t
def t_modulo_equal(t):
    r'\%\=(?= |[a-z]|[0-9]|\()'
    return t
def t_divide_divide_equal(t):
    r'\/\/\=(?= |[a-z]|[0-9]|\()'
    return t
def t_equal(t):
    r'\=(?= |[a-z]|[0-9]|\(|\"|\“)'
    return t

#arithmetic
def t_plus(t):
    r'\+(?= |[a-z]|[0-9]|\()'
    return t
def t_minus(t):
    r'\-(?= |[a-z]|[0-9]|\()'
    return t
def t_times(t):
    r'\*(?= |[a-z]|[0-9]|\()' 
    return t
def t_times_times(t):
    r'\*\*(?= |[a-z]|[0-9]|\()'
    return t
def t_divide(t):
    r'\/(?= |[a-z]|[0-9]|\()'
    return t
def t_divide_divide(t):
    r'\/\/(?= |[a-z]|[0-9]|\()'
    return t
def t_modulo(t):
    r'\%(?= |[a-z]|[0-9]|\()'
    return t


t_open_par = r'\((?=[a-zANOISDB0-9\(\)])'
t_close_par = r'\)(?=And|Or|Not|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\<\=|\>\=|\!\=|\<|\>|\=\=|[\s\:\[\)])'
t_open_brace = r'\{(?=[a-zA-Z\d\"|\“|\}])'
t_close_brace = r'\}(?=[\s\)]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=|And|Or|Not)'
t_open_bracket = r'\[(?=[\sa-z\"\“\d])'
t_close_bracket =  r'\](?= |\n|$)'


t_comma = r'\,(?=[ A-Za-z0-9])'
t_colon = r'\:(?=[\s\[])'
t_period =  r'\.(?=[a-zA-Z\d])'

t_id = r'([a-z]\w{0,19})(?=[\s\.\,\(\)\[\]]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\{)'

t_error1 = r'(e(?i:nd\.switch)|b(?i:reak)|l(?i:ink\.start)|l(?i:ink\.end)|g(?i:enerate)|s(?i:ys\.call)|s(?i:ys)|d(?i:ischarge)|a(?i:bsorb)|i(?i:f)|e(?i:lif)|e(?i:lse)|s(?i:witch)|e(?i:xecute)|d(?i:efault)|f(?i:or)|w(?i:hile)|e(?i:xit)|c(?i:ontinue)|a(?i:void)|f(?i:ixed)|s(?i:truct)|v(?i:oid)|r(?i:eturn)|i(?i:nteger)|b(?i:oolean)|s(?i:tring)|d(?i:ecimal)|a(?i:nd)|o(?i:r)|n(?i:ot)|t(?i:rue)|f(?i:alse)|i(?i:n))(?=[\s\.\,\(\)\[\]\{\}]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=)'

t_ignore = r'[ \t]+|(\/\*)[\s\S]*?(\*\/)'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
     t.lexer.skip(1)
     return t

lexer = lex.lex()