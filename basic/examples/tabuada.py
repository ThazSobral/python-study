value = float(input('Digite o número da tabuada: '))

print('-' * 15)
for interator in range(11):
  print('{} X {} = {}'.format(value, interator, (value * interator)))
print('-' * 15)
