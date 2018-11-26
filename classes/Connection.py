import sqlite3
from classes.utils import arquivo_existe
from classes.Usuario import inicia_base_usuario
from classes.Produto import inicia_base_produto, getProdutos, insere_produto, delete_produto, get5Produtos, getproduto
from classes.Fornecedor import inicia_base_fornecedor, getFornecedores, insere_fornecedor, delete_fornecedor


class Connection:

    __nome = 'the_bakery.db'
    __conexao = None
    __cursor  = None

    def __init__(self):
        if arquivo_existe(self.__nome):
            self.conecta()
        else:
            self.conecta()
            self.inicia_base()

    def conecta(self):
        if self.__conexao is None:
            self.__conexao = sqlite3.connect(self.__nome)
            self.__cursor = self.__conexao.cursor()

    def close(self):
        self.__conexao.close()

    def inicia_base(self):
        try:
            if inicia_base_usuario(self, self.__conexao):
                if inicia_base_produto(self, self.__conexao):
                    if inicia_base_fornecedor(self, self.__conexao):
                        return True
            return False
        except sqlite3.Error as er:
            print(' Deu ruim = .Error  %s' % er)
            return False

    def getAllProdutos(self):
        try:
            return getProdutos(self, self.__conexao)
        except sqlite3.Error as er:
            print(' Deu ruim = .Error  %s' % er)
            return False

    def get5Produtos(self):
        try:
            return get5Produtos(self, self.__conexao)
        except sqlite3.Error as er:
            print(' Deu ruim = .Error  %s' % er)
            return False                  

    def getAllFornecedores(self):
        try:
            return getFornecedores(self, self.__conexao)
        except sqlite3.Error as er:
            print(' Deu ruim = .Error  %s' % er)
            return False

    def getproduto(self, cod):
        try:
            return getproduto(self, self.__conexao, cod)
        except sqlite3.Error as er:
            print(' Deu ruim = .Error  %s' % er)
            return False

    def inserir_produto(self, id_interno, nome, desc, valor, estoque):
        try:
            return insere_produto(self, self.__conexao, id_interno, nome, desc, valor, estoque)
        except sqlite3.Error as er:
            print(' Deu ruim = .Error  %s' % er)
            return False

    def deletar_produto(self, cod):
        try:
            return delete_produto(self, self.__conexao, cod)
        except sqlite3.Error as er:
            print(' Deu ruim = .Error  %s' % er)
            return False

    def deletar_fornecedor(self, cod):
        try:
            return delete_fornecedor(self, self.__conexao, cod)
        except sqlite3.Error as er:
            print(' Deu ruim = .Error  %s' % er)
            return False

    def inserir_fornecedor(self, id_interno, nome, desc):
        try:
            return insere_fornecedor(self, self.__conexao, id_interno, nome, desc)
        except sqlite3.Error as er:
            print(' Deu ruim = .Error  %s' % er)
            return False

    def executa(self, sql, valores=None):
        try:
            if valores:
                self.__cursor.execute(sql, valores)
            else:
                self.__cursor.execute(sql)

            self.__conexao.commit()
            return self.__cursor.fetchall()
        except sqlite3.Error as er:
            return False

    def executa_multiplos(self, sql, arr ):
        try:
            self.__cursor.execute(sql, arr)
            return self.__cursor.fetchall()
            return True
        except sqlite3.Error as er:
            return False