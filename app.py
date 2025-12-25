import sqlite3 as sql
from flask_cors import CORS
from flask import Flask, jsonify, request


#Flask App
app = Flask(__name__)
CORS(app)

#Default Home
@app.route("/")
def home():
    return "Server Online"

#For Reading
@app.route("/read", methods=['POST'])
def read():

    #Get queries from React
    data = request.get_json()
    limit = data.get('limit')
    gender = data.get('gender')

    #Establish connection to DB
    connection = sql.connect("dataset.db")

    cursor = connection.cursor()

    query = "SELECT * FROM customer WHERE gender LIKE " + gender + " LIMIT " + str(limit)
    result = cursor.execute(query)

    return jsonify(result.fetchall())

if __name__ == "__main__":
    app.run()