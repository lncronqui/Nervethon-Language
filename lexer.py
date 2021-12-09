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
        ('ARITHMETIC', r'[+]|[\-]|[\*]|[/]|[%]|[\*][\*]|[/][/]'),
        ('RELATIONAL', r'[<]|[>]|[=][=]|[!][=]|[>][=]|[<][=]'),
        ('ASSIGNMENT', r'[=]|[\+][=]|[\-][=]|[][=]|[/][=]|[/][/][=]|[%][=]|[\*][\*][=]'),
        ('LOGICAL', r'[A][n][d]|[O][r]|[N][o][t]'),
        ('SYMBOLS', r'[(] | [)] | [{] | [}] | [[] | []] | ["] | ["]'),
        ('COMMENT', r'[/][\*]|[\*][/]'),
        ('ESCAPESEQ', r'[\n] | [\t] | [\"] | [\'] | [\\]'),
        ('ID', r'[a-z]\w{0,19}'),
        ('LIT_INTPOSI', r'[1-9][\d]{0,8}'),
        ('LIT_INTNEGA', r'-[1-9][\d]{0,8}'),
        ('LIT_DECPOSI', r'[0-9]{1,9}.[0-9]{1,6}'),
        ('LIT_DECNEGA', r'-[0-9]{1,9}.[0-9]{1,6}'),
        ('LIT_STRING', r'[a-zA-Z]'),
        ('LIT_BOOL', r'[T][r][u][e]|[F][a][l][s][e]'),
        ('SPACE', r'[ ]+'),
        ('SKIP', r'[\t]+'),
        ('NEWLINE', r'\n'),
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for x in re.finditer(tok_regex, code):
        kind = x.lastgroup
        value = x.group()
        column = x.start() - line_start
        #if --> arithmetic, relational, assignment, logical, symbols, comments, id, literals