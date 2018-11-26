import os

from mylib.connect_db import conn
from flask import json


class Produto(conn):
    codpro = ''
    nompro = ''

    def __init__(self, codpro='', nome='', deposito='', quantidadeEstoque='',  quantidadeMinima='', quantidadeMaxima='', criado_em=''):
        super().__init__()  # de Conexao
        self.codpro = codpro
        self.nome = nome
        self.deposito = deposito
        self.quantidadeEstoque = quantidadeEstoque
        self.quantidadeMinima = quantidadeMinima
        self.quantidadeMaxima = quantidadeMaxima
        self.criado_em = criado_em
        print('* Produto.__init__() (', self.codpro, ')\n')

    def cadastrar(self):

        p_nome = input('Nome: ')
        p_deposito = input('deposito: ')
        p_QtdEst= input('Estoque: ')
        p_QtdMax = input('Estoque Maximo: ')
        p_QtdMin = input('Estoque Minimo: ')
        p_criado_em = input('Criado em (yyyy-mm-dd): ')

        self.execute("""
        INSERT INTO produtos (nome, deposito, quantidadeEstoque, quantidadeMinima, quantidadeMaxima, criado_em)
        VALUES (?,?,?,?,?,?,?,?)
        """, (p_nome, p_deposito, p_QtdEst, p_QtdMax, p_QtdMin, p_criado_em))

        conn.commit()

        print('Dados inseridos com sucesso.')

        conn.close()
