import sqlite3 as sql
from flask import Flask, render_template


#Flask App
app = Flask(__name__)

#Default Home
@app.route("/")
def home():
    return "Server Online"

#For Reading
@app.route("/read")
def read():

    #Establish connection to DB
    connection = sql.connect("dataset.db")

    cursor = connection.cursor()

    query = "SELECT * FROM customer LIMIT 10;"
    result = cursor.execute(query)

    return result.fetchall()

if __name__ == "__main__":
    app.run()