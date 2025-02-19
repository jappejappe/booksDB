import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

DB = os.getenv('DB')
PASSWD = os.getenv('PASSWD')
USER = os.getenv('USER')
HOST = os.getenv('HOST')

connect = sqlite3.connect(
    database = DB
)

cursor = connect.cursor()


# cursor.execute('''
#             CREATE TABLE books (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome TEXT NOT NULL,
#             autor INTEGER NOT NULL
#             )
# ''')

nome = input("Título do livro: ")
autor = input("Autor do livro: ")

cursor.execute('INSERT INTO books (nome, autor) VALUES (?, ?)', (nome, autor))

connect.commit()

cursor.execute('SELECT * FROM books')

resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

connect.close()