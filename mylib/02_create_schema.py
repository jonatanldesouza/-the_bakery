# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('the_bakery.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE fornecedores (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	telefone TEXT,
	cnpj  VARCHAR(11) NOT NULL,	
	cidade TEXT,
	uf VARCHAR(2) NOT NULL,
	email TEXT NOT NULL,
	criado_em DATE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE produtos (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	codPro VARCHAR(100) NOT NULL,
	nome TEXT NOT NULL,
	deposito TEXT,
	quantidadeEstoque  INTEGER NOT NULL,	
	quantidadeMinima  INTEGER NOT NULL,	
	quantidadeMaxima  INTEGER NOT NULL,	
	criado_em DATE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE produtos_x_fornecedor (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	idPruduto INTEGER NOT NULL,
	idFornecedor INTEGER NOT NULL,
	cotacao float,
	constraint pk_idprofor primary key(id),
	constraint fk_produto FOREIGN KEY (idPruduto),
	constraint fk_fornecedor FOREIGN KEY (idFornecedor),
  REFERENCES prudutos (idPruduto),
  REFERENCES fornecedores (idFornecedor)
);
""")

print('Tabelas criada com sucesso.')
# desconectando...
conn.close()
