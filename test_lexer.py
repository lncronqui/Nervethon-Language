from re import X
import lexer
with open('user_input.txt', 'r') as file:
    user_input = file.read()
split_input = list(user_input)
result = lexer.run(split_input)
for x in result:
    print(x)
