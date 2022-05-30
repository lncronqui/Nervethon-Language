import ply.lex as lex

# reservedwords
reserved = {
	'INT': 'Integer',
	'STR': 'String',
	'CHAR': 'Character',
	'FLOAT': 'Float',
	'BOOLEAN': 'Boolean',
	'CONS': 'Constant',
	'DOJO': 'Struct',
	'PRINT': 'Output',
	'INPUT': 'Input',
	'IF': 'Ifstatement',
	'ELSEIF': 'Elseifstatement',
	'ELSE': 'Elsestatement',
	'QUIVER': 'Switchstatement',
	'ARROW': 'Case',
	'BREAK': 'Break',
	'DEFAULT': 'Default',
	'CONTINUE': 'Continue',
	'FOR': 'LoopFor',
	'WHILE': 'LoopWhile',
	'TRUE': 'BoolTrue',
	'FALSE': 'BoolFalse',
	'AND': 'Andlogical',
	'OR': 'Orlogical',
	'NULL': 'Null',
	'VOID': 'Void',
	'RETURN': 'Return'
}

# list of tokens
tokens = [
	'MainFunctionBegin',
	'MainFunctionEnd',
	'ID',
	'ADD',
	'MINUS',
	'NEGATIVE',
	'MULTIPLY',
	'DIVIDE',
	'MODULO',
	'EQUALTO',
	'EQUALS',
	'PLUSASSIGN',
	'MINUSASSIGN',
	'MULTIPLYASSIGN',
	'DIVIDEASSIGN',
	'MODULOASSIGN',
	'NOT',
	'NOTEQUALTO',
	'GREATERTHAN',
	'LESSTHAN',
	'GREATEROREQUAL',
	'LESSOREQUAL',
	'INCREMENT',
	'DECREMENT',
	'COMMA',
	#'DQUOTE',
	#'SQUOTE',
	'LPAREN',
	'RPAREN',
	'LBRACKET',
	'RBRACKET',
	'LCURLY',
	'RCURLY',
	'COLON',
	'TERMINATOR',
	'INTLit',
	'FLOATLit',
	'CHARLit',
	'STRLit',
	'DOT',
	'COMMENT',
    'SPACE'
	#'String',
	#'Integer',
	#'Float',
	#'Character',
	#'Boolean',
] + list(reserved.values())

