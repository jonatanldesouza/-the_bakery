# 05_delete_produto.py
import sqlite3

conn = sqlite3.connect('the_bakery.db')
cursor = conn.cursor()

id_produto =  input('Código do produto: ')

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM produtos
WHERE id = ?
""", (id_produto,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()
