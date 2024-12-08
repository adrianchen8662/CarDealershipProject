# Database Schema and Mock Data

## Mock Data
Data for tables was generated using [Mockaroo](mockaroo.com) and custom Python scripts to handle foreign keys
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
| **Field Name** | **Type**                      |
|----------------|-------------------------------|
| Vehicle_ID     | Number, from 100000 to 999999 |
| Make           | Car Make                      |
| Model          | Car Model                     |
| Year           | Car Model Year                |
| Tire_Type      | Street Suffix                 |
| Engine_Type    | Short Hex Color               |
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
#### Time Slot
| Field_Name   | Type                                    |
|--------------|-----------------------------------------|
| Time_Slot_ID | Number, from 100000 to 999999           |
| Start_Time   | Datetime, from 01/01/2022 to 12/31/2022 |
| End_Time     | Datetime, from 01/01/2023 to 12/31/2023 |
| Date         | Datetime, from 01/01/2021 to 12/31/2022 |