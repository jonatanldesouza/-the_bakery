from flask import Flask, render_template, session, json, request
import os
from minha_lib.Conexao   import Conexao
from minha_lib.Produto   import Produto

from minha_lib.PessoaDao import PessoaDao
from minha_lib.Pessoa    import Pessoa
from minha_lib.funcoes   import funcao_get_dicionario
from minha_lib.funcoes   import verifica_sessao

app = Flask(__name__)

app.secret_key = '12341234abc'
app.config["CACHE_TYPE"] = "null"


@app.route('/teste_conexao_sqlite')
def teste_conexao_sqlite():
    str = '<h3>teste_conexao_sqlite<h3>'
    con = Conexao()
    return str


@app.route('/teste_produto_sqlite')
def teste_produto_sqlite():
    str = '<h3>teste_produto_sqlite<h3>'
    pr = Produto()
    print(' * /teste_produto_sqlite pr.buscar(1) = ', pr.buscar(1))
    pr.descri = "Novo conteúdo"
    pr.salva()
    print(' * /teste_produto_sqlite codseq 2  = ', pr.nompro)

    # for linha in fetchall():
    #     print(linha)

    return str


@app.route('/')
@app.route('/produtos')
def produtos():
    usuario = verifica_sessao()
    if usuario is not None:
        return render_template('home.html', usuario=usuario)
    else:
        return render_template('login.html')


@app.route('/carrinho')
def carrinho():
    usuario = verifica_sessao()
    if usuario is not None:
        return render_template('home.html', usuario=usuario)
    else:
        return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('/login => Veio com POST')
        # request.args.get('') URL e GET
        # request.form.get('') POST
        email = request.form.get('imput_email')  # form quando vem do <form>
        senha = request.form.get('imput_senha')  # args só funciona quando parâmetro vem da URL
        print(' - email = ', email)
        print(' - senha = ', senha)
        pes = PessoaDao()
        pes = pes.login(senha, email)
        if pes is not None:
            session['usuario_logado'] = json.dumps(pes)
        else:
            print('Usuário ou senha inválidos')
        # * * *  - Aqui deve se realizar teste com os dados recebidos e investigar o TXT - * *
        # inicar um LIB para guardar as classe e funções para manuseio de sessão e arquivos
    else:
        print('/login => Veio por Get, sem parametro')

    usu = None
    try:
        usu = session['usuario_logado']
        print(usu)
        usu = json.loads(usu)
        print(' - Ok, sessão tem o índice "usuario_logado" ')
        return render_template('home.html', usuario=usu)
    except KeyError:
        print(' - Não existe o índice "usuario_logado" na sessão ')
        return render_template('login.html')


@app.route('/sair')
def sair():
    print('/sair')
    try:
        del session['usuario_logado']
        print(' - Ok, sessão removida "usuario_logado" ')
    except KeyError:
        print(' - Ok, sessão "usuario_logado" não existe!')

    return render_template('login.html')



@app.route('/usuarios')
def home():
    usuario_logado = verifica_sessao()
    if usuario_logado is not None:
        dao_pes = PessoaDao()
        return render_template('usuarios_lista_normal.html'
                               , usuario=usuario_logado
                               , array_usuarios=dao_pes.lista())
    else:
        return render_template('login.html')


@app.route('/usuarios_ajax')
def usuarios_com_ajax():
    usuario_logado = verifica_sessao()
    if usuario_logado is not None:
        return render_template('usuarios_lista_com_ajax.html'
                               , usuario=usuario_logado)
    else:
        return render_template('login.html')




@app.route('/ajax/get_lista_usuarios/')
def get_lista_usuarios():
    imp_pes = request.args.get('imp_pes')
    #print(request)
    print(' * - /ajax/get_lista_usuarios/ imp_pes = ', imp_pes)
    usuario_logado = verifica_sessao()
    if usuario_logado is not None:
        arr = PessoaDao.lista(imp_pes)
        jso = json.dumps(arr
                         , default=Pessoa.metodo_dinamico_get_dicionario)
        return jso
    else:
        return ''




@app.route('/teste')
def teste():
    p = Pessoa()
    print('\np = ', p)
    print('\nPessoa 1 = ', json.dumps(p, default=funcao_get_dicionario))
    p = Pessoa('Marcelo Fey')
    print('\nPessoa 2 = ', json.dumps(p, default=Pessoa.metodo_dinamico_get_dicionario))
    print('\nPessoa 3 = ', Pessoa)
    print('\np = ', p)
    print('\nPessoa.metodo_estatico = ', Pessoa.metodo_estatico)
    print('\np.metodo_estatico = ', p.metodo_estatico)
    print('\np.metodo_dinamico = ', p.metodo_dinamico)
    print('\nPessoa.metodo_estatico(AAAA) = ', Pessoa.metodo_estatico('AAAA'))
    print('\np.metodo_estatico(BBBB) = ', p.metodo_estatico('BBBB'))
    print('\np.metodo_dinamico(1234) = ', p.metodo_dinamico('1234'))
    return '....Teste....'

app.run()
