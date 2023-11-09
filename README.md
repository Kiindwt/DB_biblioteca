# Sistema de busca de biblioteca usando SQL e Python

Este projeto consiste em um sistema de busca para uma biblioteca usando SQL e Python. O sistema permite que os usuários pesquisem livros, usuarios e emprestimos dos livros.

## Requisitos

Para executar este projeto, você precisará dos seguintes requisitos:

Python 3.7+ <br>
MySQL 

## Instalação

Para instalar o projeto, siga estas etapas:

1. Clone o repositório do GitHub:
```
git clone https://github.com/Kiindwt/DB_biblioteca.git
```
2. Instale os requisitos:
```
pip install -r requirements.txt
```
## Configuração

Para configurar o projeto, abra o arquivo config.py e altere as seguintes variaveis:

```host```: o endereço do servidor do banco de dados <br>
```user```: o nome de usuário do banco de dados <br>
```password```: a senha do banco de dados <br>

## Execução

Para executar o projeto, execute os seguintes comando: <br>
1. Cria um banco de dados chamado 'biblioteca' <br>
```python create_database.py``` <br>
2. Preenche o banco de dados com 100 dados aleatorios <br>
```python gerador_dados.py``` <br>
3. Executa a interface do python para fazer as consultas <br>
```python main.py```
