import sqlite3
from classes.utils import arquivo_existe
from flask import session, json
from classes.Connection import Connection

class Login(Connection):

    def login(self, username, password):
      if username and password: 
        user = self.getUsers(username, password)
        if user:
            session['user_session'] = json.dumps({'user': {'cod': user[0][0], 'name': user[0][1], 'email': user[0][2]}})
            return True
      else:
        return False


    def getUsers(self, username, password):
        try:
            rs = self.executa("SELECT cod, name, email FROM usuario WHERE email = ? and senha = ?", (username, password,))
            return rs
        except sqlite3.Error as er:
            print(' Erro ao consultar usuários - Error  %s' % er)
            return []

    def getSession(self):
      try:
          sessionUser = session['user_session']
          if sessionUser:
            return json.loads(sessionUser)['user']
          else:
            return False
      except KeyError as er:
          return False

    def logout(self):
        try:
          sessionUser = session['user_session']
          if sessionUser:
            del session['user_session']
          else:
            return False
        except KeyError as er:
          return False