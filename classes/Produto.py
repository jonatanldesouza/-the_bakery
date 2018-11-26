import sqlite3
import datetime

now = datetime.datetime.now()

def inicia_base_produto(self, con):
    try:
        con.execute(
            """
            CREATE TABLE produto (
                cod INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id_interno TEXT NOT NULL,
                nome TEXT NOT NULL,
                desc TEXT,
                valor NUMERIC,
                estoque NUMERIC,
                criado_em DATE NOT NULL
            );
            """)
        con.commit()
        print('Criou Table Produto')
        
        return insere_produto_padrao(self, con)

    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def insere_produto_padrao(self, con):
    try:
        self.executa_multiplos(
            """
           INSERT INTO produto (cod, id_interno, nome, desc, valor, estoque,criado_em) VALUES( ?, ?, ?, ?, ?, ?)
            """, (1, "001", "Produto 1", "Primeiro produto cadastrado automaticamente", 50, 10,31/12/1900))
        con.commit()
        print('Criou Produto')
        return True
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def insere_produto(self, con, id_interno, nome, desc, valor, estoque):
    try:
        cod = produtos = getProdutos(self, con);
        self.executa_multiplos(
            """
            INSERT INTO produto (cod, id_interno, nome, desc, valor, estoque,criado_em) VALUES( ?, ?, ?, ?, ?, ?, ?)
            """, ((len(cod) + 1), id_interno, nome, desc, valor, estoque,now))
        con.commit()
        print('Criou Produto %s', nome)
        return True
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def delete_produto(self, con, cod):
    try:
        if cod:
            self.executa_multiplos(
                """
                DELETE FROM produto WHERE cod = ?
                """, (cod))
        con.commit()
        print('Deletou Produto %s', cod)
        return True
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def getProdutos(self, con):
    try:
        rs = self.executa("SELECT cod, id_interno, nome, desc, valor, estoque FROM produto")
        return rs
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def get5Produtos(self, con):
    try:
        rs5 = self.executa("SELECT cod, id_interno, nome, desc, valor, estoque,criado_em FROM produto ORDER BY cod DESC LIMIT 3")
        return rs5
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False 

def getproduto(self, con, cod):
    try:
        rs = self.executa("SELECT cod, id_interno, nome, desc, valor, estoque,criado_em FROM produto WHERE cod = ?", (cod))
        print('Pegou o  Produto %s', cod)
        return rs
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False      