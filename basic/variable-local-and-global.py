# variável LOCAL é aquela que pode ser manipulada somente dentro de um escopo específico
# variável GLOBAL é aquela que pode ser manipulada em todo o documento e seu subsequentes

variable = 'Global'

def variableIdentify ():
  # mas podemos alterar um variável global dentro de um escopo específico utilizando a key GLOBAL
  global variable
  variable = 'Local'
  print(variable)

print(variable)
variableIdentify()
print(variable)
