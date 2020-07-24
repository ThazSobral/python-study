# break indica parada de algum laço (estrutura de repetição)

x = 0
while(x < 10):
  x += 1
  if x == 5:
    print('Interrompendo!')
    break
  print(x)