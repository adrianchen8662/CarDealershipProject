from flask import Flask
import mysql.connector

'''
mydb = mysql.connector.connect(
  host="your_database_host",
  user="your_username",
  password="your_password",
  database="your_database_name"
)
'''

app = Flask(__name__)

@app.route('/')
def hello():
    '''
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM your_table_name")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    '''
    return "Hello World!"