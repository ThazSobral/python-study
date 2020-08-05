import urllib.request
import time

def search_price():
    url = 'http://beans.itcarlow.ie/prices-loyalty.html'
    page = urllib.request.urlopen(url)
    text = page.read().decode('utf8')
    where_is_price = text.find('>$')
    start = where_is_price + 2
    end = start + 4
    return float(text[start:end])

def compare_values(desired_price, current_price):
    if desired_price >= current_price: return 'dentro do desejado'
    else: return 'alto'

monitoring_price = True
print(f'O preço do café no site Beans está R${search_price()}.')
desired_price = float(input('Qual o valor de café que você deseja? '))

while monitoring_price:
    price = search_price()
    print(f'O preço do café no site Beans está {price}. O valor está {compare_values(desired_price, price)}.')
    choice = str(input('Deseja continuar verificando? (S/N)')).lower()
    
    if choice == 'n': monitoring_price = False
    else: time.sleep(100)

print('Obrigado. Volte sempre! ')
    