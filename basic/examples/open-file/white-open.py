# o método WITH server para abrir um escopo onde o arquivo será utilizada, passando o 'apelido' após o AS
# utilizando o WITH não é necessário utilizar o método close

with open(r'C:\Users\User\Projects\python-study\basic\examples\open-file\test.txt') as file:
  # o método read serve para ler o arquivo
  print(file.read())