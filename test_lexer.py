import lexer
with open('user_input.txt', 'r') as file:
    user_input = file.read().replace('\n', ' N_L ').replace('\t', '')#\n
result = lexer.run(user_input)

while True:
    print(result)