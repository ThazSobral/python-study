# Palindrome é quando uma expressão é a mesma
# tanto de frente para trás quanto de trás para frente

first_string = str(input('Qual palavra deseja verificar se é palindrome? '))

second_string = first_string[::-1]

if first_string == second_string:
  print(f'{first_string} é palindrome')
else:
  print(f'{first_string} não é palindrome')
