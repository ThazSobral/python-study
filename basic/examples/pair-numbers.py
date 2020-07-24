# Imprimi somente valores pares

start = 0

end = float(input('Digite um valor final: '))

while start <= end:
  if start % 2 == 0:
    print(start)
  start += 1