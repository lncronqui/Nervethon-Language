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
    'ID',
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
    
    'SPACE',

    #identifier
    'id', 
    'reserved_words',
    'error'
] + list(reserved_words.values())

delimDict = {
    'Integer' : [' '],
    'Decimal' : [' '],
    'String' : [' '],
    'Boolean' : [' '],
    'Struct' : [' '],
    'Generate' : [' '],
    'Absorb' : [' '],
    'Discharge' : [' '],
    'Switch' : [' '],
    'For' : [' '],
    'In' : [' '],
    'Sys' : [' '],
    'Sys.Call' : [' '],
    'Execute' : [' '],
    'Fixed' : [' '],
    'Return' : [' '],
    'Default' : ['\:'],
    'Else' : ['colon'],
    'If' : [' ', 'open_par'],
    'Elif' : [' ', 'open_par'],
    'And' : [' ', 'open_par'],
    'Or' : [' ', 'open_par'],
    'Not' : [' ', 'open_par'],
    'While' : [' ', 'open_par'],
    'End.Switch' : ['\n'],
    'Break' : ['\n'],
    'Continue' : ['\n'],
    'Avoid' : ['\n'],
    'Link.Start' : ['\n'],
    'Link.End' : ['\n', '$'],
	'comment' : ['\s', '\S', '$'],
    'lit_decposi' : [' ', '\n', 'great_than_equal', 'less_than_equal', 'not_equal', 
                     'greater_than', 'less_than', 'equal_equal', 'colon', 'comma', 
                     'plus', 'minus', 'divide_divide', 'times_times', 'times', 'divide', 
                     'modulo', 'close_par', 'close_bracket', 'close_brace'],
    'lit_decnega' : [' ', '\n', 'great_than_equal', 'less_than_equal', 'not_equal', 
                     'greater_than', 'less_than', 'equal_equal', 'colon', 'comma', 
                     'plus', 'minus', 'divide_divide', 'times_times', 'times', 'divide', 
                     'modulo', 'close_par', 'close_bracket', 'close_brace'],
    'lit_intposi' : [' ', '\n', 'great_than_equal', 'less_than_equal', 'not_equal', 
                     'greater_than', 'less_than', 'equal_equal', 'colon', 'comma', 
                     'plus', 'minus', 'divide_divide', 'times_times', 'times', 'divide', 
                     'modulo', 'close_par', 'close_bracket', 'close_brace', 'colon'],
    'lit_intnega' : [' ', '\n', 'great_than_equal', 'less_than_equal', 'not_equal', 
                     'greater_than', 'less_than', 'equal_equal', 'colon', 'comma', 
                     'plus', 'minus', 'divide_divide', 'times_times', 'times', 'divide', 
                     'modulo', 'close_par', 'close_bracket', 'close_brace', 'colon'],
    'lit_str' : ['\s', 'comma', 'open_par', 'close_par', 'open_bracket', 'close_bracket', 'open_brace', 'close_brace', 'colon'], 
    'lit_bool' : ['\s', 'comma', 'open_par', 'close_par', 'open_bracket', 'close_bracket', 'open_brace', 'close_brace'],
    'less_than_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'great_than_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'not_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'less_than' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'greater_than' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'equal_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus', 'lit_str'],
    'minus_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus', 'lit_str'],
    'plus_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus', 'lit_str'],
    'times_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus', 'lit_str'],
    'divide_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus', 'lit_str'],
    'times_times_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus', 'lit_str'],
    'modulo_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus', 'lit_str'],
    'divide_divide_equal' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus', 'lit_str'],
    'plus' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'minus' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'times' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'divide' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'times_times' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'divide_divide' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'modulo' : [' ', '[a-z]', '[0-9]', 'open_par', 'minus'],
    'open_par' : ['\d', 'And', 'Or', 'Not', 'open_par', 'close_par'],
    'close_par' : [' ', 'open_bracket', 'plus', 'minus', 'times', 'divide', 'modulo', 'times_times', 'divide_divide', 'greater_than', 'less_than', 'equal_equal', 'not_equal', 'great_equal', 'less_equal', 'And', 'Or', 'Not', 'colon', 'close_par'],
    'open_brace' : ['id', '[A-Z]', '\d', 'lit_str', 'close_brace'],
    'close_brace' : ['\s', 'close_par', 'plus', 'minus', 'divide_divide', 'times_times', 'times', 'divide', 'modulo', 'equal', 'minus_equal', 'plus_equal', 'times_equal', 'divide_equal', 'times_times_equal', 'modulo_equal', 'divide_divide_equal', 'less_equal', 'great_equal', 'not_equal', 'greater_than', 'less_than', 'equal_equal', 'And', 'Or', 'Not'],
    'open_bracket' : ['\s', 'id', '\"', '\“', '\d'],
    'close_bracket' : [' ', '\n', '$'],
    'comma' : [' ', 'id', '[A-Z]', '\d'],
    'colon' : ['\s', 'open_bracket'], 
    'period' : ['id', '\d'],
    'id' : ['\s', 'period', 'comma', 'open_par', 'close_par', 'open_bracket', 'close_bracket', 
            'plus', 'minus', 'divide_divide', 'times_times', 'times', 'divide', 'modulo', 'equal', 
            'minus_equal', 'plus_equal', 'times_equal', 'divide_equal', 'times_times_equal', 
            'modulo_equal', 'divide_divide_equal', 'great_equal', 'less_equal', 'not_equal', 
            'greater_than', 'less_than', 'equal_equal', 'colon', 'open_brace']
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

def t_ID(t):
	r'([a-z]\w{0,19})'
	return t

def t_reserved_words(t):
    r'([A-Z][\w\.]{0,19})'
    t.type = reserved_words.get(t.value, 'error') #t.value will be error if not within reserved words list
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



def t_SPACE(t):
    r'[ \t]+'
    #return t --> no need to output space???

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
    
def t_error(t):
     t.lexer.skip(1)
     return t
 

lexi = lex.lex()