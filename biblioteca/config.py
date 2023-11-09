import mysql.connector

def conectar_mysql(host, user, password,database=None):
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return conexao

host = 'localhost'
user = 'root'
password = 'senha'

conexao = conectar_mysql(host,user,password)
cursor = conexao.cursor()

