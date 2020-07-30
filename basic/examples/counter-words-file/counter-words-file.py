# o script mostra a 20 palavras mais frequentes dentro do arquivo de texto

# a biblioteca string disponibiliza mais funções para manipulação de texto
import string

# defini uma função para retornar apenas o valor de cada chave e valor que for passada
def counter(key_value):
  return key_value[1]

# abre o arquivo de texto, já deixando todo o texto em minúsculo
text = open(r'basic\examples\alice-dictionary\history.txt', encoding='utf8').read().lower()

# troca toda a pontução reconhecida pela função por espaço em branco
for punctuation in string.punctuation:
  text = text.replace(punctuation, ' ')

# troca os caracteres estranhos encontrados por nada
text = text.replace('”','')
text = text.replace('“','')

# converte todo o texto em uma lista
words = text.split()

# define um dicionario para contagem de palavras
word_count = {}

# percorre todas as palavras do texto
for word in words:
  if word in word_count:
    # se a chave existir dentro do dicionário ele adiciona mais um na contagem já exitente para a chave
    word_count[word] += 1
  else:
    # se não existir a chave ela é adicionada e já começa com o valor um
    word_count[word] = 1

# é realizada uma ordenação no dicionário utilizando o valor como critério
# já aplicadando a ordenação reversa (do maior para o menor) no dicionário
keys_values = sorted(word_count.items(), key=counter, reverse=True)

# percorre as primeiras 20 chaves dentro do dicionário e exibe eles na tela
for key_value in keys_values[:20]:
  print(key_value[0], key_value[1])
