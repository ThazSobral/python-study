# Fatiamento de strings é a maneira de definir a forma de recorte de uma string, por exemplo:
#  com a variável definida com uma string
#  variable = 'string'
#  podemos recortar a string de acordo com os parametros seguintes
#  variable[<indíce_inicial>:<indíce_final>:<qtd_de_saltos>]
#
# Os indíces podem ser referenciados com números negativos, por exemplo:
#  o valor -1 significa último valor da string
#  os numeros negativos reference aos valores andados para trás
#  mas quando referenciado um número inicial negativo não pode ocorrer um erro se o
#  se o indíce final for positivo
#
# Se a quantidade de saltos for negativo, podemos manipular a forma de andar com as strings,
# por exemplo:
#  se utilizado o valor -1 fazemos com que seja andado de trás pra frente

number = '0123456789'

print(number[2:-1])

print(number[::-1])