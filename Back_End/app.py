from flask import Flask, request
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

@app.route('/')
def main():
  return "Hello World!"

# Internal function to find if customer exists based on email
def find_customer(email):
  mycursor = mydb.cursor()
  mycursor.execute(f"""
      SELECT Customer_ID
      FROM Customer
      WHERE email = '{email}';
  """)
  myresult = mycursor.fetchall()
  return myresult

# Application 1 API
# If customer exists based on email, use Customer_ID and update information. Else, generate a new Customer_ID
@app.route('/add_customer', methods = ['GET','POST'])
def add_customer():
  
  F_Name = request.args['f_name']
  M_Init = request.args['m_init']
  L_Name = request.args['l_name']
  Email = request.args['email']
  Phone = request.args['phone']
  Address = request.args['address']

  
  if not find_customer(Email):
    print("No Customer Found")
    Customer_ID = random.randint(100000,999999)
  else:
    print("Customer Found")
    Customer_ID = find_customer(Email)[0]
  
  Customer_ID = random.randint(100000,999999)
  mycursor = mydb.cursor()

  mycursor.execute(f"""
      INSERT INTO Customer(Customer_ID,F_Name,M_Init,L_Name,Email,Phone,Address)
      VALUES (
          {Customer_ID},
          '{F_Name}',
          '{M_Init}',
          '{L_Name}',
          '{Email}',
          '{Phone}',
          '{Address}'
      );
  """)
  return str(Customer_ID)

# Records sale to relevant tables and junction tables
@app.route('/record_sale', methods=['GET','POST'])
def record_sale():
  Customer_ID = request.args['customer_id']
  Car_ID = request.args['car_id']
  Date_Of_Purchase = request.args['date_of_purchase']
  Sale_Price = request.args['sale_price']
  License_Plate_State = request.args['license_plate_state']
  License_Plate = request.args['license_plate']

  mycursor = mydb.cursor()

  Purchase_ID = random.randint(100000,999999)

  # Insert for Purchase Table
  mycursor.execute(f"""
      INSERT INTO Purchase(Purchase_ID, Date_Of_Purchase, Sale_Price, Car_Car_ID) 
      VALUES (
          {Purchase_ID}
          '{Date_Of_Purchase}', 
          {Sale_Price}, 
          {Car_ID},
      );
  """)

  # Insert for Made Purchase Junction Table
  mycursor.execute(f"""
      INSERT INTO Made_Purchase(Purchase_ID, Date_Of_Purchase, Sale_Price, Car_Car_ID) 
      VALUES (
          {Customer_ID},
          {Purchase_ID}
      );
  """)
  # Insert for Owns Junction Table
  mycursor.execute(f"""
      INSERT INTO Owns(Purchase_ID, Date_Of_Purchase, Sale_Price, Car_Car_ID) 
      VALUES (
          {Customer_ID},
          {Car_ID}
      );
  """)

  # Update for Car Table (assuming that a License Plate_State and License_Plate are added at time of purchase)
  mycursor.execute(f"""
      UPDATE Car
      SET License_Plate_State = '{License_Plate_State}', License_Plate = '{License_Plate}'
      WHERE Car_ID = {Car_ID};
  """)

  return str(Purchase_ID)

# Application 2 API
# Schedule a new appointment. Drop off and pick up time, and packages are recorded later. Returns the generated appointment ID
@app.route("/new_appointment", methods=['GET','POST'])
def new_appointment():
  Appointment_Made_Date = request.args['appointment_made_date']
  Time_Slot_Time_Slot_ID = request.args['time_slot_time_slot_id']
  Customer_Customer_ID = find_customer(request.args['email'])
  Car_Car_ID = request.args['car_car_id']
  
  Appointment_ID  = random.randint(100000,999999)

  mycursor = mydb.cursor()
  mycursor.execute(f"""
      INSERT INTO Appointment (Appointment_ID, Appointment_Made_Date, Time_Slot_Time_Slot_ID, Customer_Customer_ID, Car_Car_ID)
      VALUES ('{Appointment_ID}', '{Appointment_Made_Date}', '{Time_Slot_Time_Slot_ID}', '{Customer_Customer_ID}', '{Car_Car_ID}');
  """)

  return Appointment_ID
  
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