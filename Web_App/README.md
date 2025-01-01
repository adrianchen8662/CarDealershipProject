# Car Dealership Project Backend
The application is a web application developed in Python using the Flask repository, and some of its associated features. The webapp is not configured to be deployed in production environment, and thus will have a warning saying it’s a development server. Connecting to the database, and the secret key necessary for some of the CSS/Javascripting to work are also temporary, and should definitely not be kept in the main python file in an actual deployment. For a final project, however, I thought it would be fine to leave in. 
You will need to install the Flask and MySQL Connector libraries for this application to work. Flask handles the backend REST API calls along with the HTML rendering, while MySQL handles the SQL queries to the MySQL database instance. 
Pages are created using HTML and some Javascript/CSS where appropriate, such as styling and allowing for notifications or auto-populating fields, such as the time slot. 

**Application 1**

This application is rendered using sale_form.html and add_customer_form.html. It didn’t make sense to have each sale form reference the customer by the primary key, so a separate helper call is made to check if the customer exists. If not, it redirects to the add_customer_form to allow for a customer to be added. It can then go back to the sale form the complete the purchase. 

**Application 2**

This application is rendered using schedule_appointment.html, appointment_details.thml and bill_details.html. An appointment can be scheduled through schedule_appointment. This also is able to figure out what package is needed based on the time period of the car being requested. Appointment Details is meant for the service member at the dealership to log drop-off, pick-up and package details to add to the car. Appointment Details also contains the ability to print the receipt in Bill Details. 

**Application 3**

This application queries the database to pull up sales done in a certain time period. It sorts by the Make, Model then Year. 

## Dependencies
mysql-connector-python
flask

These can be installed using pip, i.e. <strong>pip install flask</strong> or <strong>pip install mysql-connector-python</strong>

## How to Run
The Webapp can be started typing py app.py in the Web_App directory
Once the application has started, navigate to http://127.0.0.1:5000 on your browser to access the application. 

There are four buttons:
Record New Sale - Application 1
    This allows for a salesperson or manager to record the sale of a car to a customer. If the customer email is not recognized, the customer's information will be asked to be added. 

Maintenance - Application 2
    This is the first part of Application 2 where customers can schedule for an appointment and pick a time slot that works for them. The time slots were generated to be a year long, so the dropdown menu contains a lot of entries. 

Appointment Details - Application 2
    This is the second part of Application 2 that allows for the dealership mechanics to log drop-off times, pick-up times, packages to add to a car, and to generate a bill. 

View Sales Report - Application 3
    This shows the sales based on a start and end date. Data has only been populated for the years 2022 to 2023, so anything selected outside of those bounds will show no sales. 

## HTML Templates
/ - index.html
/sale_form - sale_form.html
/add_customer_form - add_customer.html. Not directly accessed, but accessed through /sale_form
/list_sales_form - list_sales.html
/schedule_appointment - schedule_appointment.html
/appointment_details - appointment_details.html
/bill_details - bill_details.html. Not directly accessed, but accessed through /appointment_details

## Internal Functions
find_customer(email)
find_customer_by_car(car_id)
find_car(car_id)

## API
### Application 1
/add_customer

/create_customer

/get_time_slots

/record_sale


### Application 2
/new_appointment", methods=['GET','POST']

/dropped_car_off, methods=['POST']

/picked_car_up, methods=['POST']

/set_package, methods=['POST']

/generate_bill, methods=["GET"]


### Application 3
/list_sales, methods=['GET']
