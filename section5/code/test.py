import sqlite3
from user import User
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

users = [(1,'bob', 'asdf'), (2,'alice', 'asdf'),(3,'cherry', 'asdf')]
create_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text)"
cursor.execute(create_table)

insert_table = "INSERT INTO users values(?,?,?)"
cursor.executemany(insert_table,users)


select_query = "SELECT * FROM users"
connection.commit()
connection.close()
