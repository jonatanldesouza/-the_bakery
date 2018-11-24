from minha_lib.Conexao import Conexao
from flask import json


class Produto(Conexao):
    codseq = ''
    nompro = ''
    descri = ''
    sigsku = ''

    # Método Construtor, sempre acontece quando iniciamos uma instância
    def __init__(self, codseq='', nompro='', descri='', sigsku='' ):
        super().__init__()  # de Conexao
        self.codseq = codseq
        self.nompro = nompro
        self.descri = descri
        self.sigsku = sigsku
        print('* Produto.__init__() (', self.codseq, ')\n')

    def buscar(self, codseq):
        self.codseq = codseq
        print('* Produto.buscar() codseq = ', self.codseq)
        rs = self.executa(
            """
            SELECT * FROM  tb_produto WHERE pr_codseq = ?
            """, (codseq,))
        print('- Produto.buscar() len(rs) = ', len(rs))
        if len(rs) == 0:
            if self.nompro == '': self.nompro = 'Produto %s ' % self.codseq
            self.executa_multiplos(
                """
                INSERT INTO tb_produto VALUES( ?, ?, ?, ? )
                """, (self.codseq, self.nompro, self.descri, self.sigsku))
            rs = self.executa(
                """
                SELECT * FROM  tb_produto WHERE pr_codseq = ?
                """, (codseq,))

        print('- Produto.buscar() rs = ', rs);
        self.codseq = rs[0][0]
        self.nompro = rs[0][1]
        self.descri = rs[0][2]
        self.sigsku = rs[0][3]
        return self

    def salvar(self):
        print('* Produto.salvar() self = ', self)

        return None

    def get_dicionario(self):
        print(' * Produto.get_dicionario() self = ', self.__dict__)
        return self.__dict__


