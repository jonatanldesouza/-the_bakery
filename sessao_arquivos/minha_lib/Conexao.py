# https://docs.python.org/2/library/sqlite3.html

import sqlite3
from minha_lib.funcoes import arquivo_existe


class Conexao:

    __caminho = 'minha_base_sqlite.db'
    __conexao = None
    __cursor  = None

    def __init__(self):
        print('* Conexao.__init__() ')
        if arquivo_existe(self.__caminho):
            print('Ok caminho já existe apenas conecta! ')
            self.conecta()
        else:
            print('Ok caminho já existe apenas conecta! ')
            self.conecta()
            self.inicia_base()

    def conecta(self):
        print('* Conexao.conecta() ')
        if self.__conexao is None:
            self.__conexao = sqlite3.connect(self.__caminho)
            self.__cursor = self.__conexao.cursor()

        print(self.__conexao)
        print(self.__cursor)

    def close(self):
        print('* Conexao.close() ')
        self.__conexao.close()

    def inicia_base(self):
        print('* Conexao.inicia_base()')
        #  SQLite Foreign Key Support - https://www.sqlite.org/foreignkeys.html , FOREIGN KEY(..) REFERENCES artist(..)
        try:
            self.__conexao.execute(
                """
                CREATE TABLE tb_produto (
                    pr_codseq INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    pr_nompro TEXT NOT NULL,
                    pr_descri INTEGER,
                    pr_sigsku TEXT
                );
                """)
            self.__conexao.commit()
            return True
        except sqlite3.Error as er:
            print(' - Conexao.inicia_base() CREATE TABLE tb_produtos = .Error  %s' % er)
            return False

    def executa(self, sql, valores=None):
        print('* Conexao.executa() = %s ' % sql)
        try:
            self.__cursor.execute(sql, valores)
            self.__conexao.commit()
            return self.__cursor.fetchall()
        except sqlite3.Error as er:
            print(' - Conexao.insert() sqlite3.Error  %s' % er)
            return False

    def executa_multiplos(self, sql, arr ):
        print('* Conexao.executemany() = %s' % sql)
        try:
            self.__cursor.execute(sql, arr)
            return self.__cursor.fetchall()
            return True
        except sqlite3.Error as er:
            print(' - Conexao.insert() sqlite3.Error  %s' % er)
            return False