import pandas as pd
import collections
import glob
import random
import itertools
import os

'''
Generates Parts table using Task primary keys and a pre-existing Part_Data_Generated_NF.csv that contains all other non-foreign key data
'''
def generatePartCSV():
    print("Generating Part Table")

    task_pandas = pd.read_csv("Task_Data_Generated.csv")
    part_pandas = pd.read_csv("Part_Data_Generated_NF.csv")
    task_matrix = task_pandas[task_pandas.columns[0]]
    part_matrix = part_pandas[part_pandas.columns[0]]
    id_list = task_matrix.tolist()
    
    randomized_id_list = []
    for i in range(part_matrix.size):
        randomized_id_list.append(random.choice(id_list))
    part_pandas["Task_Task_ID"] = randomized_id_list

    part_pandas.to_csv("Part_Data_Generated.csv", index=False)

'''
Randomly combines the primary keys in Vehicle Type and Part for a given amount to generate
'''
def generateUsedInCSV(combinations_to_generate):
    print("Generating Used In Table")

    vehicle_type_pandas = pd.read_csv("Vehicle_Type_Data_Generated.csv")
    part_pandas = pd.read_csv("Part_Data_Generated.csv")
    vehicle_type_list = vehicle_type_pandas[vehicle_type_pandas.columns[0]].tolist()
    part_list = part_pandas[part_pandas.columns[0]].tolist()

    combined_keys = [(random.choice(vehicle_type_list), random.choice(part_list)) for _ in range(combinations_to_generate)]
    column_names = ["Vehicle_Type_Vehicle_ID", "Part_Part_ID"]

    pd.DataFrame(combined_keys,columns=column_names).to_csv("Used_In_Data_Generated.csv", index=False)

'''
Generates Car table using Vehicle Type primary keys and a pre-existing Car_Data_Generated_NF.csv that contains all other non-foreign key data
'''
def generateCarCSV():
    print("Generating Car Table")

    vehicle_type_pandas = pd.read_csv("Vehicle_Type_Data_Generated.csv")
    car_pandas = pd.read_csv("Car_Data_Generated_NF.csv")
    vehicle_type_matrix = vehicle_type_pandas[vehicle_type_pandas.columns[0]]
    car_matrix = car_pandas[car_pandas.columns[0]]
    id_list = vehicle_type_matrix.tolist()
    
    randomized_id_list = []
    for i in range(car_matrix.size):
        randomized_id_list.append(random.choice(id_list))
    car_pandas["Vehicle_Type_Vehicle_ID"] = randomized_id_list

    car_pandas.to_csv("Car_Data_Generated.csv", index=False)

'''
Randomly combines the primary keys in Customer and Car for a given amount to generate
'''
def generateOwnsCSV(combinations_to_generate):
    print("Generating Owns Table")

    customer_pandas = pd.read_csv("Customer_Data_Generated.csv")
    car_pandas = pd.read_csv("Car_Data_Generated.csv")
    customer_list = customer_pandas[customer_pandas.columns[0]].tolist()
    car_list = car_pandas[car_pandas.columns[0]].tolist()

    combined_keys = [(random.choice(customer_list), random.choice(car_list)) for _ in range(combinations_to_generate)]
    column_names = ["Customer_Customer_ID", "Car_Car_ID"]

    pd.DataFrame(combined_keys,columns=column_names).to_csv("Owns_Data_Generated.csv", index=False)

'''
Generates Purchase table using Car primary keys and a pre-existing Purchase_Data_Generated_NF.csv that contains all other non-foreign key data
'''
def generatePurchaseCSV():
    print("Generating Purchase Table")

    car_pandas = pd.read_csv("Car_Data_Generated.csv")
    purchase_pandas = pd.read_csv("Purchase_Data_Generated_NF.csv")
    car_matrix = car_pandas[car_pandas.columns[0]]
    purchase_matrix = purchase_pandas[purchase_pandas.columns[0]]
    id_list = car_matrix.tolist()
    
    randomized_id_list = []
    for i in range(purchase_matrix.size):
        randomized_id_list.append(random.choice(id_list))
    purchase_pandas["Car_Car_ID"] = randomized_id_list

    purchase_pandas.to_csv("Purchase_Data_Generated.csv", index=False)

