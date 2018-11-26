# 04_read_producto.py
import sqlite3

conn = sqlite3.connect('the_bakery.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM produtos;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
