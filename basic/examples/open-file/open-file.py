# O método open é utilizado para tabalhar com arquivos de diversos formatos (sempre adequano o método)

# se o caminho não for fornecido se considera que o arquivo está no mesmo diretório do script
# o 'r' significa RAW, onde ele descosidera o significa das barras no endereço
# o 'w' significa WRITE, o que simboliza escrita
# quando omitir o modo de abertura ele considera o 'r' de read
file = open(r'C:\Users\User\Projects\python-study\basic\examples\open-file\test.txt', 'w')
for line in range(1, 100):
  file.write(f'{line}\n')
# o método close é importante para proteger seu arquivo (SEMPRE FECHE O ARQUIVO quando terminar)
file.close

file = open(r'C:\Users\User\Projects\python-study\basic\examples\open-file\test.txt')
# readlines significa ler linha por linha
for line in file.readlines():
  # o método strip é utilizado para remover os \n (pular linha) que é um caracter especial
  print(line.strip())
file.close