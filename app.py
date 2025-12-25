import sqlite3 as sql
from flask_cors import CORS
from flask import Flask, jsonify, render_template


#Flask App
app = Flask(__name__)
CORS(app)

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

    return jsonify(result.fetchall())

if __name__ == "__main__":
    app.run()