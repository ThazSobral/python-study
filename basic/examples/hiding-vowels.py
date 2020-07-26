string = str(input('Digite uma frase: '))
count = 0
string_empty = ''

while count < len(string):
  if string[count] in 'aeiou':
    string_empty += '*'
  else:
    string_empty +=string[count]
  count += 1

print(string_empty)
