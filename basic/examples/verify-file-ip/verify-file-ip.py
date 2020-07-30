# verificar ip é importante e nesse script faremos o básico que é checar o tamanha de bytes de cada octeto 

def verify_ip(ip):
  # dividimos o ip pelo ponto
  ip = ip.split('.')
  # e percorremos cada posição da lista
  for byte in ip:
    # transformamos o valor na posição em inteiro e verificamos se é maior que 255
    if int(byte) > 255:
      # se for maior, então o ip é inválido
      return False
  # se não for encontrado nenhum octeto inválido, o ip é válido
  return True

# abrimos os arquivos
# um pra leitura apenas
# e dois pra escrever os ips válidos e inválidos
file = open(r'basic\examples\verify-file-ip\ips.txt')
validates = open(r'basic\examples\verify-file-ip\validates-ip.txt', 'w')
undervalidates = open(r'basic\examples\verify-file-ip\undevalidates.txt', 'w')

# percorremos o arquivo de leitura linha por linha
for line in file.readlines():
  # executamos cada linha com a função definida a cima
  if verify_ip(line):
    # se retornar True, escrevemos o ip no arquivo de válidos
    validates.write(line)
  else:
    # caso não retorne True, escrevemos o ip no arquivo de inválidos
    undervalidates.write(line)

# sempre fechamos os arquivos
file.close()
validates.close()
undervalidates.close()