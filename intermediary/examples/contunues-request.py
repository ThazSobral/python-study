# o script é definido para fazer requisições até quando o usuário definir que não quer mais

# para isso utilizamos a biblioteca e requisição padrão
import urllib.request
# e uma biblioteca de tempo para realizar operações específicas de tempo
import time

# abrir uma função que realiza a busca por um preço na resposta e uma requisição
def search_price():
    # definimos uma url
    url = 'http://beans.itcarlow.ie/prices-loyalty.html'
    # realização um requisição
    page = urllib.request.urlopen(url)
    # lemos o conteúdo da resposta com o padrão utf8
    text = page.read().decode('utf8')
    # buscamos um padrão na resposta
    where_is_price = text.find('>$')
    # a partir da posição do padrão encontrado definimos um número de casas para frente que precisamos
    # para ser nosso ponto inicial
    start = where_is_price + 2
    # e um número de casas para o nosso ponto final
    end = start + 4
    # retornamos o valor com base no ponto inicial e final
    return float(text[start:end])

# definimos uma função para comparar valores
def compare_values(desired_price, current_price):
    if desired_price >= current_price: return 'dentro do desejado'
    else: return 'alto'

# definimos uma variável para ser nosso critério de parada de busca
# se True continua o laço, se False sai do laço
monitoring_price = True
print(f'O preço do café no site Beans está R${search_price()}.')
# recebemos o nosso preço desejado
desired_price = float(input('Qual o valor de café que você deseja? '))

while monitoring_price:
    # realiza a busca pelo valor
    price = search_price()
    # mostra o valor e compara ele com o valor desejado
    print(f'O preço do café no site Beans está {price}. O valor está {compare_values(desired_price, price)}.')
    choice = str(input('Deseja continuar verificando? (S/N)')).lower()
    
    # verifica se o laço continua
    if choice == 'n': monitoring_price = False
    else: time.sleep(100)

print('Obrigado. Volte sempre! ')
    