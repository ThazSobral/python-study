# FOR é uma estrutura que permite criar um laço (repetição) com mais liberdade de controle, ou um WHILE "enxuto",
# mas cada um com sua particularidade

# podemos percorrer uma sequência assim como no while mas de forma unitária, por exemplo
print('Sequência:')
for value in range(10): print(value)
# onde o primeiro valor é 0 e o último é 9 (10 valores)
# ou podemos definir um intervalo
print('\nCom intervalo:')
for value in range(1, 5): print(value)

# podemos percorrer uma string
print('\nCom string:')
for value in 'show': print(value)

# podemos fazer o mesmo com uma lista
print('\nCom lista:')
for value in ['show', 42, True, 3.17]: print(value)
