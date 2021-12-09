import re
import lexer
with open('user_input.txt', 'r') as file:
    user_input = file.read()

for result in lexer.run(user_input):
    if result.hasError == False:
        print(result)

print("Syntax Error:")
for result in lexer.run(user_input):
    if result.hasError == True:
        if result.value != "":
            print(result)