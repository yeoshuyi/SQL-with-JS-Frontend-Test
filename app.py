import sqlite3 as sql

connection = sql.connect("testDB.db")

cursor = connection.cursor()

while(True):
    query = input() 
    result = cursor.execute(query)
    print(result.fetchall())

    