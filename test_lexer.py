from re import X
import lexer
with open('user_input.txt', 'r') as file:
    user_input = file.read().replace('\n', ' N_L ').replace('\t', '')#\n
split_input = user_input.split()
test_input = ["Generate", "Absorb"]
test = "Generate Absorb"
result = []
for x in split_input:
    result.append(lexer.run(x))
for x in result:
    print(x)
