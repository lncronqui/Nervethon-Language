import re
import lexer
with open('user_input.txt', 'r') as file:
    user_input = file.read()

for result in lexer.run(user_input):
    print(result)
