from flask import Flask
from flask import render_template
from flask import request, session
from classes.Connection import Connection
from classes.Produto import getProdutos
from classes.Produto import get5Produtos
from classes.Produto import getproduto
from classes.Login import Login

app = Flask(__name__)

app.secret_key = '12341234abc'
app.config["CACHE_TYPE"] = "null"

@app.route("/", methods = ["GET", "POST"] )
def inicial():
        con = Connection()
        if con:
            login = Login()
            user = login.getSession()
            if user:
                return render_template('home.html', user = user['name'])
            else:
                return render_template('login.html', msg = '')
        else:
            return render_template('login.html', msg = '')

@app.route("/login", methods = ["GET", "POST"] )
def login():
    login = Login()
    if request.method == "POST":
        usuario = request.form.get('inp_usuario')
        senha = request.form.get('inp_senha')
        con = Connection()
        produtos5 = con.get5Produtos()
        if login.login(usuario, senha):
            user = login.getSession()
            return render_template('home.html',  lista = produtos5, user = user['name'])
        else:
            return render_template('login.html', msg = 'Usuário ou senha incorretos!')
    else:
        return render_template('login.html', msg = 'Usuário ou senha incorretos!')    

@app.route('/home/')
def home():
    login = Login()
    user = login.getSession()
    if user:
        con = Connection()
        produtos5 = con.get5Produtos()
        return render_template('home.html', lista = produtos5, user = user['name'])
        
    else:
        return render_template('login.html', msg = 'É necessário estar logado para acessar essa tela!')

@app.route("/listP")
def list():      
    con = Connection()
    produtos = con.getAllProdutos();
    login = Login()
    user = login.getSession()
    if user:
        return render_template('lista_produtos.html', lista = produtos, user = user['name'])    
    else: 
        return render_template('lista_produtos.html', lista = produtos, user = '')    

@app.route("/listP/<cod>")
def ListP(cod=None):
    login = Login()
    user = login.getSession()
    if user:
        con = Connection()
        if con.getproduto(cod):
            produtos = con.getproduto(cod)
            return render_template('lista_produto.html', lista = produtos, user = user['name'])
        else:
            return render_template('lista_produto.html', lista = produtos, user = user['name'], msg = 'Ocorreu um problema ao buscar o Produto. Tente novamente em alguns segundos!')
    else:
        return render_template('login.html', msg = 'É necessário estar logado para acessar essa tela!')   

@app.route("/listF")
def listF():    
    login = Login()
    user = login.getSession()
    if user:
        con = Connection()
        fornecedores = con.getAllFornecedores();
        return render_template('lista_fornecedores.html', lista = fornecedores, user = user['name'])
    else:
        return render_template('login.html', msg = 'É necessário estar logado para acessar essa tela!')

@app.route("/cadastrarP")
def cadastrarP():
    login = Login()
    user = login.getSession()
    if user:
        return render_template('produtos.html', user = user['name'])
    else:
        return render_template('login.html', msg = 'É necessário estar logado para acessar essa tela!')

@app.route("/inserirP", methods = ["POST"])
def inserirP():
    login = Login()
    user = login.getSession()
    if user:
        con = Connection()
        id_interno = request.form.get('id_interno')
        nome = request.form.get('nome')
        desc = request.form.get('desc')
        valor = request.form.get('valor')
        estoque = request.form.get('estoque')
        if con.inserir_produto(id_interno, nome, desc, valor, estoque):
            produtos = con.getAllProdutos();
            return render_template('lista_produtos.html', lista = produtos, user = user['name'])
        else:
            return render_template('lista_produtos.html', lista = produtos, user = user['name'], msg = 'Ocorreu um problema ao Salvar o Produto. Tente novamente em alguns segundos!')
    else:
        return render_template('login.html', msg = 'É necessário estar logado para acessar essa tela!')

@app.route("/deleteP/<cod>")
def deleteP(cod=None):
    login = Login()
    user = login.getSession()
    if user:
        con = Connection()
        if con.deletar_produto(cod):
            produtos = con.getAllProdutos();
            return render_template('lista_produtos.html', lista = produtos, user = user['name'])
        else:
            return render_template('lista_produtos.html', lista = produtos, user = user['name'], msg = 'Ocorreu um problema ao Excluir o Produto. Tente novamente em alguns segundos!')
    else:
        return render_template('login.html', msg = 'É necessário estar logado para acessar essa tela!')

@app.route("/deleteF/<cod>")
def deleteF(cod=None):
    login = Login()
    user = login.getSession()
    if user:
        con = Connection()
        if con.deletar_fornecedor(cod):
            fornecedores = con.getAllFornecedores();
            return render_template('lista_fornecedores.html', lista = fornecedores, user = user['name'])
        else:
            return render_template('lista_fornecedores.html', lista = fornecedores, user = user['name'], msg = 'Ocorreu um problema ao Excluir o Fornecedor. Tente novamente em alguns segundos!')
    else:
        return render_template('login.html', msg = 'É necessário estar logado para acessar essa tela!')

@app.route("/inserirF", methods = ["POST"])
def inserirF():
    login = Login()
    user = login.getSession()
    if user:
        con = Connection()
        id_interno = request.form.get('id_interno')
        nome = request.form.get('nome')
        desc = request.form.get('desc')
        if con.inserir_fornecedor(id_interno, nome, desc):
            fornecedores = con.getAllFornecedores();
            return render_template('lista_fornecedores.html', lista = fornecedores, user = user['name'])
        else:
            return render_template('fornecedores.html', user = user['name'], msg = 'Ocorreu um problema ao Salvar o Fornecedor. Tente novamente em alguns segundos!')
    else:
        return render_template('login.html', msg = 'É necessário estar logado para acessar essa tela!')

@app.route("/cadastrarF")
def cadastrarF():
    login = Login()
    user = login.getSession()
    if user:
        return render_template('fornecedores.html', user = user['name'])
    else:
        return render_template('login.html', msg = 'É necessário estar logado para acessar essa tela!')
    
@app.route("/logout")
def logout():
    login = Login()
    login.logout()
    return render_template('login.html', msg= '')

app.run('127.0.0.1', 9999)
