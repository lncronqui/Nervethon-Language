import decimal
from typing import NamedTuple
from decimal import *
import re


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int
    hasError: bool

#MAIN FUNCTION#
def run(lexeme):
    keywords= {'Link.Start', 'Link.End', 'Generate', 'Sys', 'Sys.Call', 'Discharge', 
               'Absorb', 'If', 'Elif', 'Else', 'Switch', 'Execute', 'Default', 'For', 
               'While', 'Exit', 'Continue', 'Avoid', 'Fixed', 'Struct', 'Void', 'Return'}
    datatype = {'Integer','Boolean','String','Decimal'}
    logical = {'And', 'Or', 'Not'}
    boolean = {'True', 'False'}
    token_specification = [
        ('COMMENT', r'\/\*[\s\S]*\*\/'),
        ('POS_NUMBER', r'(\d+(\.\d+)?)|(\d?(\.\d+)+)'),
        ('NEG_NUMBER', r'(\-\d+(\.\d+)?)|\-(\d?(\.\d+)+)'),
        ('RELATIONAL', r'([<][=]|[>][=]|[!][=]|[<]|[>]|[=][=])'),
        ('ASSIGNMENT', r'\=|(\-\=)|(\+\=)|(\*\=)|(\/\=)|(\*\*\=)|(\%\=)|(\/\/\=)'),
        ('ARITHMETIC', r'\+|\-|(\/\/)|(\*\*)|\*|\/|\%'),
        ('SYMBOLS', r'\(|\)|\{|\}|\[|\]|\,|\:'),
        ('ESCAPESEQ', r'\\n|\\t|\\"|\\\'|\\\\'),
        ('NON_KEYWORD', r'(l(?i:ink.start)|l(?i:ink.end)|g(?i:enerate)|s(?i:ys)|s(?i:ys.call)|d(?i:ischarge)|a(?i:bsorb)|i(?i:f)|e(?i:lif)|e(?i:lse)|s(?i:witch)|e(?i:xecute)|d(?i:efault)|f(?i:or)|w(?i:hile)|e(?i:xit)|c(?i:ontinue)|a(?i:oid)|f(?i:ixed)|s(?i:truct)|v(?i:oid)|r(?i:eturn)|i(?i:nteger)|b(?i:oolean)|s(?i:tring)|d(?i:ecimal)|a(?i:nd)|o(?i:r)|n(?i:ot)|t(?i:rue)|f(?i:alse))'),
        ('STRUCT_ID', r'[a-z]\w*\.[a-z]\w*'),
        ('ID', r'[a-z]\w*'),
        ('RESERVED_WORD', r'[A-Z][\w\.]*'),
        ('LIT_STRING', r'(\"[\S\s]*\")|(\“.*\”)'),
        ('LIT_BOOL', r'[T][r][u][e]|[F][a][l][s][e]'),
        ('SKIP', r'[\t]+'),
        ('SPACE', r'[ ]+'),
        ('NEWLINE', r'[\n]+'),
        ('ERROR', r'.*'),
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, lexeme):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        hasError = False
        if kind == 'SYMBOLS':
            kind = value
        elif kind == 'ID' and len(value) > 20:
            hasError = True
            kind = 'ERROR'
        elif kind == 'STRUCT_ID':
            check_structid = str(value).split('.', 1)
            check_id1 = check_structid[0]
            check_id2 = check_structid[1]
            if(len(check_id1) > 20) or (len(check_id2) > 20):
                hasError = True
                kind = 'ERROR'
        elif kind == 'NON_KEYWORD':
            hasError = True
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
            hasError = True
            kind = 'ERROR'
        elif kind == 'POS_NUMBER':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                if value < 1000000000:
                    kind = "LIT_INTPOS"
                else:
                    hasError = True
                    kind = 'ERROR'
            else:
                check_decimal = str(value).split('.',1)
                digit_place = str(check_decimal[0])
                decimal_place = str(check_decimal[1])
                if (len(digit_place) < 10) and (len(decimal_place) < 6):
                    kind = "LIT_DECPOS"
                else:
                    hasError = True
                    kind = 'ERROR'
        elif kind == 'NEG_NUMBER':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                if value < 1000000000:
                    kind = "LIT_INTNEG"
                else:
                    hasError = True
                    kind = 'ERROR'
            else:
                check_decimal = str(value).split('.',1)
                digit_place = str(check_decimal[0])
                decimal_place = str(check_decimal[1])
                if (len(digit_place) < 11) and (len(decimal_place) < 6):
                    kind = "LIT_DECNEG"
                else:
                    hasError = True
                    kind = 'ERROR'
        elif kind == 'NEWLINE':
            value = "\\n"
            line_start = mo.end()
            line_num += 1
        elif kind == 'SPACE':
            value = kind
        elif kind == 'SKIP':
            value = "\\t"
        elif kind == 'ERROR':
            hasError = True
        yield Token(kind, value, line_num, column, hasError)