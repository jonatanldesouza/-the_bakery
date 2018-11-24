
class Pessoa:

    nome = ''

    # Método Construtor, sempre acontece quando iniciamos uma instância
    def __init__(self, par_nom=''):
        self.nome = par_nom
        print('* Pessoa.__init__() nom = (', par_nom, ')\n')

    def metodo_dinamico(sefl, parametro):
        print('* Pessoa.metodo_estatico() sefl = ', sefl)
        print('- Pessoa.metodo_estatico() parametro = ', parametro, '\n')
        return None

    def metodo_dinamico_get_dicionario(sefl):
        print(' * Pessoa.metodo_dinamico_get_dicionario() sefl = ', sefl.__dict__)
        return sefl.__dict__

    # Métodos estáticos sem o self
    @staticmethod
    def sql_create():
        return
        """
            CREATE TABLE tb_....
            ); 
        """
        #  SQLite Foreign Key Support - https://www.sqlite.org/foreignkeys.html , FOREIGN KEY(..) REFERENCES artist(..)

