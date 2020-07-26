# Strings são imutáveis
# Isso naõ funciona:
#  string = 'arroba'
#  string[0] = @
# 
# Mas podemos utilizar "parâmetros de fatimento" para fazer essa alteração, por exemplo:
# string = '@' + string[1:]

string = 'arroba'

print(string)

string = '@' + string[1:]

print(string)
