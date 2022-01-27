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
        ('comment', r'(\/\*)[\s\S]*?(\*\/)(?=\s|\S|$)'),
        ('array', r'[a-z]\w{0,19}\{[0-9]+\}(?=[\s\.\,\(\)\[\]\{\}]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=)'),
        ('lit_decposi', r'(([1-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\})'),
        ('lit_decnega', r'\-(([1-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\})'),
        ('lit_intposi', r'([1-9]\d{0,8})(?=[\s\,\(\)\[\]\{\}]|\<\=|\>\=|\!\=|\<|\>|\=\=|\+|\-|(\/\/)|(\*\*)|\*|\/|\%)'),
        ('lit_intnega', r'(\-[1-9]\d{0,8})(?=[\s\,\(\)\[\]\{\}]|\<\=|\>\=|\!\=|\<|\>|\=\=|\+|\-|(\/\/)|(\*\*)|\*|\/|\%)'),
        ('lit_str', r'[\"\“]([^\"][ \S]*[^\"])?[\"\”](?=[\s\,\(\)\[\]\{\}])'),
        ('lit_bool', r'(True|False)(?=[\s\,\(\)\[\]\{\}])'),
        ('relational', r'(\<\=|\>\=|\!\=|\<|\>|\=\=)(?= |[a-z]|[0-9]|\()'),
        ('equal', r'\=(?= |[a-z]|[0-9]|\(|\")'),
        ('assignment', r'(\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=)(?= |[a-z]|[0-9]|\()'),
        ('arithmetic', r'(\+|\-|(\/\/)|(\*\*)|\*|\/|\%)(?= |[a-z]|[0-9]|\()'),
        ('open_par', r'\((?=[ANO0-9\(\)])'),
        ('close_par', r'\)(?=And|Or|Not|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\<\=|\>\=|\!\=|\<|\>|\=\=|[\s\:\[\)])'),
        ('open_brace',r'\{(?=[a-zA-Z\d\"])'),
        ('close_brace',r'\}(?=[\s\)]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=|And|Or|Not)'),
        ('open_bracket', r'\[(?=[\sa-z\"\d])'),
        ('close_bracket', r'\](?=\n|$)'),
        ('comma', r'\,(?=[ A-Za-z])'),
        ('colon', r'\:(?=[\s\[])'),
        ('period', r'\.(?=[a-zA-Z\d])'),
        ('keyword', r'((Integer|Decimal|String|Boolean|Struct|Generate|Absorb|Discharge|Switch|For|In|Sys|Sys.Call|Execute|Fixed|Return)(?= ))|((Default|Else)(?=\:))|((If|Elif|And|Or|Not|While)(?=[ \(]))|Link.End(?=\n|$)|(Link.Start|End.Switch|Break|Continue|Avoid)(?=\n)'),
        ('non_keyword', r'(e(?i:nd\.switch)|b(?i:reak)|l(?i:ink\.start)|l(?i:ink\.end)|g(?i:enerate)|s(?i:ys\.call)|s(?i:ys)|d(?i:ischarge)|a(?i:bsorb)|i(?i:f)|e(?i:lif)|e(?i:lse)|s(?i:witch)|e(?i:xecute)|d(?i:efault)|f(?i:or)|w(?i:hile)|e(?i:xit)|c(?i:ontinue)|a(?i:void)|f(?i:ixed)|s(?i:truct)|v(?i:oid)|r(?i:eturn)|i(?i:nteger)|b(?i:oolean)|s(?i:tring)|d(?i:ecimal)|a(?i:nd)|o(?i:r)|n(?i:ot)|t(?i:rue)|f(?i:alse)|i(?i:n))(?=[\s\.\,\(\)\[\]\{\}]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=)'),
        ('newline', r'\n'),
        ('tab_space', r'[ \t]'),
        ('id', r'([a-z]\w{0,19})(?=[\s\.\,\(\)\[\]]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=)'),
        ('error1', r'([a-z]\w{0,19}\{[0-9]+\}|[a-z]\w{0,19})(?=\S|$)|(((\/\*)[\s\S]*?(\*\/))|([1-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4})|([1-9]\d{0,8})|(\-[1-9]\d{0,8})|([\"\“]([^\"][ \S]*[^\"])?[\"\”])|T(r(u(e)?)?)?|F(a(l(s(e)?)?)?)?|\<\=|\>\=|\!\=|\<|\>|\=\=|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\(|\)|\[|\]|\{|\}|\.|\,|\:|Link.Start|Link.End|Generate|Sys|Sys.Call|Discharge|Absorb|Boolean|Integer|Decimal|String|If|Elif|Else|Switch|Execute|Default|For|In|While|Break|Continue|Avoid|And|Not|Or|Fixed|Struct|Return)(?=\s|\S|$)'),
        ('error', r'[\S]{1}'),
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
        if kind == 'error' or kind == 'error1':
            hasError = "Invalid character/delimiter"
            token_data.append(Token(kind,value,line_num,column,hasError))
            return token_data
        if kind == 'equal' or kind == 'relational' or kind == 'arithmetic' or kind == 'assignment' or kind == 'open_par' or kind == 'close_par' or kind == 'open_brace' or kind == 'close_brace' or kind == 'open_bracket' or kind == 'close_bracket' or kind == 'comma' or kind == 'colon' or kind == 'period' or kind == 'keyword':
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
