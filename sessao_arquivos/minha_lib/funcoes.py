import os
from flask import session, json

def verifica_sessao():
    retorno = None
    try:
        usu = session['usuario_logado']
        retorno = json.loads(usu)
    except KeyError:
        print(' - Não existe o índice "usuario_logado" na sessão ')
    return retorno


def arquivo_existe(caminho):
    print('* minha_lib/funcoes.py')
    if os.path.isfile(caminho):
        print('- Ok! Arquivo existe')
        return True
    else:
        print('Arquivo ainda não existe e deve ser criado')
        return False



def ler_conteudo_do_arquivo(caminho):
    print('* minha_lib/funcoes.py ler_conteudo_do_arquivo ')
    arquivo = None
    if os.path.isfile(caminho):
        print('- Ok! Arquivo existe')
    else:
        print('Arquivo ainda não existe e deve ser criado')
        arquivo = open(caminho, 'x')
        arquivo.write('Arquivo novo')
        arquivo.close()

    arquivo = open(caminho, 'r')
    str_total = ''
    for str_linha in arquivo.readlines():
        str_total += str_linha
    arquivo.close()
    return str_total

def funcao_get_dicionario(object):
    return object.__dict__
