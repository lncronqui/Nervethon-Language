from typing import NamedTuple
import re


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

#MAIN FUNCTION#
def run(lexeme):
    keywords= {'Link.Start', 'Link.End', 'Generate', 'Sys', 'Sys.Call', 'Discharge', 'Absorb', 'If', 'Elif', 'Else', 'Switch', 'Execute', 'Default', 'For', 'While', 'Exit', 'Continue', 'Avoid', 'Fixed', 'Struct', 'Void', 'Return'}
    datatype = {'Integer','Boolean','String','Decimal'} 
    token_specification = [
        ('ARITHMETIC', r'([+]|[\-]|[\*]|[/]|[%]|[\*][\*]|[/][/])'),
        ('RELATIONAL', r'([<]|[>]|[=][=]|[!][=]|[>][=]|[<][=])'),
        ('ASSIGNMENT', r'([=]|[\+][=]|[\-][=]|[][=]|[/][=]|[/][/][=]|[%][=]|[\*][\*][=])'),
        ('LOGICAL', r'[A][n][d]|[O][r]|[N][o][t]'),
        ('SYMBOLS', r'[(] | [)] | [{] | [}] | [[] | []] | ["] | ["]'),
        ('COMMENT', r'[/][\*]|[\*][/]'),
        ('ESCAPESEQ', r'[\n] | [\t] | [\"] | [\'] | [\\]'),
        ('ID', r'[a-z]\w{0,19}'),
        ('RESERVED_WORD', r'[A-Z][\w\.]*'),
        ('NUMBER', r'\d+(\.\d{1,6})?'),
        #('LIT_INTPOS', r'[\d]{1,9}'),
        #('LIT_INTNEG', r'^\-[1-9][\d]{0,8}$'),
        #('LIT_DECPOS', r'^[\d]{1,9}\.[0-9]{1,6}$'),
        #('LIT_DECNEG', r'^\-[\d]{1,9}\.[0-9]{1,6}$'),
        #('LIT_POS', r'\d{1,9}+(\.\d){1,6}'),
        #('LIT_NEG', r'\-\d{1,9}+(\.\d){1,6}'),
        ('LIT_STRING', r'\"[a-zA-Z]\"'),
        ('LIT_BOOL', r'[T][r][u][e]|[F][a][l][s][e]'),
        ('SPACE', r'[ ]+'),
        ('SKIP', r'[\t]+'),
        ('NEWLINE', r'\n'),
        ('MISMATCH', r'.'),
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, lexeme):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        #if --> arithmetic, relational, assignment, logical, symbols, comments, id, literals
        if kind == 'ARITHMETIC':
            kind = value
        elif kind == 'RELATIONAL':
            kind = value
        elif kind == 'ASSIGNMENT':
            kind = value
        elif kind == 'LOGICAL':
            kind = value
        elif kind == 'SYMBOLS':
            kind = value
        elif kind == 'COMMENTS':
            kind = value
        elif kind == 'ID':
            kind = value
        elif kind == 'RESERVED_WORD' and value in keywords:
            kind = value
        elif kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        #elif kind == 'LIT_INTPOS':
        #    value = int(value)
        #elif kind == 'LIT_INTNEG':
        #    value = int(value)
        #elif kind == 'LIT_DECPOS':
        #    value = float(value) if '.' in value else int(value)
        #elif kind == 'LIT_DECNEG':
        #    value = float(value) if '.' in value else int(value)
        #elif kind == 'LIT_POSI':
        #    value = float(value) if '.' in value else int(value)
        #elif kind == 'LIT_NEGA':
        #    value = float(value) if '.' in value else int(value)
        elif kind == 'LIT_STRING':
            kind = value
        elif kind == 'LIT_BOOL':
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)
        
with open('user_input.txt', 'r') as file:
    user_input = file.read()

for result in run(user_input):
    print(result)
