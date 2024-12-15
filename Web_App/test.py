from flask import Flask, request, render_template, jsonify
import mysql.connector
import random

# Setup connection to the database. This varies with system
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  database="Car_Dealership_Database"
)

app = Flask(__name__)

# Flask frontend implemented using render_template library
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/sale_form')
def sale_form():
  return render_template('sale_form.html')

@app.route('/add_customer_form')
def add_customer_form():
  return render_template('add_customer.html')

# Internal function to find if customer exists based on email
def find_customer(email):
  mycursor = mydb.cursor()
  mycursor.execute("""
      SELECT Customer_ID, F_Name, L_Name
      FROM Customer
      WHERE Email = %s;
  """, (email,))
  myresult = mycursor.fetchone()
  return myresult

# Internal function to check if car exists
def find_car(car_id):
  mycursor = mydb.cursor()
  mycursor.execute("""
      SELECT Car_ID
      FROM Car
      WHERE Car_ID = %s;
  """, (car_id,))
  myresult = mycursor.fetchone()
  return myresult

# API to add or update customer information if not found
@app.route('/add_customer', methods=['POST'])
def add_customer():
  data = request.json  # Expecting JSON input
  Email = data['email']
  Customer = find_customer(Email)

  if Customer is None:  # Customer does not exist, request more information
    response = {
      "message": "Customer not found. Please provide first name, last name, and other details.",
      "status": "customer_not_found"
    }
    return jsonify(response), 404
  
  response = {
    "message": "Customer already exists.",
    "customer_id": Customer[0]
  }
  return jsonify(response), 200

@app.route('/create_customer', methods=['POST'])
def create_customer():
  data = request.json  # Expecting JSON input
  F_Name = data['f_name']
  M_Init = data.get('m_init', '')
  L_Name = data['l_name']
  Email = data['email']
  Phone = data['phone']
  Address = data['address']

  Customer_ID = random.randint(100000, 999999)
  mycursor = mydb.cursor()

  mycursor.execute("""
      INSERT INTO Customer (Customer_ID, F_Name, M_Init, L_Name, Email, Phone, Address)
      VALUES (%s, %s, %s, %s, %s, %s, %s);
  """, (Customer_ID, F_Name, M_Init, L_Name, Email, Phone, Address))

  mydb.commit()
  
  response = {
    "message": "Customer created successfully.",
    "customer_id": Customer_ID
  }
  return jsonify(response), 201

# Records sale to relevant tables and junction tables
@app.route('/record_sale', methods=['POST'])
def record_sale():
  data = request.json  # Expecting JSON input
  Email = data['email']
  Car_ID = data['car_id']
  Date_Of_Purchase = data['date_of_purchase']
  Sale_Price = data['sale_price']
  License_Plate_State = data['license_plate_state']
  License_Plate = data['license_plate']

  Customer = find_customer(Email)
  if Customer is None:  # Customer does not exist, request more information
    response = {
      "message": "Customer not found. Please provide first name, last name, and other details.",
      "status": "customer_not_found"
    }
    return jsonify(response), 404
  
  Car = find_car(Car_ID)
  if Car is None:  # Car does not exist, return error
    response = {
      "message": "Car not found. Please ensure the Car ID is correct.",
      "status": "car_not_found"
    }
    return jsonify(response), 404
  
  Customer_ID = Customer[0]
  mycursor = mydb.cursor()
  try:
    Purchase_ID = random.randint(100000, 999999)

    mycursor.execute("""
        INSERT INTO Purchase (Purchase_ID, Date_Of_Purchase, Sale_Price, Car_Car_ID) 
        VALUES (%s, %s, %s, %s);
    """, (Purchase_ID, Date_Of_Purchase, Sale_Price, Car_ID))

    mycursor.execute("""
        INSERT INTO Made_Purchase (Customer_ID, Purchase_ID) 
        VALUES (%s, %s);
    """, (Customer_ID, Purchase_ID))

    mycursor.execute("""
        INSERT INTO Owns (Customer_ID, Car_ID) 
        VALUES (%s, %s);
    """, (Customer_ID, Car_ID))

    mycursor.execute("""
        UPDATE Car
        SET License_Plate_State = %s, License_Plate = %s
        WHERE Car_ID = %s;
    """, (License_Plate_State, License_Plate, Car_ID))

    mydb.commit()
  except mysql.connector.Error as err:
    mydb.rollback()
    response = {
      "message": f"An error occurred: {err}",
      "status": "error"
    }
    return jsonify(response), 500
  
  response = {
    "message": "Sale recorded successfully.",
    "purchase_id": Purchase_ID
  }
  return jsonify(response), 201

if __name__ == '__main__':
  app.run(debug=True)
