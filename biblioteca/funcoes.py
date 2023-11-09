from create_database import cursor

# FUNCOES DO LIVRO
def livro_encontrado(lista):
    for i in range(len(lista)):
        print('****************************')
        print('Livro encontrado: ')
        print(f'ID: {lista[i][0]}')
        print(f'Nome: {lista[i][1]}')
        print(f'Ano: {lista[i][2]}')
        print(f'Autor: {lista[i][3]}')
        print(f'Setor: {lista[i][4]}')
        print(f'Gênero: {lista[i][5]}')
        print(f'ISBN: {lista[i][6]}')
        print('\n')

def buscar_id_livro():
    id = int(input('Digite o ID do livro: '))
    print('\n')
    sql_query = 'SELECT * FROM livros WHERE id_livro = %s'
    cursor.execute(sql_query, ([id]),)
    
    results = cursor.fetchall()
    if results:
        livro_encontrado(results)
    else:
        print('Livro não encontrado.')

def buscar_nome_livro():
    nome_prefix = input('Digite o nome do livro: ')
    print('\n')
    sql_query = 'SELECT * FROM livros WHERE nome_livro LIKE %s'
    cursor.execute(sql_query, (f'%{nome_prefix}%',))

    result = cursor.fetchall()
    if result:
        livro_encontrado(result)
    else:
        print('Livro não encontrado.')

def buscar_ano_livro():
    ano_prefix = int(input('Digite o ano do livro: '))
    print('\n')
    sql_query = 'SELECT * FROM livros WHERE ano LIKE %s'
    cursor.execute(sql_query, (f'%{ano_prefix}%',))

    result = cursor.fetchall()
    if result:
        livro_encontrado(result)
    else:
        print('Livro não encontrado.')

def buscar_autor_livro():
    autor_prefix = input('Digite o nome do autor: ')
    print('\n')
    sql_query = 'SELECT * FROM livros WHERE nome_autor LIKE %s'
    cursor.execute(sql_query, (f'%{autor_prefix}%',))

    result = cursor.fetchall()
    if result:
        livro_encontrado(result)
    else:
        print('Livro não encontrado.')

def buscar_setor_livro():
    setor_prefix = input('Digite o setor do livro: ')
    print('\n')
    sql_query = 'SELECT * FROM livros WHERE setor LIKE %s'
    cursor.execute(sql_query, (f'%{setor_prefix}%',))

    result = cursor.fetchall()
    if result:
        livro_encontrado(result)
    else:
        print('Livro não encontrado.')

def buscar_genero_livro():
    genero_prefix = input('Digite o genero do livro: ')
    print('\n')
    sql_query = 'SELECT * FROM livros WHERE genero LIKE %s'
    cursor.execute(sql_query, (f'%{genero_prefix}%',))

    result = cursor.fetchall()
    if result:
        livro_encontrado(result)
    else:
        print('Livro não encontrado.')

def buscar_isbn_livro():
    isbn_prefix = str(input('Digite ISBN do livro: '))
    print('\n')
    sql_query = 'SELECT * FROM livros WHERE isbn LIKE %s'
    cursor.execute(sql_query, (f'%{isbn_prefix}%',))

    result = cursor.fetchall()
    if result:
        livro_encontrado(result)
    else:
        print('Livro não encontrado.')

#FUNCOES DO USUARIO
def usuario_encontrado(lista):
    for i in range(len(lista)):
        print('****************************')
        print('Usuário encontrado: ')
        print(f'ID: {lista[i][0]}')
        print(f'Nome: {lista[i][1]}')
        print(f'CPF: {lista[i][2]}')
        print(f'Email: {lista[i][3]}')
        print(f'Telefone: {lista[i][4]}')
        print('\n')

def buscar_id_usuario():
    id = int(input('Digite o ID do usuário: '))
    print('\n')
    sql_query = 'SELECT * FROM usuarios WHERE id_usuario = %s'
    cursor.execute(sql_query, ([id]),)
    
    results = cursor.fetchall()
    if results:
        usuario_encontrado(results)
    else:
        print('Usuário não encontrado.')

