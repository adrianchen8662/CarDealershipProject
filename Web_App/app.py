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

@app.route('/list_sales_form')
def list_sales_form():
    return render_template('list_sales.html')

@app.route('/schedule_appointment', methods=['GET'])
def schedule_appointment():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("""
        SELECT * FROM Time_Slot 
        WHERE Time_Slot_ID NOT IN (SELECT Time_Slot_Time_Slot_ID FROM Appointment)
    """)
    time_slots = mycursor.fetchall()
    return render_template('schedule_appointment.html', time_slots=time_slots)


@app.route('/appointment_details', methods=['GET'])
def appointment_details():
    return render_template('appointment_details.html')

# Internal function to find if customer exists based on email
def find_customer(email):
  mycursor = mydb.cursor()
  mycursor.execute(f"""
      SELECT Customer_ID
      FROM Customer
      WHERE email = '{email}';
  """)
  myresult = mycursor.fetchall()
  print(myresult)
  return myresult

# Application 1 API
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
      "message": "Customer not found. Redirecting to add customer form.",
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

# Application 2 API
# Schedule a new appointment. Drop off and pick up time, and packages are recorded later. Returns the generated appointment ID
@app.route("/new_appointment", methods=['GET','POST'])
def new_appointment():
  Appointment_Made_Date = request.args['appointment_made_date']
  Time_Slot_Time_Slot_ID = request.args['time_slot_time_slot_id']
  Customer_Customer_ID = find_customer(request.args['email'])
  Car_Car_ID = request.args['car_car_id']
  
  Appointment_ID = random.randint(100000, 999999)
  
  mycursor = mydb.cursor()
  mycursor.execute(f"""
      INSERT INTO Appointment (Appointment_ID, Appointment_Made_Date, Time_Slot_Time_Slot_ID, Customer_Customer_ID, Car_Car_ID)
      VALUES ('{Appointment_ID}', '{Appointment_Made_Date}', '{Time_Slot_Time_Slot_ID}', '{Customer_Customer_ID}', '{Car_Car_ID}');
  """)
  mydb.commit()
  return f"Appointment created with ID: {Appointment_ID}"
  
@app.route("/dropped_car_off", methods=['POST'])
def dropped_car_off():
  Appointment_ID = request.args['appointment_id']
  Drop_Off = request.args['drop_off']

  mycursor = mydb.cursor()
  mycursor.execute(f"""
      UPDATE Appointment
      SET Drop_Off = "{Drop_Off}"
      WHERE Appointment_ID = {Appointment_ID};
  """)
  return "Drop-Off Time Updated. "

@app.route("/picked_car_up", methods=['POST'])
def picked_car_up():
  Appointment_ID = request.args['appointment_id']
  Package_Package_ID = request.args['package_package_id']
  
  mycursor = mydb.cursor()
  mycursor.execute(f"""
      UPDATE Appointment
      SET Package_Package_ID = "{Package_Package_ID}"
      WHERE Appointment_ID = {Appointment_ID};
  """)
  return "Pick-Up Time Updated. "

@app.route("/set_package", methods=['POST'])
def set_package():
  Appointment_ID = request.args['appointment_id']
  Pick_Up = request.args['pick_up']
  
  mycursor = mydb.cursor()
  mycursor.execute(f"""
      UPDATE Appointment
      SET Pick_Up = "{Pick_Up}"
      WHERE Appointment_ID = {Appointment_ID};
  """)
  return "Package updated. "

@app.route("/generate_bill", methods=['GET'])
def generate_bill():
  Appointment_ID = request.args['appointment_id']

  mycursor = mydb.cursor()
  mycursor.execute(f"""
    SELECT a.Appointment_ID, 
        c.F_Name, c.L_Name,
        SUM(wp.Labor_Cost) AS Total_Labor_Cost,
        SUM(pt.Cost_of_Part) AS Total_Parts_Cost,
        SUM(wp.Labor_Cost) + IFNULL(SUM(pt.Cost_of_Part), 0) AS Total_Amount
    FROM Appointment a
    JOIN Customer c ON a.Customer_Customer_ID = c.Customer_ID
    LEFT JOIN Was_Performed wp ON a.Appointment_ID = wp.Appointment_Appointment_ID
    LEFT JOIN Was_Replaced wr ON a.Appointment_ID = wr.Appointment_Appointment_ID
    LEFT JOIN Part pt ON wr.Part_Part_ID = pt.Part_ID
    WHERE a.Appointment_ID = '{Appointment_ID}'
    GROUP BY a.Appointment_ID, c.F_Name, c.L_Name;
  """)
  myresult = mycursor.fetchall()
  return myresult

# Application 3 API
@app.route('/list_sales', methods=['GET'])
def list_sales():
  start_date = request.args['start_date']
  end_date = request.args['end_date']

  # MySQL Requires a time with date
  start_date = start_date + " 00:00:00"
  end_date = end_date + " 23:59:59"

  mycursor = mydb.cursor()
  mycursor.execute(f"""
      SELECT 
        VT.Make, 
        VT.Model, 
        VT.Year, 
        COUNT(P.Purchase_ID) AS Number_of_Cars_Sold, 
        ROUND(AVG(P.Sale_Price - C.Cost), 2) AS Profit_Per_Car 
      FROM 
        Purchase P 
        JOIN Car C ON P.Car_Car_ID = C.Car_ID 
        JOIN Vehicle_Type VT ON C.Vehicle_Type_Vehicle_ID = VT.Vehicle_ID 
      WHERE 
        P.Date_Of_Purchase BETWEEN '{start_date}' AND '{end_date}'
      GROUP BY 
        VT.Make, 
        VT.Model, 
        VT.Year
      ORDER BY 
        VT.Make, 
        VT.Model, 
        VT.Year;
  """)
  myresult = mycursor.fetchall()
  return myresult

if __name__ == '__main__':
  app.run(debug=True)