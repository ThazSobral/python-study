# requisições são muito úteis quando queremos trabalhar com dados remotos
# mas para fazer isso podemos utilizar a biblioteca padrão do python URLLIB com o método REQUEST

import urllib.request

# fazemos uma requisição para uma url utilizando a biblioteca urllib
# e armazenamos a resposta na variável page
# page = urllib.request.urlopen('http://beans.itcarlow.ie/prices.html')
page = urllib.request.urlopen('https://api.github.com/users/octocat')

# podemos ler o conteúdo da resposta, mas precisamos primeiro definir o decodidficador que será usado para ler o conteúdo ()
text = page.read().decode('utf8')

# após conhecermos nosso texto podemos reconhecer padrões que nos permite sempre exibir informações
# por exemplo o login na resposta
print(text[ text.find('"login":"') + 9 : text.find(',"id"') - 1])
