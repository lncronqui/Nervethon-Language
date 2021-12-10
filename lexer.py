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
    keywords= {'Link.Start', 'Link.End', 'Generate', 'Sys', 'Sys.Call', 'Discharge', 'Absorb', 'If', 'Elif', 'Else', 'Switch', 'Execute', 'Default', 'For', 'While', 'Exit', 'Continue', 'Avoid', 'Fixed', 'Struct', 'Void', 'Return'}
    datatype = {'Integer','Boolean','String','Decimal'}
    logical = {'And', 'Or', 'Not'}
    boolean = {'True', 'False'}
    token_specification = [
        ('COMMENT', r'\/\*.*\*\/'),
        ('POS_NUMBER', r'(\d+(\.\d+)?)|(\d?(\.\d+)+)'),
        ('NEG_NUMBER', r'(\-\d+(\.\d+)?)|\-(\d?(\.\d+)+)'),
        ('RELATIONAL', r'([<][=]|[>][=]|[!][=]|[<]|[>]|[=][=])'),
        ('ASSIGNMENT', r'\=|(\-\=)|(\+\=)|(\*\=)|(\/\=)|(\*\*\=)|(\%\=)|(\/\/\=)'),
        ('ARITHMETIC', r'\+|\-|(\/\/)|(\*\*)|\*|\/|\%'),
        ('SYMBOLS', r'\(|\)|\{|\}|\[|\]|\,|\.'),
        #('ESCAPESEQ', r'[\n] | [\t] | [\"] | [\'] | [\\]'),
        ('ID', r'[a-z]\w*'),
        ('RESERVED_WORD', r'[A-Z][\w\.]*'),
        ('LIT_STRING', r'(\".*\")|(\“.*\”)'),
        ('LIT_BOOL', r'[T][r][u][e]|[F][a][l][s][e]'),
        ('SKIP', r'[\t]+'),
        ('SPACE', r'[ ]+'),
        ('NEWLINE', r'[\n]+'),
        ('MISMATCH', r'.*'),
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
        elif kind == 'POS_NUMBER':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                if value < 1000000000:
                    kind = "LIT_INTPOS"
                else:
                    hasError = True
            else:
                check_decimal = str(value).split('.',1)
                digit_place = str(check_decimal[0])
                decimal_place = str(check_decimal[1])
                if (len(digit_place) < 10) and (len(decimal_place) < 6):
                    kind = "LIT_DECPOS"
                else:
                    hasError = True
        elif kind == 'NEG_NUMBER':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                if value < 1000000000:
                    kind = "LIT_INTNEG"
                else:
                    hasError = True
            else:
                check_decimal = str(value).split('.',1)
                digit_place = str(check_decimal[0])
                decimal_place = str(check_decimal[1])
                if (len(digit_place) < 11) and (len(decimal_place) < 6):
                    kind = "LIT_DECNEG"
                else:
                    hasError = True
        elif kind == 'NEWLINE':
            value = "\\n"
            line_start = mo.end()
            line_num += 1
        elif kind == 'SPACE':
            value = kind
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            hasError = True
        yield Token(kind, value, line_num, column, hasError)