'''
Randomly combines the primary keys in Customer and Purchase for a given amount to generate
'''
def generateMadePurchaseCSV(combinations_to_generate):
    print("Generating Made Purchase Table")

    customer_pandas = pd.read_csv("Customer_Data_Generated.csv")
    purchase_pandas = pd.read_csv("Purchase_Data_Generated.csv")
    customer_list = customer_pandas[customer_pandas.columns[0]].tolist()
    purchase_list = purchase_pandas[purchase_pandas.columns[0]].tolist()

    combined_keys = [(random.choice(customer_list), random.choice(purchase_list)) for _ in range(combinations_to_generate)]
    column_names = ["Customer_Customer_ID", "Purchase_Purchase_ID"]

    pd.DataFrame(combined_keys,columns=column_names).to_csv("Made_Purchase_Data_Generated.csv", index=False)

'''
Generates Appointments table using Package, Time Slot, Customer and Car primary keys and a pre-existing Appointment_Data_Generated_NF.csv that contains all other non-foreign key data
'''
def generateAppointmentCSV():
    print("Generating Appointments Table")

    appointment_pandas = pd.read_csv("Appointment_Data_Generated_NF.csv")
    purchase_matrix = appointment_pandas[appointment_pandas.columns[0]]

    randomized_id_list = []
    package_pandas = pd.read_csv("Package_Data_Generated.csv")
    package_matrix = package_pandas[package_pandas.columns[0]]
    id_list = package_matrix.tolist()
    for i in range(purchase_matrix.size):
        randomized_id_list.append(random.choice(id_list))
    appointment_pandas["Package_Package_ID"] = randomized_id_list

    randomized_id_list = []
    time_slot_pandas = pd.read_csv("Time_Slot_Data_Generated.csv")
    time_slot_matrix = time_slot_pandas[time_slot_pandas.columns[0]]
    id_list = time_slot_matrix.tolist()
    for i in range(purchase_matrix.size):
        randomized_id_list.append(random.choice(id_list))
    appointment_pandas["Time_Slot_Time_Slot_ID"] = randomized_id_list

    randomized_id_list = []
    customer_pandas = pd.read_csv("Customer_Data_Generated.csv")
    customer_matrix = customer_pandas[customer_pandas.columns[0]]
    id_list = customer_matrix.tolist()
    for i in range(purchase_matrix.size):
        randomized_id_list.append(random.choice(id_list))
    appointment_pandas["Customer_Customer_ID"] = randomized_id_list

    randomized_id_list = []
    car_pandas = pd.read_csv("Car_Data_Generated.csv")
    car_matrix = car_pandas[car_pandas.columns[0]]
    id_list = car_matrix.tolist()
    for i in range(purchase_matrix.size):
        randomized_id_list.append(random.choice(id_list))
    appointment_pandas["Car_Car_ID"] = randomized_id_list

    appointment_pandas.to_csv("Appointment_Data_Generated.csv", index=False)

'''
Randomly combines the primary keys in Appointment and Task for a given amount to generate
'''
def GenerateAdditionallyScheduledCSV(combinations_to_generate):
    print("Generating Additionally Scheduled Table")
    
    appointment_pandas = pd.read_csv("Appointment_Data_Generated.csv")
    task_pandas = pd.read_csv("Task_Data_Generated.csv")
    appointment_list = appointment_pandas[appointment_pandas.columns[0]].tolist()
    task_list = task_pandas[task_pandas.columns[0]].tolist()

    combined_keys = [(random.choice(appointment_list), random.choice(task_list)) for _ in range(combinations_to_generate)]
    column_names = ["Appointment_Appointment_ID", "Task_Task_ID"]

    pd.DataFrame(combined_keys,columns=column_names).to_csv("Addionally_Scheduled_Data_Generated.csv", index=False)

