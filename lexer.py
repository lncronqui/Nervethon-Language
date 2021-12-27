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
               'While', 'Exit', 'Continue', 'Avoid', 'Fixed', 'Struct', 'Void', 'Return', 'Break',
                'End.Switch', 'In'}

    logical = {'And', 'Or', 'Not'}
    boolean = {'True', 'False'}
    token_specification = [
        ('comment', r'(\/\*)[\s\S]*?(\*\/)'),
        ('pos_number', r'(\d+(\.\d*)?)|(\d?(\.\d+)+)'),
        ('neg_number', r'(\-\d+(\.\d+)?)|\-(\d?(\.\d+)+)'),
        ('relational', r'([<][=]|[>][=]|[!][=]|[<]|[>]|[=][=])'),
        ('assignment', r'\=|(\-\=)|(\+\=)|(\*\=)|(\/\=)|(\*\*\=)|(\%\=)|(\/\/\=)'),
        ('arithmetic', r'\+|\-|(\/\/)|(\*\*)|\*|\/|\%'),
        ('lit_str', r'[\"\“]([ \n\S]*?)[\"\”]'),
        ('symbols', r'\(|\)|\{|\}|\[|\]|\,|\:|\.'),
        ('non_keyword', r'(e(?i:nd\.switch)$|b(?i:reak)$|l(?i:ink\.start)$|l(?i:ink\.end)$|g(?i:enerate)$|s(?i:ys\.call)$|s(?i:ys)$|d(?i:ischarge)$|a(?i:bsorb)$|i(?i:f)$|e(?i:lif)$|e(?i:lse)$|s(?i:witch)$|e(?i:xecute)$|d(?i:efault)$|f(?i:or)$|w(?i:hile)$|e(?i:xit)$|c(?i:ontinue)$|a(?i:void)$|f(?i:ixed)$|s(?i:truct)$|v(?i:oid)$|r(?i:eturn)$|i(?i:nteger)$|b(?i:oolean)$|s(?i:tring)$|d(?i:ecimal)$|a(?i:nd)$|o(?i:r)$|n(?i:ot)$|t(?i:rue)$|f(?i:alse)$|i(?i:n)$)'),
        ('struct_id', r'[a-z]\w*\.[a-z]\w*'),
        ('id', r'[a-z]\w*'),
        ('reserved_word', r'[A-Z][\w\.]*'),
        ('lit_bool', r'[T][r][u][e]|[F][a][l][s][e]'),
        ('tab', r'[\t]+'),
        ('space', r'[ ]+'),
        ('newline', r'[\n]+'),
        ('error', r'[^\s]+'),
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
        if kind == 'error':
            if str(value)[0] == "\"" or str(value)[-1] == "\"":
                hasError = "Lacking open/close quotation mark"
            else:
                hasError = "Invalid character/symbol"
        if kind == 'lit_str':
            if re.search(r'\n', value):
                kind = 'error'
                hasError = "Multi-line string"
        elif kind == 'symbols':
            kind = value
        elif kind == 'relational':
            kind = value
        elif kind == 'assignment':
            kind = value
        elif kind == 'arithmetic':
            kind = value
        elif kind == 'id' and len(value) > 20:
            value_exceed = len(value) - 20
            hasError = "Identifier exceeded maximum values by " + str(value_exceed) + " characters"
            kind = 'error'
        elif kind == 'struct_id':
            check_structid = str(value).split('.', 1)
            check_id1 = check_structid[0]
            check_id2 = check_structid[1]
            if(len(check_id1) > 20) or (len(check_id2) > 20):
                hasError = True
                kind = 'error'
        elif kind == 'non_keyword':
            hasError = "Reserved word cannot be used as an identifier"
            kind = 'error'
        elif kind == 'reserved_word' and value in keywords:
            kind = value
        elif kind == 'reserved_word' and value in datatype:
            kind = value
        elif kind == 'reserved_word' and value in logical:
            kind = "lit_logical"
        elif kind == 'reserved_word' and value in boolean:
            kind = "lit_bool"
        elif kind == 'reserved_word':
            hasError = "The reserved word does not exist"
            kind = 'error'
        elif kind == 'pos_number':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                if value < 1000000000:
                    kind = "lit_intposi"
                else:
                    hasError = "Exceeded number of digits allowed"
                    kind = 'error'
            else:
                check_decimal = str(value).split('.',1)
                digit_place = str(check_decimal[0])
                decimal_place = str(check_decimal[1])
                if (len(digit_place) < 10) and (len(decimal_place) < 6):
                    kind = "lit_decposi"
                else:
                    hasError = "Exceeded number of digits allowed"
                    kind = 'error'
        elif kind == 'neg_number':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                if value > -1000000000:
                    kind = "lit_intnega"
                else:
                    hasError = "Exceeded number of digits allowed"
                    kind = 'error'
            else:
                check_decimal = str(value).split('.',1)
                digit_place = str(check_decimal[0])
                decimal_place = str(check_decimal[1])
                if (len(digit_place) < 11) and (len(decimal_place) < 6):
                    kind = "lit_decnega"
                else:
                    hasError = "Exceeded number of digits allowed"
                    kind = 'error'
        elif kind == 'newline':
            value = "\\n"
            line_start = mo.end()
            line_num += 1
        elif kind == 'space':
            value = kind
        elif kind == 'tab':
            value = "\\t"
        if kind == 'error' and value == "":
            continue
        elif kind == 'error' and len(token_data) > 0:
            if (token_data[-1].type != 'space' and token_data[-1].value != "\\n" and token_data[-1].value != "\\t"):
                hold_value = str(token_data[-1].value)
                token_data = token_data[:-1]
                value = hold_value + str(value)
                print("hello")
            else:
                print("hi")
        if(kind == 'error'):
            token_data.append(Token(kind,value,line_num,column,hasError))
            break
        token_data.append(Token(kind,value,line_num,column,hasError))
        hasError = ""
    return token_data
