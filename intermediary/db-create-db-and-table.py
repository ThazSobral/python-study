# o sqlite é uma biblioteca padrão e não necessita de instalação
import sqlite3

# para iniciar é necessário conectar num banco de dados
# caso ele não exista será criado um
# se exisir os comandos a seguir não serão executados
connection = sqlite3.connect('students.db')
# o cursor é um apontador para a conexão
cursor = connection.cursor()
# o método execute serve para enviar comandos ao nosso banco de dados
cursor.execute('''
                create table if not exists students(
                    login varchar(8),
                    ra integer,
                    email varchar (12)
                )
                ''')
# se faz necessário fechar o uso do cursor
cursor.close()
# e também fechar a conexão com o banco de dados
connection.close()
