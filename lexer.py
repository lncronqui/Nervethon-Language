from typing import NamedTuple
import re


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int
    
#MAIN FUNCTION#
def run(lexeme):
    keywords= {}
    token_specification = [
        ()
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for x in re.finditer(tok_regex, code):
        kind = x.lastgroup
        value = x.group()
        column = x.start() - line_start