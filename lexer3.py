import ply.lex as lex
from ply.lex import TOKEN


# list of tokens
tokens = [
    'comment',
    'space',
    'newline',
    
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
    'id',
    
    
    
    #errors
    'error1', #non-keyword
    'error2', #incomplete word
    'error3'
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
t_error1 = r'((e(?i:nd\.switch)|b(?i:reak)|l(?i:ink\.start)|l(?i:ink\.end)|g(?i:enerate)|s(?i:ys\.call)|s(?i:ys)|d(?i:ischarge)|a(?i:bsorb)|i(?i:f)|e(?i:lif)|e(?i:lse)|s(?i:witch)|e(?i:xecute)|d(?i:efault)|f(?i:or)|w(?i:hile)|e(?i:xit)|c(?i:ontinue)|a(?i:void)|f(?i:ixed)|s(?i:truct)|v(?i:oid)|r(?i:eturn)|i(?i:nteger)|b(?i:oolean)|s(?i:tring)|d(?i:ecimal)|a(?i:nd)|o(?i:r)|n(?i:ot)|t(?i:rue)|f(?i:alse)|i(?i:n))(?=[\s]|$))|(E(?i:nd\.switch)|B(?i:reak)|L(?i:ink\.start)|L(?i:ink\.end)|G(?i:enerate)|S(?i:ys\.call)|S(?i:ys)|D(?i:ischarge)|A(?i:bsorb)|I(?i:f)|E(?i:lif)|E(?i:lse)|S(?i:witch)|E(?i:xecute)|D(?i:efault)|F(?i:or)|W(?i:hile)|E(?i:xit)|C(?i:ontinue)|A(?i:void)|F(?i:ixed)|S(?i:truct)|V(?i:oid)|R(?i:eturn)|I(?i:nteger)|B(?i:oolean)|S(?i:tring)|D(?i:ecimal)|A(?i:nd)|O(?i:r)|N(?i:ot)|T(?i:rue)|F(?i:alse)|I(?i:n))'
t_error3 = r'[A-Z][\w](?=\s)'
t_error2 = r'^\s+|\S+'

def t_space(t):
    r'[ \t]'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
     t.lexer.skip(1)
     return t

lexer = lex.lex()

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
    'lit_str' : ['id', 'reserved_word', ',', '(', ')', '[', ']', '{', '}', ':' , 'space' , 'newline'], 
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
    'open_par' : ['lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', 'And', 'Or', 'Not', '(', ')', 'space', 'id', 'Integer', 'String', 'Decimal', 'Boolean'],
    'close_par' : ['space', '[', '+', '-', '*', '/', '%', '**', '//', '>', '<', '==', '!=', '>=', '<=', 'And', 'Or', 'Not', ':', ')', 'newline'],
    'open_brace' : ['id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega', 'lit_str', '}', 'space', 'newline'],
    'close_brace' : ['id', 'reserved_word', ')', '+', '-', '//', '**', '*', '/', '%', '=', '-=', '+=', '*=', '/=', '**=', '%=', '//=', '<=', '>=', '!=', '>', '<', '==', 'And', 'Or', 'Not', 'space', 'newline', ':'],
    'open_bracket' : ['id', 'newline', 'reserved_word', 'id', '\"', '\“', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega'],
    'close_bracket' : ['space', 'newline', ''],
    'comma' : ['space', 'id', 'id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega'],
    'colon' : ['id', 'reserved_word', '[', 'newline'], 
    'period' : ['id', 'lit_decposi', 'lit_decnega', 'lit_intposi', 'lit_intnega'],
    'id' : ['space', 'newline', '.', ',', '(', ')', '[', ']', 
            '+', '-', '//', '**', '*', '/', '%', '=', 
            '-=', '+=', '*=', '/=', '**=', 
            '%=', '//=', '>=', '<=', '!=', 
            '>', '<', '==', ':', '{', '}']
    
}