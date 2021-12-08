#######################################
# CONSTANTS
#######################################

LOWERCASE   = 'abcdefghijklmnopqrstuvwxyz' 
UPPERCASE   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS     = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NONZERO     = '123456789'
NUMBERS     = '0123456789'
ASCII       = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

#######################################
# TOKENS
#######################################

#RESERVED WORDS#
TT_START        = 'Link.Start'
TT_END          = 'Link.End'
TT_GENERATE     = 'Generate'
TT_SYS          = 'Sys'
TT_SYSCALL      = 'Sys.Call'
TT_DISCHARGE    = 'Discharge'
TT_ABSORB		    = 'Absorb'
TT_BOOLEAN		  = 'Boolean'
TT_INTEGER		  = 'Integer'
TT_DECIMAL		  = 'Decimal'
TT_STRING		    = 'String'
TT_IF		        = 'If'
TT_ELIF		      = 'Elif'
TT_ELSE		      = 'Else'
TT_SWITCH		    = 'Switch'
TT_EXECUTE		  = 'Execute'
TT_DEFAULT		  = 'Default'
TT_FOR		      = 'For'
TT_DO		        = 'Do'
TT_WHILE		    = 'While'
TT_EXIT		      = 'Exit'
TT_CONTINUE		  = 'Continue'
TT_AVOID		    = 'Avoid'
TT_FIXED		    = 'Fixed'
TT_STRUCT		    = 'Struct'
TT_VOID		      = 'Void'
TT_RETURN		    = 'Return'
TT_TRUE		      = 'True'
TT_FALSE		    = 'False'

#UNARY OPERATORS#
TT_UNARY1		    = '+'
TT_UNARY2       = '-'

#ARITHMETIC OPERATORS#
TT_ARITHOP1     = '*'
TT_ARITHOP2     = '/'
TT_ARITHOP3     = '%'
TT_AIRTHOP4     = '**'
TT_ARITHOP5     = '//'

#RELATIONAL OPERATORS#
TT_RELATEOP1    = '<'
TT_RELATEOP2    = '>'
TT_RELATEOP3    = '=='
TT_RELATEOP4    = '!'
TT_RELATEOP5    = '!='
TT_RELATEOP6    = '>='
TT_RELATEOP7    = '<='

#ASSIGNMENT OPERATORS#
TT_ASSIGNOP1    = '='
TT_ASSIGNOP2    = '+='
TT_ASSIGNOP3    = '-='
TT_ASSIGNOP4    = '*='
TT_ASSIGNOP5    = '/='
TT_ASSIGNOP6    = '//='
TT_ASSIGNOP7    = '%='
TT_ASSIGNOP8    = '**='

#LOGICAL OPERATORS#
TT_LOGICALOP1   = 'And'
TT_LOGICALOP2   = 'Or'
TT_LOGICALOP3   = 'Not'

#OPEN SYMBOLS#
TT_OPENSYM1     = '('
TT_OPENSYM2     = '{'
TT_OPENSYM3     = '['
TT_OPENSYM4     = '"'

#CLOSE SYMBOLS#
TT_CLOSESYM1    = ')'
TT_CLOSESYM2    = '}'
TT_CLOSESYM3    = ']'
TT_CLOSESYM4    = '"'

#COMMENT SYMBOLS#
TT_COMMENT1     = '/*'
TT_COMMENT2     = '*/'

#ESCAPE SEQUENCES SYMBOLS#
TT_ESCAPESEQ1   = '\n'
TT_ESCAPESEQ2   = '\t'
TT_ESCAPESEQ3   = '\"'
TT_ESCAPESEQ4   = '\''
TT_ESCAPESEQ5   = '\\'

#OTHER SYMBOLS#
TT_COLON        = ':'
TT_PERIOD       = '.'
TT_SEMICOLON    = ';'
TT_COMMA        = ','
TT_SPACE        = 'Space'

#IDENTIFIERS#
TT_IDENTIFIER   = 'id'

#LITERALS#
TT_INTPOSI      = 'lit_intposi'
TT_INTNEGA      = 'lit_intnega'   
TT_DECPOSI      = 'lit_decposi'
TT_DECNEGA      = 'lit_decnega'
TT_STRING       = 'lit_str'
TT_BOOLEAN      = 'lit_bool'
