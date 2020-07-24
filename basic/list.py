# listas são valores ligados que possuem posições específicas (ou endereços) dentro da estrutura
# podem esses valores serem recuperados quando apontados entre [] após o nome da lista
# podemos encarar as listas como um trem, onde:
# - os valores são vagões;
# - e cada endereço é a posição do vagão.

building = [
  'Souza',
  'Brito',
  'Jorge',
  'Tanaka'
]

end = len(building)

while (end >= 0):
  print(building[end - 1])
  end  -= 1

print('end\n')

# podemos adicionar mais vagões

building.append('Shikamui')

# não precisa ser de um único tipo

building.append(42)

print(building)

# ou podemos retirar o último vagão

building.pop()

print(building)

# ou algum específico

building.remove('Souza')

print(building)