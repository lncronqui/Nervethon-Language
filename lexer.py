from typing import NamedTuple
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
    token_specification = [
        ('POS_NUMBER', r'\d+(\.\d{1,6})?'),
        ('NEG_NUMBER', r'\-\d+(\.\d{1,6})?'),
        ('RELATIONAL', r'([<][=]|[>][=]|[!][=]|[<]|[>]|[=][=])'),
        ('ASSIGNMENT', r'\=|(\-\=)|(\+\=)|(\*\=)|(\/\=)|(\*\*\=)|(\%\=)|(\/\/\=)'),
        ('ARITHMETIC', r'\+|\-|(\/\/)|(\*\*)|\*|\/|\%'),
        ('LOGICAL', r'[A][n][d]|[O][r]|[N][o][t]'),
        ('SYMBOLS', r'[(] | [)] | [{] | [}] | [[] | []] | ["] | ["]'),
        ('COMMENT', r'[/][\*]|[\*][/]'),
        ('ESCAPESEQ', r'[\n] | [\t] | [\"] | [\'] | [\\]'),
        ('ID', r'[a-z]\w{0,19}'),
        ('RESERVED_WORD', r'[A-Z][\w\.]*'),
        #('LIT_INTPOS', r'[\d]{1,9}'),
        #('LIT_INTNEG', r'^\-[1-9][\d]{0,8}$'),
        #('LIT_DECPOS', r'^[\d]{1,9}\.[0-9]{1,6}$'),
        #('LIT_DECNEG', r'^\-[\d]{1,9}\.[0-9]{1,6}$'),
        #('LIT_POS', r'\d{1,9}+(\.\d){1,6}'),
        #('LIT_NEG', r'\-\d{1,9}+(\.\d){1,6}'),
        ('LIT_STRING', r'\"[a-zA-Z]\"'),
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
        elif kind == 'COMMENTS':
            kind = value
        elif kind == 'RESERVED_WORD' and value in keywords:
            kind = value
        elif kind == 'RESERVED_WORD' and value in datatype:
            kind = value
        elif kind == 'RESERVED_WORD':
            hasError = True
        elif kind == 'POS_NUMBER':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                kind = "LIT_INTPOS"
            else:
                kind = "LIT_DECPOS"
        elif kind == 'NEG_NUMBER':
            value = float(value) if '.' in value else int(value)
            if (isinstance(value, int) == True):
                kind = "LIT_INTNEG"
            else:
                kind = "LIT_DECNEG"
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
            value = "\n"
            line_start = mo.end()
            line_num += 1
            #continue
        elif kind == 'SPACE':
            value = kind
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            #raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            hasError = True
        yield Token(kind, value, line_num, column, hasError)
        
with open('user_input.txt', 'r') as file:
    user_input = file.read()

for result in run(user_input):
    if result.hasError == False:
        print(result)

print("Syntax Error:")
for result in run(user_input):
    if result.hasError == True:
        if result.value != "":
            print(result)