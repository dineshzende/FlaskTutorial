import sqlite3
from user import User
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

users = [(1,'bob', 'asdf'), (2,'alice', 'asdf'),(3,'cherry', 'asdf')]
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name str, price real)"
cursor.execute(create_table)

#cursor.execute("INSERT INTO items VALUES('chair', 10.99)")

connection.commit()
connection.close()



