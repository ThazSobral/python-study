# DEF é uma palavra reservada para definir uma função
# assim podemos chamar esse escopo definido com DEF no decorrer do código

def isPair(value):
  return value%2 == 0

print(f'O valor 2 é par? {isPair(2)}')
print(f'O valor 3 é par? {isPair(3)}')