'''
Randomly combines the primary keys in Appointment and Task for a given amount to generate and a pre-existing Was_Performed_Data_Generated.csv that contains all other non-foreign key data
'''
def GenerateWasPerformedCSV(combinations_to_generate):
    print("Generating Was Performed Table")
    # TODO 
    return

'''
Randomly combines the primary keys in Appointment and Package for a given amount to generate and a pre-existing Recommends_Data_Generated_NF.csv that contains all other non-foreign key data
'''
def GenerateRecommendsCSV(combinations_to_generate):
    print("Generating Recommends Table")
    # TODO 
    return

'''
Randomly combines the primary keys in Appointment and Part for a given amount to generate
'''
def GenerateWasReplacedCSV(combinations_to_generate):
    print("Generating Was Replaced Table")

    appointment_pandas = pd.read_csv("Appointment_Data_Generated.csv")
    part_pandas = pd.read_csv("Part_Data_Generated.csv")
    appointment_list = appointment_pandas[appointment_pandas.columns[0]].tolist()
    part_list = part_pandas[part_pandas.columns[0]].tolist()

    combined_keys = [(random.choice(appointment_list), random.choice(part_list)) for _ in range(combinations_to_generate)]
    column_names = ["Appointment_Appointment_ID", "Part_Part_ID"]

    pd.DataFrame(combined_keys,columns=column_names).to_csv("Was_Replaced_Data_Generated.csv", index=False)

    return

'''
Randomly combines the primary keys for two Tasks for a given amount to generate
'''
def GenerateFailureRequiresCSV(combinations_to_generate):
    print("Generating Failure Requires Table")
    task_pandas_1 = pd.read_csv("Task_Data_Generated.cs")
    task_pandas_2 = pd.read_csv("Task_Data_Generated.csv")
    task_list_1 = task_pandas_1[task_pandas_1.columns[0]].tolist()
    task_list_2 = task_pandas_2[task_pandas_2.columns[0]].tolist()

    combined_keys = [(random.choice(task_list_1), random.choice(task_list_2)) for _ in range(combinations_to_generate)]
    column_names = ["Task_Task_ID1", "Task_Task_ID2"]

    pd.DataFrame(combined_keys,columns=column_names).to_csv("Failure_Requires_Data_Generated.csv", index=False)
    return

'''
Checks for primary key duplicates in the tables that don't contain any foreign keys to prevent issues in the future
'''
def checkIDDuplication(csv_list):
    print("Duplicate Primary Keys:")
    allowed_list = ["Customer_Data_Generated.csv",
                    "Package_Data_Generated.csv",
                    "Part_Data_Generated.csv",
                    "Part_Data_Generated_NF.csv",
                    "Task_Data_Generated.csv",
                    "Time_Slot_Data_Generated.csv",
                    "Vehicle_Type_Data_Generated.csv"]
    
    for i in csv_list:
        if i in allowed_list:
            df = pd.read_csv(i)
            matrix = df[df.columns[0]]
            id_List = matrix.tolist()
            print(i, " ", [item for item, count in collections.Counter(id_List).items() if count > 1])

if __name__ == "__main__":
    current_dir = os.getcwd()

    # Construct the path to the CSV_Files folder
    csv_folder = os.path.join(current_dir, "CSV_Files")

    # Check if the directory exists before changing to it
    if os.path.exists(csv_folder):
        os.chdir(csv_folder)
        print(f"Working directory changed to: {os.getcwd()}")
    else:
        print("Error: CSV_Files directory not found")

    print("Checking for duplicates")

    checkIDDuplication(glob.glob("*.csv"))

    print()
    print("Generating files with foreign keys")

    generatePartCSV()
    generateUsedInCSV(500)
    generateCarCSV()
    generateOwnsCSV(500)
    generatePurchaseCSV()
    generateMadePurchaseCSV(500)
    
    generateAppointmentCSV()
    GenerateAdditionallyScheduledCSV(500)
    GenerateWasPerformedCSV(500)
    GenerateRecommendsCSV(500)
    GenerateWasReplacedCSV(500)
    GenerateFailureRequiresCSV(500)

    print("CSV files successfully generated!")
    print("Import everything but _NF CSV files into the corresponding MySQL Workbench table")