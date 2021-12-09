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
    logical = {'And', 'Or', 'Not'} 
    token_specification = [
        ('COMMENT', r'\/\*.*\*\/'),
        ('POS_NUMBER', r'(\d+(\.\d{1,6})?)|(\d?(\.\d{1,6})+)'),
        ('NEG_NUMBER', r'(\-\d+(\.\d{1,6})?)|\-(\d?(\.\d{1,6})+)'),
        ('RELATIONAL', r'([<][=]|[>][=]|[!][=]|[<]|[>]|[=][=])'),
        ('ASSIGNMENT', r'\=|(\-\=)|(\+\=)|(\*\=)|(\/\=)|(\*\*\=)|(\%\=)|(\/\/\=)'),
        ('ARITHMETIC', r'\+|\-|(\/\/)|(\*\*)|\*|\/|\%'),
        ('SYMBOLS', r'[(] | [)] | [{] | [}] | [[] | []] | ["] | ["]'),
        ('ESCAPESEQ', r'[\n] | [\t] | [\"] | [\'] | [\\]'),
        ('ID', r'[a-z]\w{0,19}'),
        ('RESERVED_WORD', r'[A-Z][\w\.]*'),
        ('LIT_STRING', r'\".*\"'),
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
        elif kind == 'RESERVED_WORD' and value in keywords:
            kind = value
        elif kind == 'RESERVED_WORD' and value in datatype:
            kind = value
        elif kind == 'RESERVED_WORD' and value in logical:
            kind = "LIT_LOGICAL"
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
        elif kind == 'NEWLINE':
            value = "\n"
            line_start = mo.end()
            line_num += 1
        elif kind == 'SPACE':
            value = kind
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
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