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
    'Sys.Call': 'Sys.Call',
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
    'End.Switch': 'End.Switch',
    'Break': 'Break',
    'Continue': 'Continue',
    'Avoid': 'Avoid',
}

# list of tokens
tokens = [
    'Link.Start',
    'Link.End',
	'comment',
    'lit_decposi',
    'lit_decnega',
    'lit_intposi',
    'lit_intnega',
    'lit_str', 
    'lit_bool',
    'less_than_equal',
    'great_than_equal',
    'not_equal',
    'less_than',
    'greater_than',
    'equal_equal',
    'equal',
    'minus_equal',
    'plus_equal',
    'times_equal',
    'divide_equal',
    'times_times_equal',
    'modulo_equal',
    'divide_divide_equal',
    'plus',
    'minus',
    'times',
    'divide',
    'modulo',
    'open_par',
    'close_par',
    'open_brace',
    'close_brace',
    'open_bracket',
    'close_bracket',
    'comma',
    'colon', 
    'period',
    'id',
] + list(reserved_words.values())

delimDict = {
    'Andlogical' : ['\n', '(', '\'', '"','STRLit','CHARLit', '~', '+','++','-','--','!','ID', 'INTLit','FLOATLit'],
    'Case' : ['\n', '(', '\'', '~', 'INTLit','CHARLit'],
    'Boolean' : ['\n', 'ID'],
    'Break' : ['\n', '|'],
    'Character' : ['\n','ID'],
    'Continue': ['\n', '|'],
    'Constant': ['\n', 'INT','FLOAT','CHAR','STR','BOOLEAN'],
    'Default': ['\n', ':'],
    'Struct': ['\n', 'ID'],
    'Elsestatement': ['\n', '{'],
    'Elseifstatement': ['\n', '('],
    'BoolFalse' : ['\n', '|', ',', ')', '=', '!=', '!'], 
    'Float': ['\n','ID'],
    'LoopFor': ['\n','('],
    'Ifstatement': ['\n', '('],
    'Input': ['\n', '('],
    'Integer' : ['\n', 'ID'],
    'Null' : ['\n', '|', ',', '=', ')', '!','==','!='],
    'Orlogical': ['\n', '(', '\'', '"','STRLit','CHARLit', '~', '+','++','-','--','!','ID', 'INTLit','FLOATLit'],
    'Output': ['\n', '('],
    'Switchstatement': ['\n', '('],
    'Return' : ['\n', '|', '(', '\'', '"', '~','ID','STRLit','INTLit', 'FLOATLit','CHARLit','TRUE', 'FALSE'],
    'String': ['\n','ID'],
    'BoolTrue': ['\n', '|', ',', '=', ')', '!'],
    'Void': ['\n','ID','+'],
    'LoopWhile': ['\n', '('],
    'MainFunctionBegin': ['\n', '{'], 
    'MainFunctionEnd': ['\n'],
    'NOT': ['\n','(','\'','"','ID','TRUE','FALSE'],
    'NOTEQUALTO': ['\n','(','\'','"','ID','INTLit','FLOATLit','CHARLit','NULL','TRUE','FALSE'],
    'ADD': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'INCREMENT': ['\n', ',', '|', ')','ID'],
    'PLUSASSIGN': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MINUS': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'DECREMENT': ['\n', ',', '|', ')','ID'],
    'MINUSASSIGN': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MULTIPLY': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MULTIPLYASSIGN': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'DIVIDE': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'DIVIDEASSIGN': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MODULO': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MODULOASSIGN': ['\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'GREATERTHAN': ['\n','(','\'','"','ID','INTLit','FLOATLit','~'],
    'GREATEROREQUAL': ['\n','(','\'','"','ID','INTLit','FLOATLit','~'],
    'LESSTHAN': ['\n','(','\'','"','ID','INTLit','FLOATLit','~'],
    'LESSOREQUAL': ['\n','(','\'','"','ID','INTLit','FLOATLit','~'],
    'EQUALS':['\n','(','ID','INTLit','FLOATLit','CHARLit', 'STRLit','NULL','TRUE','FALSE', '~', '\'', '"', '{'],
    'EQUALTO': ['\n','(','\'','"','ID','INTLit','FLOATLit','CHARLit','NULL','TRUE','FALSE','~'],
    'DOT':['ID'],
    'COMMA': ['\n','(','ID','TRUE','FALSE','INT','FLOAT','CHAR','STR','BOOLEAN','STRLit','INTLit', 'FLOATLit','CHARLit','~','\'','"'],
    'LPAREN': ['\n','(','ID','INT','FLOAT','CHAR','STR','BOOLEAN','TRUE','FALSE','STRLit','INTLit', 'FLOATLit','CHARLit','NULL','~','\'','"',')','NOT','+','++','-','--','|','.'],
    'RPAREN':['\n','|',',',')','+','-','/','*','%',']','{', '}',':','>','>=','<','<=','==','=','!','!=','AND','OR'],
    'LBRACKET':['\n','(','ID','INTLit','~','+','-','++','--',']'],
    'RBRACKET':['\n','|',',','AND','OR','>','>=','<','<=','==','=','!','!=','+','-','/','*','%','++','--','[',']',')','}','.'],
    'LCURLY':['\n','(','ID','Integer', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN', 'DOJO',
              'PRINT', 'INPUT', 'IF','ELSEIF','ELSE', 'FOR', 'WHILE', 'BREAK', 'CONTINUE',
              'DEFAULT', 'ARROW', 'QUIVER','RETURN','NULL','TRUE','FALSE','INTLit','FLOATLit',
              'CHARLit','STRLit','\'','"','{','}','~', '+','++','-','--','.'],
    
    'RCURLY' : ['\n', '|', ',', '}' ,'^AIM', '^SHOOT', 'ID', 'INT', 'FLOAT', 'STR', 'CHAR', 
                'BOOLEAN', 'DOJO', 'VOID','PRINT', 'INPUT', 'IF', 'FOR', 'WHILE', 
                'DEFAULT', 'QUIVER', 'BREAK','CONTINUE','CONS','ELSEIF','ELSE','RETURN','+','++','-','--'],
    
    'COLON' : ['\n', 'ID', 'PRINT', 'INPUT', 'IF', 'FOR', 'WHILE', 'BREAK', 'DEFAULT', 'ARROW', 
               'QUIVER', 'INT', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN', 'DOJO','RETURN', '+', '++', '-', '--'],
    
    
    'TERMINATOR' : ['\n', '}', '(', 'ID', '^AIM','PRINT', 'INPUT', 'IF', 'FOR', 'WHILE', 'BREAK', 'DEFAULT',
                    'ARROW', 'QUIVER', 'INT', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN', 'DOJO', 'CONTINUE', 'RETURN', 
                    'TRUE', 'FALSE', 'INTLit', 'FLOATLit','NULL','VOID', '+', '++', '-', '--', '~', '|','.'],
    
    'STRLit' : ['\n', '|', ',',')','}'],
    'CHARLit': ['\n', '|', ',', '>','>=','<','<=','==','=','!','!=','AND','OR',')','}',':'],
    'INTLit':['\n', '|', ',', '>','>=','<','<=','==','=','!','!=','AND','OR',')','}',':',
              '+','-','/','*','%',']'],
    'FLOATLit':['\n', '|', ',', '>','>=','<','<=','==','=','!','!=','AND','OR',')','}',
              '+','-','/','*','%'],
    'ID':['\n', '|', ',', '>','>=','<','<=','==','=','!','!=',')','}', 
              '+','-','/','*','%','++','--','(','[','{',']','.','+=','-=']

    #'SPACE':['SPACE','\n','\t']
}
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
	r'[a-zA-Z][a-zA-Z_0-9]{0,9}'
	#(\[([a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])? | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])? | [0-9]*)?\])?(\.?[a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])? | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])? | [0-9]*)?\]))?'
	t.type = reserved_words.get(t.value, 'ID')  # Check for reserved words
	return t

t_comment = r'(\/\*)[\s\S]*?(\*\/)'

t_MainFunctionBegin = r'\^AIM'
t_MainFunctionEnd = r'\^SHOOT'
t_PLUSASSIGN = r'\+='
t_MINUSASSIGN = r'-='
t_MULTIPLYASSIGN = r'\*='
t_DIVIDEASSIGN = r'/='
t_MODULOASSIGN = r'%='
t_EQUALTO = r'=='
t_NOTEQUALTO = r'!='
t_GREATEROREQUAL = r'\>='
t_LESSOREQUAL = r'\<='
t_ADD = r'\+'
t_MINUS = r'-'
t_NEGATIVE = r'~'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_EQUALS = r'='
t_NOT = r'!'
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_COMMA = r','
t_DQUOTE = r'\"'
t_SQUOTE = r'\''
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_COLON = r':'
t_TERMINATOR = r'\|'
t_DOT = r'\.'
t_ignore = ' \t'

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

    #extraBs
    '\n',
    '\t',
    ' '
}



