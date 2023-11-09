from funcoes import *
from config import *

while True:
    print('-' * 34)
    print('| Sistema de busca da biblioteca |')
    print('| 1 - Buscar Livro               |')
    print('| 2 - Buscar Usuario             |')
    print('| 3 - Buscar Emprestimo          |')
    print('| 0 - Sair                       |')
    print('-' * 34)
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            print('-' * 43)
            print('| Sistema de busca de livro da biblioteca |')
            print('| 1 - Buscar por ID                       |')
            print('| 2 - Buscar por nome                     |')
            print('| 3 - Buscar por ano                      |')
            print('| 4 - Buscar por autor                    |')
            print('| 5 - Buscar por setor                    |')
            print('| 6 - Buscar por gênero                   |')
            print('| 7 - Buscar por ISBN                     |')
            print('| 0 - Sair                                |')
            print('-' * 43)
            opcao_livro = int(input('Digite a opção desejada: '))

            match opcao_livro:
                case 1:
                    buscar_id_livro()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 2:
                    buscar_nome_livro()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 3:
                    buscar_ano_livro()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 4:
                    buscar_autor_livro()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 5:
                    buscar_setor_livro()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 6:
                    buscar_genero_livro()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 7:
                    buscar_isbn_livro()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 0:
                    cursor.close()
                    conexao.close()
                    break
        case 2:
            print('-' * 45)
            print('| Sistema de busca de usuario da biblioteca |')
            print('| 1 - Buscar por ID                         |')
            print('| 2 - Buscar por nome                       |')
            print('| 3 - Buscar por sobrenome                  |')
            print('| 4 - Buscar por numero telefone            |')
            print('| 0 - Sair                                  |')
            print('-' * 45)
            opcao_livro = int(input('Digite a opção desejada: '))

            match opcao_livro:
                case 1:
                    buscar_id_usuario()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 2:
                    buscar_nome_usuario()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 3:
                    buscar_cpf_usuario()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 4:
                    buscar_telefone_usuario()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 0:
                    cursor.close()
                    conexao.close()
                    break
                case _:
                    print('Opção inválida. Tente novamente.')
        case 3:
            print('-' * 48)
            print('| Sistema de busca de emprestimo da biblioteca |')
            print('| 1 - Buscar por ID emprestimo                 |')
            print('| 2 - Buscar por ID usuario                    |')
            print('| 3 - Buscar por isn                           |')
            print('| 4 - Buscar por data do emprestimo            |')
            print('| 5 - Buscar por data de devolucao             |')
            print('| 0 - Sair                                     |')
            print('-' * 48)
            opcao_emprestimo= int(input('Digite a opção desejada: '))
            
            match opcao_emprestimo:
                case 1:
                    buscar_id_emprestimo()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 2:
                    buscar_id_usuario_emprestimo()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 3:
                    buscar_isnb_livro_emprestimo()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 4:
                    buscar_data_emprestimo()
                    continuar = input('Deseja buscar novamente? (S/N) ').upper()
                    print('\n')
                case 5:
                    buscar_data_devolucao()
                    continuar = input('Deseja buscar outro emprestimo? (S/N) ').upper()
                    print('\n')
                case 0: 
                    cursor.close()
                    conexao.close()
                    break
                case _:
                    print('Opção inválida. Tente novamente.')
        case 0:
            cursor.close()
            conexao.close()
            break
        case _:
            print('Opção inválida. Tente novamente.')
    if continuar == 'N':
        cursor.close()
        conexao.close()
        break

