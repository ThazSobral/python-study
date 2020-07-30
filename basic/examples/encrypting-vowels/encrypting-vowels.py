# Encriptar as vogais é um exemplo do que podemos fazer com arquivos de texto
# onde encontramos os caracteres buscados dentro de um arquivo .txt
# e substituimos por '*'

# abrimos os arquivos, tanto o de leitura quanto o de escrita
text = open(r'basic\examples\encrypting-vowels\mensage.txt', 'r')
crypt = open(r'basic\examples\encrypting-vowels\crypt.txt', 'w')

# verificamos linha por linha do arquivo de leitura
for line in text.readlines():
  # verificamos letra por letra da linha
  for letter in line:
    # se a letra executada existir na string
    if letter in 'aeiouãõáéíóúâêô':
      # escreve * no arquivo de escrita
      crypt.write('*')
    else:
      # caso não, escreva a linha
      crypt.write(letter)

# sempre fechar os arquivos
text.close()
crypt.close()
