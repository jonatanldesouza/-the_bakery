# connect_db.py
import sqlite3

# conectando...
conn = sqlite3.connect('the_bakery.db')
# desconectando...
conn.close()
