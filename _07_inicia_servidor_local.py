from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

_usuario = ""
_senha = ""

@app.route("/")
def funcao1():
    return " Rota raiz '/' -> http://127.0.0.1:9999/ "


@app.route("/rota_2")
def funcao2():
    return " Rota 2  -> http://127.0.0.1:9999/rota_2  "


@app.route('/usuario/<nome>')
def funcao_usuario(nome):
    return 'Nome = %s' % nome  # '%s' para string


# definindo tipo dos parâmetros
@app.route('/produto/<int:codigo>')
def funcao_produto(codigo):
    return 'Código = %d' % codigo  # '%s' para int


# polimorfismo nas rotas
@app.route('/rota_template/')
@app.route('/rota_template/<parametro>')
def hello(parametro=None):
    return render_template('_07_template.html'
                           , parametro=parametro
                           , lista=['A', 'alaokba', 'sidao', 'joi'])

@app.route('/home/')
def home():
    global _usuario
    if _usuario == 'admin':
        return render_template('_07_home_user.html')
    else:
        return render_template('_07_formulario.html', msg = 'Usuário ou senha inválidos')

@app.route("/login", methods = ["GET", "POST"] )
def login():
    print(  request.method  )
    if request.method == "POST": # quer dizer que veio do FORM
        print("0")
        global _usuario 
        _usuario = request.form.get('inp_usuario') # form quando vem do <form>
        global _senha   
        _senha = request.args.get('inp_senha')   # args só funciona quando parâmetro vem da URL
        print(_usuario)
        if _usuario == 'admin':
            print("1")
            return render_template('_07_home_user.html')
        else:
            print("2")
            return render_template('_07_formulario.html', msg = 'Usuário ou senha inválidos')
    else:
        print("3")
        return render_template('_07_formulario.html', msg = '---')


@app.route("/list", methods = ["GET", "POST"] )
def list():    
    global _usuario
    if _usuario == 'admin':
        return render_template('lista_produtos.html', lista = [{
            'id': '1',
            'name':'Produto 1' ,
            'value':'10',
            'stock':'5'
        },{
            'id': '2',
            'name':'Produto 2' ,
            'value':'10',
            'stock':'5'
        },{
            'id': '3',
            'name':'Produto 3' ,
            'value':'10',
            'stock':'5'
        },{
            'id': '4',
            'name':'Produto 4' ,
            'value':'10',
            'stock':'5'
        }
        ])
    else:
        return render_template('_07_formulario.html', msg = 'Usuário ou senha inválidos')
    
@app.route("/logout")
def logout():
    global _usuario 
    global _senha 
    _usuario = ""
    _senha = ""
    return render_template('_07_formulario.html')

app.run('127.0.0.1', 9999)
