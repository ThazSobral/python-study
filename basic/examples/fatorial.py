# Fatorial segue a logica de multiplicar desde o valor 1 até o valor desejado (recursivamente)
# Ex.: Fatorial de 5
# 1 * 2 * 3 * 4 * 5 = 120

def fat (value):
  if value == 1:
    return value
  else:
    return fat(value - 1) * value

end = float(input('Fatorial de qual valor deseja? '))

result = fat(end)

print(result)
