import sqlite3

c = sqlite3.connect('app.db')

c.execute('DROP TABLE Post')