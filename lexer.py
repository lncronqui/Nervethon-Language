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
    token_specification = [
        ('comment', r'(\/\*)[\s\S]*?(\*\/)'),
        ('lit_decposi', r'([1-9]\d{0,8}\.\d{0,5})(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\}|$)'),
        ('lit_decnega', r'(\-[1-9]\d{0,8}\.\d{0,5})(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\}|$)'),
        ('lit_intposi', r'([1-9]\d{0,8})(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\}|$)'),
        ('lit_intnega', r'(\-[1-9]\d{0,8})(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\}|$)'),
        ('lit_str', r'([\"\“]([ \S]*?)[\"\”])(?= |\n|\:|\,|\)|\]|\}|$)'),
        ('lit_bool', r'(True|False)(?= |\n|\:|\,|\)|\]|\}|$)'),
        ('relational', r'(\<\=|\>\=|\!\=|\<|\>|\=\=)(?= |[a-z]|[0-9]|\()'),
        ('assignment', r'(\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=)(?= |[a-z]|[0-9]|\(|\")'),
        ('arithmetic', r'(\+|\-|(\/\/)|(\*\*)|\*|\/|\%)(?= |[a-z]|[0-9]|\()'),
        ('open_par', r'\((?= |[A-Za-z]|\)|\")'),
        ('close_par', r'\)(?= |\n|\[|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\<\=|\>\=|\!\=|\<|\>|\=\=|And|Or|Not|\:|\))'),
        ('open_brace',r'\{(?= |[a-z]|[0-9]|\})'),
        ('close_brace',r'\}(?= |\n|And|Or|Not|\:|\)|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\<\=|\>\=|\!\=|\<|\>|\=\=)'),
        ('open_bracket', r'\[(?=[ \nA-Z])'),
        ('close_bracket', r'\](?=\n)'),
        ('comma', r'\,(?= |[a-z])'),
        ('colon', r'\:(?= |\n|\[)'),
        ('period', r'\.(?=[a-z])'),
        ('keyword', r'((Absorb|Boolean|Decimal|Discharge|Execute|Fixed|For|Generate|Integer|Return|Struct|String|Switch|Sys|Sys.Call|While)(?= ))|((Avoid|Break|Continue|End.Switch|Link.Start)(?=[ \n]))|((Default|Else)(?=\:))|((If|Elif|And|Or|Not)(?=[ \(]))|Link.End(?=\n|$)'),
        ('non_keyword', r'(e(?i:nd\.switch)$|b(?i:reak)$|l(?i:ink\.start)$|l(?i:ink\.end)$|g(?i:enerate)$|s(?i:ys\.call)$|s(?i:ys)$|d(?i:ischarge)$|a(?i:bsorb)$|i(?i:f)$|e(?i:lif)$|e(?i:lse)$|s(?i:witch)$|e(?i:xecute)$|d(?i:efault)$|f(?i:or)$|w(?i:hile)$|e(?i:xit)$|c(?i:ontinue)$|a(?i:void)$|f(?i:ixed)$|s(?i:truct)$|v(?i:oid)$|r(?i:eturn)$|i(?i:nteger)$|b(?i:oolean)$|s(?i:tring)$|d(?i:ecimal)$|a(?i:nd)$|o(?i:r)$|n(?i:ot)$|t(?i:rue)$|f(?i:alse)$|i(?i:n)$)'),
        ('newline', r'\n'),
        ('tab_space', r'[ \t]'),
        ('id', r'([a-z]\w{0,19})(?= |\n|\:|\,|\.|\(|\{|\[|\)|\}|\]|\<\=|\>\=|\!\=|\<|\>|\=\=|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|$)'),
        ('error', r'[^\s]+'),
    ]
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
            if str(value)[0] == "\"":
                hasError = "String literal lacks close quotation mark"
            elif str(value)[-1] == "\"":
                hasError = "String literal lacks open quotation mark"
            else:
                hasError = "Invalid character/delimiter"
            token_data.append(Token(kind,value,line_num,column,hasError))
            break
        if kind == 'relational' or kind == 'arithmetic' or kind == 'assignment' or kind == 'open_par' or kind == 'close_par' or kind == 'open_brace' or kind == 'close_brace' or kind == 'open_bracket' or kind == 'close_bracket' or kind == 'comma' or kind == 'colon' or kind == 'period' or kind == 'keyword':
            kind = value
        elif kind == 'non_keyword':
            hasError = "Reserved word cannot be used as an identifier"
            kind = 'error'
        elif kind == 'lit_intposi' or kind == 'lit_intnega':
            value = int(value)
        elif kind == 'lit_decposi' or kind == 'lit_decnega':
            value = float(value)
        elif kind == 'newline':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'tab_space':
            continue
        token_data.append(Token(kind,value,line_num,column,hasError))
        hasError = ""
    return token_data
