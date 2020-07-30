# Herança é um conceito importante quando utilizamos classe
# isso permite aproveitarmos uma classe já existente dentro de outra classe

class Account:
  # podemos passar vários atributos para o método além de self
  # e podemos também definir valores padrões para um atributo, caso ele não sejá passado
  def __init__(self, clients, number, balance=0):
    self.balance = balance
    self.clients = clients
    self.number = number
    self.operations = []
    self.deposit(balance)

  def withdraw_money(self, value):
    if value > self.balance:
      return False
    else:
      self.balance -= value
      self.operations.append(['withdraw_money', vale])

  def deposit(self, value):
    self.balance += value
    self.operations.append(['Deposit', value])

# Ou seja, quando herdamos alguma classe, a classe que recebe possuirá todos os atributos e métodos da classe herdada
  class EspecialAccount(Account):
    def __init__(self, clients, number, balance=0, limit=0):
      Account.__init__(self, clients, number, balance)
      self.limit = limit
# podemos também modificar ou adicionar algum método, mas sempre como base a classe herdada
    def withdraw_money(self, value):
      if self.balance + self.limit >= value:
        self.balance -= value
        self.operations.append(['withdraw_money', value])
        