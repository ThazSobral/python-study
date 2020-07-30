# Classes são estruturas que contém
# atributos (características) que podem ser constantes, variáveis, etc. Já pré definidas dentro da estrutura
# métodos (ações) que são equiparadas aos métodos

# para declarar uma classe precisamos utilizar a key-word CLASS
class TV:
  # dentro da classe declaramos os métodos dessa classe
  # às classes têm um tipo especial de método que é conhecido como construtor
  # O construtor é o método utilizado para iniciar a classe
  # o parâmetro self siginifca o objeto instânciado em si
  def __init__(self):
    self.on = False
    self.channel = 2

  def down_change_channel(self):
    self.channel -= 1
  
  def up_change_channel(self):
    self.channel += 1

# para utilizar a classe utilizamos uma instância dela
# dessa forma, uma classe é o molde, e a instância é o objeto gerado apartir do molde
# podemos então gerar várias instâncias apartir de uma classe
# quando criamos um objeto nós basicamente chamamos o método contrutor da classe
tv_bedroom = TV()
tv_room = TV()
tv_kitchen = TV()

# podemos acessar seus atributos apenas chamando eles
# print(tv_bedroom.channel)

# podemos também alterar os valores da mesma forma
tv_bedroom.channel = 3
print(tv_bedroom.channel)

# podemos chamar os métodos da função de forma semelhante a chamar um atributo
tv_bedroom.up_change_channel()
print(tv_bedroom.channel)