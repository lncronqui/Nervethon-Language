import decimal
from typing import NamedTuple
from decimal import *
import re


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int
    hasError: str

#MAIN FUNCTION#
def run(lexeme):
    keywords= {'Link.Start', 'Link.End', 'Generate', 'Sys', 'Sys.Call', 'Discharge', 
               'Absorb', 'If', 'Elif', 'Else', 'Switch', 'Execute', 'Default', 'For', 
               'While', 'Exit', 'Continue', 'Avoid', 'Fixed', 'Struct', 'Void', 'Return'}
    
    logical = {'And', 'Or', 'Not'}
    boolean = {'True', 'False'}
    token_specification = [
        ('COMMENT', r'\/\*[\s\S]*\*\/'),
        ('POS_NUMBER', r'(\d+(\.\d+)?)|(\d?(\.\d+)+)'),
        ('NEG_NUMBER', r'(\-\d+(\.\d+)?)|\-(\d?(\.\d+)+)'),
        ('RELATIONAL', r'([<][=]|[>][=]|[!][=]|[<]|[>]|[=][=])'),
        ('ASSIGNMENT', r'\=|(\-\=)|(\+\=)|(\*\=)|(\/\=)|(\*\*\=)|(\%\=)|(\/\/\=)'),
        ('ARITHMETIC', r'\+|\-|(\/\/)|(\*\*)|\*|\/|\%'),
        ('LIT_STRING', r'([\"][\S\s]*[\"])|([\"]?[\S\s]*[\"])|([\"][\S\s]*[\"]?)'),
        ('SYMBOLS', r'\(|\)|\{|\}|\[|\]|\,|\:'),
        ('ESCAPESEQ', r'\\n|\\t|\\"|\\\'|\\\\'),
        ('NON_KEYWORD', r'(l(?i:ink.start)|l(?i:ink.end)|g(?i:enerate)|s(?i:ys)|s(?i:ys.call)|d(?i:ischarge)|a(?i:bsorb)|i(?i:f)|e(?i:lif)|e(?i:lse)|s(?i:witch)|e(?i:xecute)|d(?i:efault)|f(?i:or)|w(?i:hile)|e(?i:xit)|c(?i:ontinue)|a(?i:oid)|f(?i:ixed)|s(?i:truct)|v(?i:oid)|r(?i:eturn)|i(?i:nteger)|b(?i:oolean)|s(?i:tring)|d(?i:ecimal)|a(?i:nd)|o(?i:r)|n(?i:ot)|t(?i:rue)|f(?i:alse))[^\s]?'),
        ('STRUCT_ID', r'[a-z]\w*\.[a-z]\w*'),
        ('ID', r'[a-z]\w*'),
        ('RESERVED_WORD', r'[A-Z][\w\.]*'),
        ('LIT_BOOL', r'[T][r][u][e]|[F][a][l][s][e]'),
        ('TAB', r'[\t]+'),
        ('SPACE', r'[ ]+'),
        ('NEWLINE', r'[\n]+'),
        ('ERROR', r'[^\s]+'),
    ]
    datatype = {'Integer','Boolean','String','Decimal'}
    token_data = []
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, lexeme):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        hasError = ""
        if kind == 'ERROR':
            hasError = "Invalid character/symbol"
        if kind == 'LIT_STRING':
            count_quote = 0
            for i in value:
                   if(i == "\""):
                       count_quote += 1
            if(count_quote != 2):
                kind = 'ERROR'
                hasError = "Invalid number of quotation marks available" 
        elif kind == 'SYMBOLS':
            kind = value
        elif kind == 'ID' and len(value) > 20:
            value_exceed = len(value) - 20
            hasError = "Identifier exceeded maximum values by " + str(value_exceed) + " characters"
            kind = 'ERROR'
        elif kind == 'STRUCT_ID':
            check_structid = str(value).split('.', 1)
            check_id1 = check_structid[0]
            check_id2 = check_structid[1]
            if(len(check_id1) > 20) or (len(check_id2) > 20):
                hasError = True
                kind = 'ERROR'
        elif kind == 'NON_KEYWORD':
            hasError = "Reserved word cannot be used as an identifier"
            kind = 'ERROR'
        elif kind == 'RESERVED_WORD' and value in keywords:
            kind = value
        elif kind == 'RESERVED_WORD' and value in datatype:
            kind = value
        elif kind == 'RESERVED_WORD' and value in logical:
            kind = "LIT_LOGICAL"
        elif kind == 'RESERVED_WORD' and value in boolean:
            kind = "LIT_BOOLEAN"
        elif kind == 'RESERVED_WORD':
            hasError = "The reserved word does not exist"
            kind = 'ERROR'
        elif kind == 'POS_NUMBER':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                if value < 1000000000:
                    kind = "LIT_INTPOS"
                else:
                    hasError = "Exceeded number of digits allowed"
                    kind = 'ERROR'
            else:
                check_decimal = str(value).split('.',1)
                digit_place = str(check_decimal[0])
                decimal_place = str(check_decimal[1])
                if (len(digit_place) < 10) and (len(decimal_place) < 6):
                    kind = "LIT_DECPOS"
                else:
                    hasError = "Exceeded number of digits allowed"
                    kind = 'ERROR'
        elif kind == 'NEG_NUMBER':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                if value < -1000000000:
                    kind = "LIT_INTNEG"
                else:
                    hasError = "Exceeded number of digits allowed"
                    kind = 'ERROR'
            else:
                check_decimal = str(value).split('.',1)
                digit_place = str(check_decimal[0])
                decimal_place = str(check_decimal[1])
                if (len(digit_place) < 11) and (len(decimal_place) < 6):
                    kind = "LIT_DECNEG"
                else:
                    hasError = "Exceeded number of digits allowed"
                    kind = 'ERROR'
        elif kind == 'NEWLINE':
            value = "\\n"
            line_start = mo.end()
            line_num += 1
        elif kind == 'SPACE':
            value = kind
        elif kind == 'TAB':
            value = "\\t"
        #elif kind == 'ERROR':
        #    hasError = True
        if kind == 'ERROR' and value == "":
            continue
        elif kind == 'ERROR' and len(token_data) > 0 and value != "" and not(token_data[-1].value == " " or token_data[-1].value == "\\n" or token_data[-1].value == "\\t"):
            hold_value = str(token_data[-1].value)
            token_data = token_data[:-1]
            value = hold_value + str(value)
        else:
            None
        token_data.append(Token(kind,value,line_num,column,hasError))
        hasError = ""
    return token_data
        
#with open('user_input.txt', 'r') as file_open:
#    user_input = file_open.read()
#run_code = run(user_input) 
#for result in run_code:
#    if result.hasError == False:
#        print(str(result.value) + "\t" + result.type)
#print("Syntax Error:")
#for result in run_code:
#    if result.hasError == True:
#        print("\'" + result.value + "\' at line " + str(result.line))
