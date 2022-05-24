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
        ('COMMENT', r'(\/\*)[\s\S]*?(\*\/)(?=\s|\S|$)'),
    #    ('ARRAY_ELEMENT', r'[a-z]\w{0,19}\{([0-9]{1,9}|[a-z]\w{0,19})\}(?=[\s\.\,\(\)\[\]\{\}]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=)'),
    #    ('ARRAY', r'[a-z]\w{0,19}\{\}(?=[\s\,\:\=\)])'),
        ('LIT_DECPOSI', r'(([0-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\})'),
        ('LIT_DECNEGA', r'\-(([0-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4}))(?= |\n|\<\=|\>\=|\!\=|\<|\>|\=\=|\:|\,|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\)|\]|\})'),
        ('LIT_INTPOSI', r'([0-9]\d{0,8})(?=[\s\,\(\)\[\]\{\}]|\<\=|\>\=|\!\=|\<|\>|\=\=|\+|\-|(\/\/)|(\*\*)|\*|\/|\%)'),
        ('LIT_INTNEGA', r'(\-[1-9]\d{0,8})(?=[\s\,\(\)\[\]\{\}]|\<\=|\>\=|\!\=|\<|\>|\=\=|\+|\-|(\/\/)|(\*\*)|\*|\/|\%)'),
        ('LIT_STR', r'[\"\“]{1}([^\"^\n^\“^\”])*?[\"\”]{1}(?=[\s\,\(\)\[\]\{\}\:])'),
        ('LIT_BOOL', r'(True|False)(?=[\s\,\(\)\[\]\{\}])'),
        ('RELATIONAL', r'(\<\=|\>\=|\!\=|\<|\>|\=\=)(?= |[a-z]|[0-9]|\()'),
        ('EQUAL', r'\=(?= |[a-z]|[0-9]|\(|\"|\“)'),
        ('ASSIGNMENT', r'(\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=)(?= |[a-z]|[0-9]|\()'),
        ('ARITHMETIC', r'(\+|\-|(\/\/)|(\*\*)|\*|\/|\%)(?= |[a-z]|[0-9]|\()'),
        ('OPEN_PAR', r'\((?=[a-zANOISDB0-9\(\)])'),
        ('CLOSE_PAR', r'\)(?=And|Or|Not|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\<\=|\>\=|\!\=|\<|\>|\=\=|[\s\:\[\)])'),
        ('OPEN_BRACE',r'\{(?=[a-zA-Z\d\"|\“])'),
        ('CLOSE_BRACE',r'\}(?=[\s\)]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=|And|Or|Not)'),
        ('OPEN_BRACKET', r'\[(?=[\sa-z\"\“\d])'),
        ('CLOSE_BRACKET', r'\](?= |\n|$)'),
        ('COMMA', r'\,(?=[ A-Za-z0-9])'),
        ('COLON', r'\:(?=[\s\[])'),
        ('PERIOD', r'\.(?=[a-zA-Z\d])'),
        ('KEYWORD', r'((Integer|Decimal|String|Boolean|Struct|Generate|Absorb|Discharge|Switch|For|In|Sys|Sys\.Call|Execute|Fixed|Return)(?= ))|((Default|Else)(?=\:))|((If|Elif|And|Or|Not|While)(?=[ \(]))|Link\.End(?=\n|$)|(Link\.Start|End\.Switch|Break|Continue|Avoid)(?=\n)'),
        ('NON_KEYWORD', r'(e(?i:nd\.switch)|b(?i:reak)|l(?i:ink\.start)|l(?i:ink\.end)|g(?i:enerate)|s(?i:ys\.call)|s(?i:ys)|d(?i:ischarge)|a(?i:bsorb)|i(?i:f)|e(?i:lif)|e(?i:lse)|s(?i:witch)|e(?i:xecute)|d(?i:efault)|f(?i:or)|w(?i:hile)|e(?i:xit)|c(?i:ontinue)|a(?i:void)|f(?i:ixed)|s(?i:truct)|v(?i:oid)|r(?i:eturn)|i(?i:nteger)|b(?i:oolean)|s(?i:tring)|d(?i:ecimal)|a(?i:nd)|o(?i:r)|n(?i:ot)|t(?i:rue)|f(?i:alse)|i(?i:n))(?=[\s\.\,\(\)\[\]\{\}]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=)'),
        ('NEWLINE', r'\n'),
        ('TAB_SPACE', r'[ \t]'),
        ('ID', r'([a-z]\w{0,19})(?=[\s\.\,\(\)\[\]]|\+|\-|(\/\/)|(\*\*)|\*|\/|\%|\=|\-\=|\+\=|\*\=|\/\=|\*\*\=|\%\=|\/\/\=|\<\=|\>\=|\!\=|\<|\>|\=\=|\:)'),
        ('ERROR1', r'([a-z]\w{0,19}(\{([0-9]+(\})?)?)?|[a-z]\w{0,19})(?=\S|$)|(\/(\*([\s\S]*(\*(\/)?)?)?)?|([1-9]\d{0,8}\.\d{0,5})|(\d{0,9}\.\d{1}\d{0,4})|([1-9]\d{0,8})|(\-[1-9]\d{0,8})|[\"\“]{1}([^\"^\n^\“^\”])*?[\"\”]{1}|T(r(u(e)?)?)?|F(a(l(s(e)?)?)?)?|\<\=?|\>\=?|\!\=?|\<|\>|\=\=?|\=|\-\=?|\+\=?|\*\=?|\/\=?|\*(\*(\=)?)?|\%\=?|\/(\/(\=)?)?|\+|\-|(\/\/?)|(\*\*?)|\*|\/|\%|\(|\)|\[|\]|\{|\}|\.|\,|\:|L(i(n(k(\.(S(t(a(r(t)?)?)?)?)?)?)?)?)?|L(i(n(k(\.(E(n(d)?)?)?)?)?)?)?|G(e(n(e(r(a(t(e)?)?)?)?)?)?)?|S(y(s)?)?|S(y(s(\.(C(a(l(l)?)?)?)?)?)?)?|D(i(s(c(h(a(r(g(e)?)?)?)?)?)?)?)?|A(b(s(o(r(b)?)?)?)?)?|B(o(o(l(e(a(n)?)?)?)?)?)?|I(n(t(e(g(e(r)?)?)?)?)?)?|D(e(c(i(m(a(l)?)?)?)?)?)?|S(t(r(i(n(g)?)?)?)?)?|I(f)?|E(l(i(f)?)?)?|E(l(s(e)?)?)?|S(w(i(t(c(h)?)?)?)?)?|E(x(e(c(u(t(e)?)?)?)?)?)?|D(e(f(a(u(l(t)?)?)?)?)?)?|F(o(r)?)?|I(n)?|W(h(i(l(e)?)?)?)?|B(r(e(a(k)?)?)?)?|C(o(n(t(i(n(u(e)?)?)?)?)?)?)?|A(v(o(i(d)?)?)?)?|A(n(d)?)?|N(o(t)?)?|O(r)?|F(i(x(e(d)?)?)?)?|S(t(r(u(c(t)?)?)?)?)?|E(n(d(\.(S(w(i(t(c(h)?)?)?)?)?)?)?)?)?|R(e(t(u(r(n)?)?)?)?)?)(?=\s|\S|$)'),
        ('ERROR', r'[\S]{1}'),
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
        if kind == 'ERROR':
            hasError = "Invalid character"
        if kind == 'ERROR1':
            hasError = "Invalid delimiter"
        if kind == 'EQUAL' or kind == 'RELATIONAL' or kind == 'ARITHMETIC' or kind == 'ASSIGNMENT' or kind == 'OPEN_PAR' or kind == 'CLOSE_PAR' or kind == 'OPEN_BRACE' or kind == 'CLOSE_BRACE' or kind == 'OPEN_BRACKET' or kind == 'CLOSE_BRACKET' or kind == 'COMMA' or kind == 'COLON' or kind == 'PERIOD' or kind == 'KEYWORD':
            kind = value
        elif kind == 'NON_KEYWORD':
            hasError = "Reserved word cannot be used as an identifier"
            kind = 'ERROR'
        elif kind == 'LIT_INTPOSI' or kind == 'LIT_INTNEGA':
            value = int(value)
        elif kind == 'LIT_DECPOSI' or kind == 'LIT_DECNEGA':
            value = float(value)
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'TAB_SPACE':
            continue
        token_data.append(Token(kind,value,line_num,column,hasError))
        hasError = ""
    return token_data
