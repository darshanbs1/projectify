import sqlite3

connection=sqlite3.connect("users_data.db")
cursor=connection.cursor()
command1="""CREATE TABLE IF NOT EXISTS users(name TEXT NOT NULL PRIMARY KEY, email TEXT, password TEXT)"""
cursor.execute(command1)
command2="""CREATE TABLE IF NOT EXISTS events(EventName TEXT, link1 TEXT,link2 TEXT)"""
cursor.execute(command2)

connection.commit()