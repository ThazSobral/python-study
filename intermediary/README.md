Estaá pasta pode necessitar da utilização do virtualenv para melhor gerenciamento dos arquivos e bibliotecas, o que evita conflitos e mal funcionamento dos escritps.

Para isso instale o virtualenv, como demonstrado a seguir:

pip install virtualenv

* para atualizar o pip utilize:

python -m pip install --upgrade pip

Para cada projeto utilize:

virtualenv <nome_da_virtualenv>

Ativar a virtualenv:

. .\<virualenv>\Scripts\activate

* pronto agora podemos instalar as dependecias

Para sair da virtualenv:

deactivate
