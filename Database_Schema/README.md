# Database Schema and Mock Data

## Mock Data
Data for tables was generated using [Mockaroo](https://mockaroo.com) and [a custom Python script](generate_csv.py) to handle foreign keys
Tables that contain a mix of foreign keys, primary keys and values are generated with the "_NF" in its name to denote that it does not contain foreign keys
[Table_Name]_Data_Generated.csv are completed mock data .csv files, ready to be imported into MySQL Workbench to be populated. 

To populate tables in MySQL, open the [SQL Model](Car_Dealership_Database_Schema.mwb) and import information in the Inserts tab. 
Once all tables have been populated, select in the top bar Database -> Forward Engineer. The options "Generate separate CREATE INDEX statements" and "Generate INSERT statements for tables" should be selected. Save it as a file. An [example](Forward_Engineer_SQL.sql) is included. 
With an instance of MySQL open in MySQL Workbench, select in the side Navigator Data Import/Restore. Select Import from Self-Contained File, and select the sql file. Start import. There should be a schema present in the MySQL instance called car_dealership_database with example data populated into it, as long as "Generate INSERT statements for tables" was selected during the Forward Engineering step. 

### Mockeroo Fields
#### Customer - Generated 100 lines
| **Field Name** | **Type**                       |
|----------------|--------------------------------|
| Customer_ID    | Number, from 100000 to 999999  |
| F_Name         | First Name                     |
| M_Init         | First Name, this[1] in formula |
| L_Name         | Last Name                      |
| Email          | Email Address                  |
| Phone          | Phone                          |
| Address        | Street Address                 |
#### Task - Generated 200 lines
| **Field Name** | **Type**                             |
|-----------------|-------------------------------------|
| Task_ID         | Number, from 100000 to 999999       |
| Name            | First Name                          |
| Estd_Time       | Time, 12:00 AM to 11:59 PM, 24 Hour |
| Estd_Labor_Cost | Number, 1 to 1000, 2 decimals       |
#### Vehicle Type - Generated 20 lines
| **Field Name** | **Type**                      |
|----------------|-------------------------------|
| Vehicle_ID     | Number, from 100000 to 999999 |
| Make           | Car Make                      |
| Model          | Car Model                     |
| Year           | Car Model Year                |
| Tire_Type      | Street Suffix                 |
| Engine_Type    | Short Hex Color               |
#### Package - Generated 25 lines
| **Field_Name**      | **Type**                      |
|---------------------|-------------------------------|
| Package_ID          | Number, from 100000 to 999999 |
| Name                | Color                         |
| Time_Since_Purchase | Number, from 1 to 1000        |
#### Time Slot - Generated 100 lines
| **Field_Name** | **Type**                                |
|----------------|-----------------------------------------|
| Time_Slot_ID   | Number, from 100000 to 999999           |
| Start_Time     | Datetime, from 01/01/2022 to 12/31/2022 |
| End_Time       | Datetime, from 01/01/2023 to 12/31/2023 |
| Date           | Datetime, from 01/01/2021 to 12/31/2022 |
#### Part - Generated 500 lines
| **Field_Name** | **Type**                          |
|----------------|-----------------------------------|
| Part_ID        | Number, from 100000 to 999999     |
| Cost_Of_Part   | Number, from 1 to 100, 2 decimals |
| Name           | Currency                          |
| Task_Task_ID   | Foreign Key from table Task       |
#### Used In - Generated 500 lines
| **Field_Name**          | **Type**                            |
|-------------------------|-------------------------------------|
| Vehicle_Type_Vehicle_ID | Foreign Key from table Vehicle Type |
| Part_Part_ID            | Foreign Key from table Part         |
#### Car - Generated 500 lines
| **Field_Name**          | **Type**                                |
|-------------------------|-----------------------------------------|
| Car_ID                  | Number, from 100000 to 999999           |
| Interior                | Color                                   |
| Odometer                | Number, from 1 to 100000                |
| Color                   | Color                                   |
| License_Plate_State     | State(abbrev)                           |
| License_Plate           | Airport Region Code                     |
| Cost                    | Number, from 20000 to 40000, 2 decimals |
| Vehicle_Type_Vehicle_ID | Foreign Key from table Vehicle          |
#### Owns - Generated 500 lines
| **Field_Name**       | **Type**                        |
|----------------------|---------------------------------|
| Customer_Customer_ID | Foreign Key from table Customer |
| Car_Car_ID           | Foreign Key from table Car      |
#### Purchase - Generated 500 lines
| **Field_Name**   | **Type**                                |
|------------------|-----------------------------------------|
| Purchase_ID      | Number, from 100000 to 999999           |
| Date_Of_Purchase | Datetime, from 01/01/2022 to 12/31/2022 |
| Sale_Price       | Number, from 20000 to 40000, 2 decimals |
| Car_Car_ID       | Foreign Key from table Car              |
#### Made Purchase - Generated 500 lines
| **Field_Name**        | **Type**                        |
|-----------------------|---------------------------------|
| Customer_Customer_ID  | Foreign Key from table Customer |
| Purchase_Purchase_ID  | Foreign Key from table Purchase |

#### Appointments
TODO
#### Additionally Scheduled
TODO
#### Was Performed
TODO
#### Recommends
TODO
#### Was Replaced
TODO
#### Failure Requires
TODO