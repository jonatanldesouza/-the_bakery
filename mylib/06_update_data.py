# 06_update_produto.py
import sqlite3

conn = sqlite3.connect('the_bakery.db')
cursor = conn.cursor()

id_produto =  input('Código do produto: ')
novo_deposito = input('novo deposito: ')
novo_saldo = input('novo saldo: ')

cursor.execute("""
UPDATE produtos
SET deposito = ?, quantidadeEstoque = ?
WHERE id = ?
""", (novo_deposito, novo_saldo, id_produto))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()
