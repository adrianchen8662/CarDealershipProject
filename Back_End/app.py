from flask import Flask
import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  database="Car_Dealership_Database"
)


app = Flask(__name__)

@app.route('/')
def hello():
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM test")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    
    return "Hello World!"