def buscar_nome_usuario():
    nome_prefix = input('Digite o nome do usuário: ')
    print('\n')
    sql_query = 'SELECT * FROM usuarios WHERE nome LIKE %s'
    cursor.execute(sql_query, (f'%{nome_prefix}%',))

    result = cursor.fetchall()
    if result:
        usuario_encontrado(result)
    else:
        print('Usuário não encontrado.')

def buscar_cpf_usuario():
    cpf_prefix = input('Digite o CPF do usuário: ')
    print('\n')
    sql_query = 'SELECT * FROM usuarios WHERE cpf LIKE %s'
    cursor.execute(sql_query, (f'%{cpf_prefix}%',))

    result = cursor.fetchall()
    if result:
        usuario_encontrado(result)
    else:
        print('Usuário não encontrado.')
        
def buscar_email_usuario():
    email_prefix = input('Digite o email do usuário: ')
    print('\n')
    sql_query = 'SELECT * FROM usuarios WHERE email LIKE %s'
    cursor.execute(sql_query, (f'%{email_prefix}%',))

    result = cursor.fetchall()
    if result:
        usuario_encontrado(result)
    else:
        print('Usuário não encontrado.')

def buscar_telefone_usuario():
    telefone_prefix = input('Digite o telefone do usuário: ')
    print('\n')
    sql_query = 'SELECT * FROM usuarios WHERE telefone LIKE %s'
    cursor.execute(sql_query, (f'%{telefone_prefix}%',))

    result = cursor.fetchall()
    if result:
        usuario_encontrado(result)
    else:
        print('Usuário não encontrado.')

#FUNCOES EMPRESTIMOS
def emprestimo_encontrado(lista):
    for i in range(len(lista)):
        print('****************************')
        print('Empréstimo encontrado: ')
        print(f'ID emprestimo: {lista[i][0]}')
        print(f'ID do usuário: {lista[i][1]}')
        print(f'Codigo isnb: {lista[i][2]}')
        print(f'Data de empréstimo: {lista[i][3]}')
        print(f'Data de devolução: {lista[i][4]}')
        print('\n')

def buscar_id_emprestimo():
    id = int(input('Digite o ID do empréstimo: '))
    print('\n')
    sql_query = 'SELECT * FROM emprestimos WHERE id_emprestimo = %s'
    cursor.execute(sql_query, ([id]),)
    
    results = cursor.fetchall()
    if results:
        emprestimo_encontrado(results)
    else:
        print('Empréstimo não encontrado.')

def buscar_id_usuario_emprestimo():
    id = int(input('Digite o ID do usuário: '))
    print('\n')
    sql_query = 'SELECT * FROM emprestimos WHERE id_usuario = %s'
    cursor.execute(sql_query, ([id]),)
    
    results = cursor.fetchall()
    if results:
        emprestimo_encontrado(results)
    else:
        print('Empréstimo não encontrado.')

def buscar_isnb_livro_emprestimo():
    isbn = str(input('Digite o ISBN do livro: '))
    print('\n')
    sql_query = 'SELECT * FROM emprestimos WHERE id_livro LIKE %s'
    cursor.execute(sql_query, (f'%{isbn}%',))
    
    results = cursor.fetchall()
    if results:
        emprestimo_encontrado(results)
    else:
        print('Empréstimo não encontrado.')

def buscar_data_emprestimo():
    data = str(input('Digite a data(Y-M-D) de empréstimo:  '))
    print('\n')
    sql_query = 'SELECT * FROM emprestimos WHERE data_emprestimo LIKE %s'
    cursor.execute(sql_query, (f'%{data}%',))
    
    results = cursor.fetchall()
    if results:
        emprestimo_encontrado(results)
    else:
        print('Empréstimo não encontrado.')

def buscar_data_devolucao():
    data = str(input('Digite a data(Y-M-D) de devolução: '))
    print('\n')
    sql_query = 'SELECT * FROM emprestimos WHERE data_devolucao LIKE %s'
    cursor.execute(sql_query, (f'%{data}%',))
    
    results = cursor.fetchall()
    if results:
        emprestimo_encontrado(results)
    else:
        print('Empréstimo não encontrado.')

