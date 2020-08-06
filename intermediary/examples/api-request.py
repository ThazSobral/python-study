# Esse script se destina a realizar uma requisição para uma api e mostrar na tela a resposta

import urllib.request
# utilizamos a biblioteca de json para interpretar a estrutura json
import json

# determinamos a url que vamos utilizar
url = 'http://api.icndb.com/jokes/random/limitTo=[nerdy]'

# realizamos a requisição
response = urllib.request.urlopen(url).read()
# lemos a resposta carregando uma estrutura em json com decodificação UTF-8
data = json.loads(response.decode('utf8'))

print(f'Joke --> {data["value"]["joke"]}')
