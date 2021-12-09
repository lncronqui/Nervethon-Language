import lexer
with open('user_input.txt', 'r') as file:
    user_input = file.read().replace('\n', ' N_L ').replace('\t', '')#\n
split_input = user_input.split()

for x in split_input:
    result = lexer.run(x)
    for x in result:
        print(x)
