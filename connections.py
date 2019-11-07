#Sqlite module for saving data
import sqlite3

#Class For accessing sqlite database
class Database():
    user_name = ''
    pass_word = ''

    def __init__(self, us, passw):
        self.user_name = us
        self.pass_word = passw

    def getuser_name(self):
        return self.user_name

    def getpass_word(self):
        return self.pass_word

    def setuser_name(self, us):
        self.user_name = us

    def setpass_word(self, passw):
        self.pass_word = passw

    #Function for logging in/registering for sqlite database: master.db
    def welcome(self):
        conn = sqlite3.connect('master.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS users(
        username text,
        password text)''')

        c.execute("INSERT INTO users VALUES(?,?)",(self.user_name, self.pass_word))

        c.execute("SELECT* FROM users WHERE username=? and password=?", (self.user_name, self.pass_word))
        results = c.fetchall()

        if results:
            for a in results:
                print(a[0])

        conn.commit()
        conn.close()

    def register(self):
        conn = sqlite3.connect('master.db')
        c = conn.cursor()

        c.execute("INSERT INTO users VALUES(?,?)", (self.user_name, self.pass_word))
        

        conn.commit()
        conn.close()
