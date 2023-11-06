import mysql.connector
from model.User import User
from model.Book import Book
from model.Loan import Loan

# Configuração de conexão com o MySQL
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '@Gremio1010',
    'database': 'gen_livros'
}

# Conecta com o banco
def connect():
    conn = mysql.connector.connect(**config)
    return conn

def save_user(User):
    conn = connect()
    cursor = conn.cursor()
    insert_query = """INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES (%s, %s, %s, %s, %s)"""
    values = (User.nome, User.sobrenome, User.endereco, User.email, User.telefone)
    cursor.execute(insert_query, values)
    conn.commit()
    conn.close()

def save_book(Book):
    conn = connect()
    cursor = conn.cursor()
    insert_query = """INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) VALUES (%s, %s, %s, %s, %s)"""
    values = (Book.titulo,Book.autor,Book.editora,Book.ano_publicacao,Book.isbn)
    cursor.execute(insert_query, values)
    conn.commit()
    conn.close()

def read_user():
    conn = connect()
    cursor = conn.cursor()
    query = """SELECT id,nome,sobrenome,endereco,email,telefone FROM usuarios"""
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    return users

def read_book():
    conn = connect()
    cursor = conn.cursor()
    query = """SELECT id,titulo,autor,editora,ano_publicacao,isbn FROM livros"""
    cursor.execute(query)
    books = cursor.fetchall()
    conn.close()
    return books

def insert_loan(Loan):
    conn = connect()
    cursor = conn.cursor()
    insert_query = """INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (%s, %s, %s, %s)"""
    values = (Loan.id_livro, Loan.id_usuario, Loan.data_emprestimo, Loan.data_devolucao)
    cursor.execute(insert_query, values)
    conn.commit()
    conn.close()

def get_books_on_loan():
    conn = connect()
    cursor = conn.cursor()
    insert_query = """SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao
                   FROM livros
                   INNER JOIN emprestimos ON livros.id = emprestimos.id_livro
                   INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario
                   WHERE emprestimos.data_devolucao IS NULL"""

    cursor.execute(insert_query)
    results = cursor.fetchall()
    conn.close()

    return results

def update_loan_return_date(data_devolucao, id_emprestimo):
    conn = connect()
    cursor = conn.cursor()
    insert_query = """UPDATE emprestimos SET data_devolucao = %s where id = %s"""
    values = (data_devolucao, id_emprestimo)
    cursor.execute(insert_query, values)

    conn.commit()
    conn.close()
