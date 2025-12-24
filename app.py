import sqlite3 as sql
from flask import Flask, render_template


#Flask App
app = Flask(__name__)

@app.route("/")
def home():

    #Establish connection to DB
    connection = sql.connect("testDB.db")

    cursor = connection.cursor()

    query = input() 
    result = cursor.execute(query)

    return result.fetchall()

if __name__ == "__main__":
    app.run()