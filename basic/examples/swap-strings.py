# Podemos utilizar uma única string para gerar uma lista simples.
month = ''' janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()

# Podemos atribuir variáveis multiplas de uma só vez
day, number_month, year = str(input('Insira uma data (dd/mm/aaaa): ')).split('/')

print(f'{day} de {month[int(number_month)-1]} de {year}.')
