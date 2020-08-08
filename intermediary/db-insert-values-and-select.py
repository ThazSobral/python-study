# o sqlite é uma biblioteca padrão e não necessita de instalação
import sqlite3
# para iniciar é necessário conectar num banco de dados
# caso ele não exista será criado um
connection = sqlite3.connect('students.db')
# o cursor é um apontador para a conexão
cursor = connection.cursor()

# o método execute serve para enviar comandos ao nosso banco de dados
cursor.execute('insert into students values("primeiro", 17)')
cursor.execute('insert into students values("segundo", 3)')

# o método fetchall requisita todos os registros do banco
for line in cursor.fetchall():
    # imprimindo linha por linha
    print(line)

# se faz necessário fechar o uso do cursor
cursor.close()
# para gravar no banco e dados
connection.commit()
# e também fechar a conexão com o banco de dados
connection.close()
