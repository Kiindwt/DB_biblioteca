from faker import Faker
from create_database import conexao, cursor

def gerador_de_dados(num_dados):
    faker = Faker('pt_BR')

    livros = []
    for i in range(num_dados):
        livro = {
            'id_livro': i + 1,
            'nome_livro': faker.catch_phrase(),
            'ano': faker.random_int(min=1980, max=2023),
            'nome_autor': faker.name(),
            'setor': faker.random_element(elements=('Ficção', 'Não Ficção', 'Romance', 'Mistério', 'Aventura')),
            'genero': faker.random_element(elements=('Fantasia', 'Sci-Fi', 'Drama', 'Suspense', 'Romance')),
            'isbn': faker.isbn13(separator='-'),
        }
        livros.append(livro)

    usuarios = []
    for i in range(num_dados):
        usuario = {
            'id_usuario': i + 1,
            'nome': faker.first_name(),
            'cpf': faker.cpf(),
            'email': faker.email(),
            'numero_telefone': faker.phone_number(),
        }
        usuarios.append(usuario)

    emprestimos = []
    for i in range(num_dados):
        emprestimo = {
            'id_emprestimo': i + 1,
            'id_usuario': faker.random_int(min=1, max=num_dados),
            'isbn': faker.isbn13(separator='-'),
            'data_emprestimo': faker.date_between(start_date='-1y', end_date='today'),
            'data_devolucao': faker.date_between(start_date='today', end_date='+1y')
        }
        emprestimos.append(emprestimo)

    for livro in livros:
        sql_query = "INSERT INTO livros (id_livro, nome_livro, ano, nome_autor, setor, genero, isbn) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (livro['id_livro'], livro['nome_livro'], livro['ano'], livro['nome_autor'], livro['setor'], livro['genero'], livro['isbn'])
        cursor.execute(sql_query, data)

    for usuario in usuarios:
        sql_query = "INSERT INTO usuarios (id_usuario, nome, cpf, email, numero_telefone) VALUES (%s, %s, %s, %s, %s)"
        data = (usuario['id_usuario'], usuario['nome'], usuario['cpf'], usuario['email'], usuario['numero_telefone'])
        cursor.execute(sql_query, data)

    for emprestimo in emprestimos:
        sql_query = "INSERT INTO emprestimos (id_emprestimo, id_usuario, isbn, data_emprestimo, data_devolucao) VALUES (%s, %s, %s, %s, %s)"
        data = (emprestimo['id_emprestimo'], emprestimo['id_usuario'], emprestimo['isbn'], emprestimo['data_emprestimo'], emprestimo['data_devolucao'])
        cursor.execute(sql_query, data)

    conexao.commit()
    cursor.close()
    conexao.close()


if __name__ == "__main__":
    gerador_de_dados(100)

