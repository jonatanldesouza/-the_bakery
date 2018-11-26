import sqlite3

def inicia_base_usuario(self, con):
    try:
        con.execute(
            """
            CREATE TABLE usuario (
                cod INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL
            );
            """)
        con.commit()
        print('Criou Table Usuário')
        
        return insere_usuario_admin(self, con)

    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False

def insere_usuario_admin(self, con):
    try:
        self.executa_multiplos(
            """
            INSERT INTO usuario VALUES( ?, ?, ?, ? )
            """, (1, "Admin", "admin", "admin"))
        con.commit()
        print('Criou User - Admin')
        return True
    except sqlite3.Error as er:
        print(' Deu ruim = .Error  %s' % er)
        return False