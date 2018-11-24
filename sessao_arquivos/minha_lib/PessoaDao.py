from minha_lib.Pessoa import Pessoa
from minha_lib.funcoes import ler_conteudo_do_arquivo
from flask import json


class PessoaDao:

    @staticmethod
    def metodo_estatico(qualquer_valor):
        print('* Pessoa.metodo_estatico() qualquer_valor = ', qualquer_valor, '\n')
        return None

    @staticmethod
    def login(senha, email):
        teste = None
        str_pessoas = ler_conteudo_do_arquivo('pessoas.json')
        print(str_pessoas)
        array_pessoas = json.loads(str_pessoas)
        print(type(array_pessoas))
        for pes in array_pessoas:
            print(pes['email'])
            if email == pes['email'] and senha == pes['senha']:
                teste = pes
        return teste

    @staticmethod
    def lista(filtro_nome=''):
        str_pessoas = ler_conteudo_do_arquivo('pessoas.json')
        array_pessoas = json.loads(str_pessoas)
        arr_retorno = []
        for p in array_pessoas:
            print(p['nome'] , '=?=', filtro_nome)
            # atividade verificar parte da palavra
            if filtro_nome == p['nome'] or filtro_nome=='':
                # arr_retorno[len(array_pessoas)] = pessoa
                arr_retorno.append(p)

        return arr_retorno
