from config import *

nome_database = 'biblioteca'

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_database}")
cursor.execute("USE biblioteca;")
cursor.close()

conexao = conectar_mysql(host,user,password,nome_database)
cursor = conexao.cursor()
# criar a tabela 'livros'
create_livros_table_query = """
CREATE TABLE IF NOT EXISTS livros ( 
    id_livro INT PRIMARY KEY,  
    nome_livro VARCHAR(100),  
    ano INT,  
    nome_autor VARCHAR(60),  
    setor VARCHAR(60),  
    genero VARCHAR(60),  
    isbn VARCHAR(17) 
);
"""
cursor.execute(create_livros_table_query)

# criar a tabela 'usuarios'
create_usuarios_table_query = """
CREATE TABLE IF NOT EXISTS usuarios ( 
    id_usuario INT PRIMARY KEY,  
    nome VARCHAR(100),  
    cpf VARCHAR(14),  
    email VARCHAR(100),   
    numero_telefone VARCHAR(20) 
);
"""
cursor.execute(create_usuarios_table_query)

# criar a tabela 'emprestimos'
create_emprestimos_table_query = """
CREATE TABLE IF NOT EXISTS emprestimos (
    id_emprestimo INT PRIMARY KEY,
    id_usuario INT,
    isbn VARCHAR(17),
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
"""
cursor.execute(create_emprestimos_table_query)
conexao.commit()