# def t_SPACE(t):
# 	r'[ \t]+'
# 	return t

def t_FLOATLit(t):
	r'~?[0-9]{0,9}\.[0-9]{1,5}'
	return t

def t_INTLit(t):
	r'~?[0-9]{1,9}'
	return t

def t_CHARLit(t):
	#r'\'([^\\\n]|(\\.))*?\''
    r'\'(.|\n)*?\''
    return t

def t_STRLit(t):
	#r'\"([^\\\n]|(\\.))*?\"'
    r'\"(.|\n)*?\"'
    return t

def t_ignore_COMMENT(t):
	r'@\$(.|\n)*?\$@'
	#return t
    

def t_error(t):
     #print('Lexical Error: Invalid delim for "{}" token'.format(t.value[0]))
     t.lexer.skip(1)
     return t
 

lexi = lex.lex()

# data = '''
# INT A =5|
# ^AIM{INT A =5|}^SHOOT INT A =5|
# '''

# lexer.input(data)
# lexerrors=[]
# toks=[]
# previousToken=' '
# previousValue=' '
# for tok in lexer:
#     if(tok.type != 'SPACE'):
#         print(tok.type, ": ", tok.value)
#     try:
#         listVal = delimDict[previousToken]
        
#         if((tok.value not in listVal and tok.type not in listVal) or tok.type=='error'):         
#             lexerrors.append('Lexical Error: Invalid lexem for \'{}\' '.format(previousValue))
#         previousToken = tok.type
#         previousValue = tok.value
#         toks.append(tok)
        
#     except:
#         previousToken = tok.type
#         previousValue = tok.value
#         toks.append(tok)
# if(lexerrors):
#     for i in lexerrors:
#         print(i)
# else:
#     print("No error")