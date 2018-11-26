import sqlite3

def inicia_base_fornecedor(self, con):
    try:
        con.execute(
            """
            CREATE TABLE fornecedor (
                cod INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id_interno TEXT NOT NULL,
                nome TEXT NOT NULL,
                desc TEXT
            );
            """)
        con.commit()
        print('Criou Table Fornecedor')
        
        return insere_fornecedor_padrao(self, con)

    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def insere_fornecedor_padrao(self, con):
    try:
        self.executa_multiplos(
            """
            INSERT INTO fornecedor (cod, id_interno, nome, desc) VALUES( ?, ?, ?, ?)
            """, (1, "001", "Fornecedor 1", "Primeiro fornecedor"))
        con.commit()
        print('Criou Fornecedor')
        return True
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def insere_fornecedor(self, con, id_interno, nome, desc):
    try:
        cod = produtos = getFornecedores(self, con);
        self.executa_multiplos(
            """
            INSERT INTO fornecedor (cod, id_interno, nome, desc) VALUES( ?, ?, ?, ?)
            """, ((len(cod) + 1), id_interno, nome, desc))
        con.commit()
        print('Criou Produto %s', nome)
        return True
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def delete_fornecedor(self, con, cod):
    try:
        if cod:
            self.executa_multiplos(
                """
                DELETE FROM fornecedor WHERE cod = ?
                """, (cod))
        con.commit()
        print('Deletou Forneceodr %s', cod)
        return True
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def getFornecedores(self, con):
    try:
        rs = self.executa("SELECT cod, id_interno, nome, desc FROM fornecedor")
        return rs
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False