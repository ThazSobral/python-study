# dicionário é uma estrutura que segue a premissa de chave e valor
# semelhante aos objetos de algumas linguagens, como Javascript por exemplo

# declaramos um dicionário com chaves( '{}' )
dictionary = {}
# podemos adicionar uma chave nova no dicionário indicando uma nova
dictionary['new_key'] = 'The new value'

# podemos também adicionar valores variados no dicionário, como uma lista
dictionary['the_list'] = 'This is a new list'.split()

print(dictionary)

# a forma comum de acesso aos valores de um dicionário se faz através das chaves
print(f'o valor escondido em new_key é: {dictionary["new_key"]}')
