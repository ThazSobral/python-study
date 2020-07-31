# o script permite você tentar o número quer gerado pelo computador
import random

print('Adivinhando 0 ou 1')

end_game = 'n'

#continua o laço até que end_game sejá 's'
while(end_game != 's'):
  value = int(input('Escolha 0 ou 1: '))

  # gera o valor randomicamente zero ou um e compara com o valor escolhido pelo usuário
  if value == random.randint(0, 1):
    print('Acertou!')
  else:
    print('Errou!')
  
  end_game = input('Quer sair do jogo? (s/n)')

print('Fim de jogo')