delimDict = {
    'Andlogical' : ['SPACE', '\n', '(', '\'', '"','STRLit','CHARLit', '~', '+','++','-','--','!','+=','-='],
    'Case' : ['SPACE', '\n', '(', '\'', '~'],
    'Boolean' : ['SPACE', '\n'],
    'Break' : ['SPACE', '\n', '|'],
    'Character' : ['SPACE', '\n'],
    'Continue': ['SPACE', '\n', '|'],
    'Constant': ['SPACE', '\n'],
    'Default': ['SPACE', '\n', ':'],
    'Struct': ['SPACE', '\n'],
    'Elsestatement': ['SPACE', '\n', '{'],
    'Elseifstatement': ['SPACE', '\n', '('],
    'BoolFalse' : ['SPACE', '\n', '|', ',', ')', '=', '!=', '!'], 
    'Float': ['SPACE', '\n'],
    'LoopFor': ['SPACE', '\n','('],
    'Ifstatement': ['SPACE', '\n', '('],
    'Input': ['SPACE', '\n', '('],
    'Integer' : ['SPACE', '\n'],
    'Null' : ['SPACE', '\n', '|', ',', '=', ')', '!','==','!='],
    'Orlogical': ['SPACE', '\n', '(', '\'', '"','STRLit','CHARLit', '~', '+','++','-','--','!','+=','-='],
    'Output': ['SPACE', '\n', '('],
    'Switchstatement': ['SPACE', '\n', '('],
    'Return' : ['SPACE', '\n', '|', '(', '\'', '"', '~'],
    'String': ['SPACE', '\n'],
    'BoolTrue': ['SPACE', '\n', '|', ',', '=', ')', '!'],
    'Void': ['SPACE', '\n', '-'],
    'LoopWhile': ['SPACE', '\n', '('],
    'MainFunctionBegin': ['SPACE', '\n', '{'], 
    'MainFunctionEnd': ['SPACE', '\n'],
    'NOT': ['SPACE', '\n','(','\'','"','ID','TRUE','FALSE'],
    'NOTEQUALTO': ['SPACE', '\n','(','\'','"','ID','INTLit','FLOATLit','CHARLit','NULL','TRUE','FALSE'],
    'ADD': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'INCREMENT': ['SPACE', '\n', ',', '|', ')','ID'],
    'PLUSASSIGN': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MINUS': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'DECREMENT': ['SPACE', '\n', ',', '|', ')','ID'],
    'MINUSASSIGN': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MULTIPLY': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MULTIPLYASSIGN': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'DIVIDE': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'DIVIDEASSIGN': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MODULO': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'MODULOASSIGN': ['SPACE', '\n', '(', 'ID', 'INTLit', 'FLOATLit','~'],
    'GREATERTHAN': ['SPACE', '\n','(','\'','"','ID','INTLit','FLOATLit','~'],
    'GREATEROREQUAL': ['SPACE', '\n','(','\'','"','ID','INTLit','FLOATLit','~'],
    'LESSTHAN': ['SPACE', '\n','(','\'','"','ID','INTLit','FLOATLit','~'],
    'LESSOREQUAL': ['SPACE', '\n','(','\'','"','ID','INTLit','FLOATLit','~'],
    'EQUALS':['SPACE', '\n','(','ID','INTLit','FLOATLit','CHARLit', 'STRLit','NULL','TRUE','FALSE', '~', '\'', '"', '{'],
    'EQUALTO': ['SPACE', '\n','(','\'','"','ID','INTLit','FLOATLit','CHARLit','NULL','TRUE','FALSE','~'],
    'DOT':['ID'],
    'COMMA': ['SPACE', '\n','(','ID','TRUE','FALSE','INT','FLOAT','CHAR','STR','BOOLEAN','STRLit','INTLit', 'FLOATLit','CHARLit','~','\'','"'],
    'LPAREN': ['SPACE', '\n','(','ID','INT','FLOAT','CHAR','STR','BOOLEAN','TRUE','FALSE','STRLit','INTLit', 'FLOATLit','CHARLit','NULL','~','\'','"',')','NOT','+','++','-','--','|','.'],
    'RPAREN':['SPACE', '\n','|',',',')','+','-','/','*','%',']','{', '}',':','>','>=','<','<=','==','=','!','!=','AND','OR','+=','+=','-=','--','*=','%=','/='],
    'LBRACKET':['SPACE', '\n','(','ID','INTLit','~','+','-','++','--',']'],
    'RBRACKET':['SPACE', '\n','|',',','AND','OR','>','>=','<','<=','==','=','!','!=','+','-','/','*','%','++','--','[',']',')','}','.','+=','-=','*=','/=','%='],
    'LCURLY':['SPACE', '\n','(','ID','INT', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN', 'DOJO',
              'PRINT', 'INPUT', 'IF','ELSEIF','ELSE', 'FOR', 'WHILE', 'BREAK', 'CONTINUE',
              'DEFAULT', 'ARROW', 'QUIVER','RETURN','NULL','TRUE','FALSE','INTLit','FLOATLit',
              'CHARLit','STRLit','\'','"','{','}','~', '+','++','-','--','.','+=','-='],
    
    'RCURLY' : ['SPACE', '\n', '|', ',', '}' ,'^AIM', '^SHOOT', 'ID', 'INT', 'FLOAT', 'STR', 'CHAR', 
                'BOOLEAN', 'DOJO', 'VOID','PRINT', 'INPUT', 'IF', 'FOR', 'WHILE', 
                'DEFAULT', 'QUIVER', 'BREAK','CONTINUE','CONS','ELSEIF','ELSE','RETURN','+','++','-','--','+=','-='],
    
    'COLON' : ['SPACE', '\n', 'ID', 'PRINT', 'INPUT', 'IF', 'FOR', 'WHILE', 'BREAK', 'DEFAULT', 'ARROW', 
               'QUIVER', 'INT', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN', 'DOJO','RETURN', '+', '++', '-', '--','+=','-='],
    
    
    'TERMINATOR' : ['SPACE', '\n', '}', '(', ')', 'ID', '^AIM','PRINT', 'INPUT', 'IF', 'FOR', 'WHILE', 'BREAK', 'DEFAULT',
                    'ARROW', 'QUIVER', 'INT', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN', 'DOJO', 'CONTINUE', 'RETURN', 
                    'TRUE', 'FALSE', 'INTLit', 'FLOATLit','NULL','VOID', '+', '++', '-', '--', '~', '|','.','+=','-='],
    
    'STRLit' : ['SPACE', '\n', '|', ',',')','}'],
    'CHARLit': ['SPACE', '\n', '|', ',', '>','>=','<','<=','==','=','!','!=','AND','OR',')','}',':'],
    'INTLit':['SPACE', '\n', '|', ',', '>','>=','<','<=','==','=','!','!=','AND','OR',')','}',':',
              '+','-','/','*','%',']','++','--','+=','-=','/=','*=','%='],
    'FLOATLit':['SPACE', '\n', '|', ',', '>','>=','<','<=','==','=','!','!=','AND','OR',')','}',
              '+','-','/','*','%''++','--','+=','-=','/=','*=','%='],
    'ID':['SPACE', '\n', '|', ',', '>','>=','<','<=','==','=','!','!=',')','}', 
              '+','-','/','*','%','++','--','(','[','{',']','.','++','--','+=','-=','/=','*=','%=']
    #'SPACE':['SPACE','\n','\t']
}
# Define a rule so we can track line numbers
# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

def t_ID(t):
	r'[a-zA-Z][a-zA-Z_0-9]{0,9}'
	#(\[([a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])? | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])? | [0-9]*)?\])?(\.?[a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])? | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]*(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])?(\[([a-zA-Z][a-zA-Z_0-9]* | [0-9]*)?\])? | [0-9]*)?\]))?'
	t.type = reserved.get(t.value, 'ID')  # Check for reserved words
	return t

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
#t_DQUOTE = r'\"'
#t_SQUOTE = r'\''
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_COLON = r':'
t_TERMINATOR = r'\|'
t_DOT = r'\.'

symbols = {
    '+=',
    '-=',
    '*=',
    '=',
    '%=',
    '==',
    '!=',
    '>=',
    '<=',
    '+',
    '-',
    '~',
    '*',
    '/',
    '%',
    '=',
    '!',
    '>',
    '<',
    '++',
    '--',
    ',',
    '"',
    '\'',
    '(',
    ')',
    '[',
    ']',
    '{',
    '}',
    ':',
    '|',
    '.',
    '\n',
    '\t',
    ' ',
    '^'
    
        
}

# def t_eof(t):
#     return None

def t_SPACE(t):
	r'[ \t\n]'
	return t

def t_FLOATLit(t):
	r'~?[0-9]{0,9}\.[0-9]{1,5}'
	return t

def t_INTLit(t):
	r'~?[0-9]{1,9}'
	return t

def t_CHARLit(t):
	#r'\'([^\\\n]|(\\.))*?\''
    r'\'(.|\n)?\'' 
    return t

def t_STRLit(t):
	#r'\"([^\\\n]|(\\.))*?\"'
    r'\"(.|\n)*?\"'
    return t

def t_ignore_COMMENT(t):
	r'@(.|\n)*?@'
	#return t

def t_error(t):
     #print('Lexical Error: Invalid delim for "{}" token'.format(t.value[0]))
     t.lexer.skip(1)
     return t

lexer = lex.lex()
# data = '''
# INT A = 5+- |
# $#
# '''
# lexer.input(data)
# lexerrors=[]
# toks=[]
# previousToken=' '
# previousValue=' '
# for tok in lexer:
#       if(tok.type != 'SPACE'):
#           print(tok.type, ": ", tok.value)
#       try:
#           listVal = delimDict[previousToken]
     
#           if((tok.value not in listVal and tok.type not in listVal) or tok.type=='error'):         
#               lexerrors.append('Lexical Error: Invalid lexeme for \'{}\' '.format(previousValue))
#           previousToken = tok.type
#           previousValue = tok.value
#           toks.append(tok)
#           if(tok.type == 'error'):
#               print(tok.value)
              
#       except:
#           previousToken = tok.type
#           previousValue = tok.value
#           toks.append(tok)
# if(lexerrors):
#       for i in lexerrors:
#           print(i)
# else:
#       print("No error")
      
      