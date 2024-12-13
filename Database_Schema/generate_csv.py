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
    
    # Load vehicle type and part data from CSV files
    vehicle_type_pandas = pd.read_csv("Vehicle_Type_Data_Generated.csv")
    part_pandas = pd.read_csv("Part_Data_Generated.csv")
    
    # Extract vehicle type and part IDs into lists
    vehicle_type_list = vehicle_type_pandas[vehicle_type_pandas.columns[0]].tolist()
    part_list = part_pandas[part_pandas.columns[0]].tolist()
    
    # Generate unique combinations of vehicle type IDs and part IDs
    combined_keys = set()
    
    while len(combined_keys) < combinations_to_generate:
        vehicle_type_id = random.choice(vehicle_type_list)
        part_id = random.choice(part_list)
        combined_keys.add((vehicle_type_id, part_id))
    
    # Convert the set of unique combinations to a DataFrame
    column_names = ["Vehicle_Type_Vehicle_ID", "Part_Part_ID"]
    combined_keys_list = list(combined_keys)
    
    pd.DataFrame(combined_keys_list, columns=column_names).to_csv("Used_In_Data_Generated.csv", index=False)

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
    
    # Load customer and car data from CSV files
    customer_pandas = pd.read_csv("Customer_Data_Generated.csv")
    car_pandas = pd.read_csv("Car_Data_Generated.csv")
    
    # Extract customer and car IDs into lists
    customer_list = customer_pandas[customer_pandas.columns[0]].tolist()
    car_list = car_pandas[car_pandas.columns[0]].tolist()
    
    # Generate unique combinations of customer IDs and car IDs
    combined_keys = set()
    
    while len(combined_keys) < combinations_to_generate:
        customer_id = random.choice(customer_list)
        car_id = random.choice(car_list)
        combined_keys.add((customer_id, car_id))
    
    # Convert the set of unique combinations to a DataFrame
    column_names = ["Customer_Customer_ID", "Car_Car_ID"]
    combined_keys_list = list(combined_keys)
    
    pd.DataFrame(combined_keys_list, columns=column_names).to_csv("Owns_Data_Generated.csv", index=False)

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
    
    # Load customer and purchase data from CSV files
    customer_pandas = pd.read_csv("Customer_Data_Generated.csv")
    purchase_pandas = pd.read_csv("Purchase_Data_Generated.csv")
    
    # Extract customer and purchase IDs into lists
    customer_list = customer_pandas[customer_pandas.columns[0]].tolist()
    purchase_list = purchase_pandas[purchase_pandas.columns[0]].tolist()
    
    # Generate unique combinations of customer IDs and purchase IDs
    combined_keys = set()
    
    while len(combined_keys) < combinations_to_generate:
        customer_id = random.choice(customer_list)
        purchase_id = random.choice(purchase_list)
        combined_keys.add((customer_id, purchase_id))
    
    # Convert the set of unique combinations to a DataFrame
    column_names = ["Customer_Customer_ID", "Purchase_Purchase_ID"]
    combined_keys_list = list(combined_keys)
    
    pd.DataFrame(combined_keys_list, columns=column_names).to_csv("Made_Purchase_Data_Generated.csv", index=False)


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
    
    # Load appointment and task data from CSV files
    appointment_pandas = pd.read_csv("Appointment_Data_Generated.csv")
    task_pandas = pd.read_csv("Task_Data_Generated.csv")
    
    # Extract appointment and task IDs into lists
    appointment_list = appointment_pandas[appointment_pandas.columns[0]].tolist()
    task_list = task_pandas[task_pandas.columns[0]].tolist()
    
    # Generate unique combinations of appointment IDs and task IDs
    combined_keys = set()
    
    while len(combined_keys) < combinations_to_generate:
        appointment_id = random.choice(appointment_list)
        task_id = random.choice(task_list)
        combined_keys.add((appointment_id, task_id))
    
    # Convert the set of unique combinations to a DataFrame
    column_names = ["Appointment_Appointment_ID", "Task_Task_ID"]
    combined_keys_list = list(combined_keys)
    
    pd.DataFrame(combined_keys_list, columns=column_names).to_csv("Additionally_Scheduled_Data_Generated.csv", index=False)

'''
Randomly combines the primary keys in Appointment and Task for a given amount to generate and a pre-existing Was_Performed_Data_Generated.csv that contains all other non-foreign key data
'''
def GenerateWasPerformedCSV(combinations_to_generate):
    print("Generating Was Performed Table")
    appointment_pandas = pd.read_csv("Appointment_Data_Generated.csv")
    task_pandas = pd.read_csv("Task_Data_Generated.csv")
    was_performed_pandas = pd.read_csv("Was_Performed_Data_Generated_NF.csv")
    appointment_matrix = appointment_pandas[appointment_pandas.columns[0]]
    task_matrix = task_pandas[task_pandas.columns[0]]
    was_performed_matrix = was_performed_pandas[was_performed_pandas.columns[0]]
    
    appointment_id_list = appointment_matrix.tolist()
    task_id_list = task_matrix.tolist()
    
    # Track used combinations to ensure uniqueness
    used_combinations = set()
    appointment_randomized_list = []
    task_randomized_list = []
    
    for _ in range(was_performed_matrix.size):
        while True:
            appointment_id = random.choice(appointment_id_list)
            task_id = random.choice(task_id_list)
            combination = (appointment_id, task_id)
            
            if combination not in used_combinations:  # Ensure the combination is unique
                used_combinations.add(combination)
                appointment_randomized_list.append(appointment_id)
                task_randomized_list.append(task_id)
                break  # Break the loop once a unique combination is found
    
    was_performed_pandas["Appointment_Appointment_ID"] = appointment_randomized_list
    was_performed_pandas["Task_Task_ID"] = task_randomized_list

    was_performed_pandas.to_csv("Was_Performed_Data_Generated.csv", index=False)

'''
Randomly combines the primary keys in Appointment and Package for a given amount to generate and a pre-existing Recommends_Data_Generated_NF.csv that contains all other non-foreign key data
'''
def GenerateRecommendsCSV(combinations_to_generate):
    print("Generating Recommends Table")
    package_pandas = pd.read_csv("Package_Data_Generated.csv")
    task_pandas = pd.read_csv("Task_Data_Generated.csv")
    recommends_pandas = pd.read_csv("Recommends_Data_Generated_NF.csv")
    package_matrix = package_pandas[package_pandas.columns[0]]
    task_matrix = task_pandas[task_pandas.columns[0]]
    recommends_matrix = recommends_pandas[recommends_pandas.columns[0]]
    
    package_id_list = package_matrix.tolist()
    task_id_list = task_matrix.tolist()
    
    # Track used combinations to ensure uniqueness
    used_combinations = set()
    package_randomized_list = []
    task_randomized_list = []
    
    for _ in range(recommends_matrix.size):
        while True:
            package_id = random.choice(package_id_list)
            task_id = random.choice(task_id_list)
            combination = (package_id, task_id)
            
            if combination not in used_combinations:  # Ensure the combination is unique
                used_combinations.add(combination)
                package_randomized_list.append(package_id)
                task_randomized_list.append(task_id)
                break  # Break the loop once a unique combination is found
    
    recommends_pandas["Package_Package_ID"] = package_randomized_list
    recommends_pandas["Task_Task_ID"] = task_randomized_list

    recommends_pandas.to_csv("Recommends_Data_Generated.csv", index=False)

'''
Randomly combines the primary keys in Appointment and Part for a given amount to generate
'''
def GenerateWasReplacedCSV(combinations_to_generate):
    print("Generating Was Replaced Table")
    
    # Load appointment and part data from CSV files
    appointment_pandas = pd.read_csv("Appointment_Data_Generated.csv")
    part_pandas = pd.read_csv("Part_Data_Generated.csv")
    
    # Extract appointment and part IDs into lists
    appointment_list = appointment_pandas[appointment_pandas.columns[0]].tolist()
    part_list = part_pandas[part_pandas.columns[0]].tolist()
    
    # Generate unique combinations of appointment IDs and part IDs
    combined_keys = set()
    
    while len(combined_keys) < combinations_to_generate:
        appointment_id = random.choice(appointment_list)
        part_id = random.choice(part_list)
        combined_keys.add((appointment_id, part_id))
    
    # Convert the set of unique combinations to a DataFrame
    column_names = ["Appointment_Appointment_ID", "Part_Part_ID"]
    combined_keys_list = list(combined_keys)
    
    pd.DataFrame(combined_keys_list, columns=column_names).to_csv("Was_Replaced_Data_Generated.csv", index=False)

'''
Randomly combines the primary keys for two Tasks for a given amount to generate
'''
def GenerateFailureRequiresCSV(combinations_to_generate):
    print("Generating Failure Requires Table")
    
    # Load task data from CSV files
    task_pandas_1 = pd.read_csv("Task_Data_Generated.csv")
    task_pandas_2 = pd.read_csv("Task_Data_Generated.csv")
    
    # Extract task IDs into lists
    task_list_1 = task_pandas_1[task_pandas_1.columns[0]].tolist()
    task_list_2 = task_pandas_2[task_pandas_2.columns[0]].tolist()
    
    # Generate unique combinations of two task IDs
    combined_keys = set()
    
    while len(combined_keys) < combinations_to_generate:
        task_id_1 = random.choice(task_list_1)
        task_id_2 = random.choice(task_list_2)
        if task_id_1 != task_id_2:  # Ensuring the two tasks are not the same
            combined_keys.add((task_id_1, task_id_2))
    
    # Convert the set of unique combinations to a DataFrame
    column_names = ["Task_Task_ID1", "Task_Task_ID2"]
    combined_keys_list = list(combined_keys)
    
    pd.DataFrame(combined_keys_list, columns=column_names).to_csv("Failure_Requires_Data_Generated.csv", index=False)

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
                    "Vehicle_Type_Data_Generated.csv",
                    "Car_Data_Generated.csv"]
    
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

    '''
    generatePartCSV()
    generateUsedInCSV(300)
    generateCarCSV()
    generateOwnsCSV(300)
    generatePurchaseCSV()
    generateMadePurchaseCSV(300)
    generateAppointmentCSV()
    GenerateAdditionallyScheduledCSV(300)
    GenerateWasPerformedCSV(300)
    GenerateRecommendsCSV(300)
    GenerateWasReplacedCSV(300)
    GenerateFailureRequiresCSV(300)
    '''

    GenerateWasPerformedCSV(300)
    GenerateRecommendsCSV(300)

    if not os.path.exists("Part_Data_Generated.csv"):
        generatePartCSV()
    if not os.path.exists("Used_In_Data_Generated.csv"):
        generateUsedInCSV(300)
    if not os.path.exists("Car_Data_Generated.csv"):
        generateCarCSV()
    if not os.path.exists("Owns_Data_Generated.csv"):
        generateOwnsCSV(300)
    if not os.path.exists("Purchase_Data_Generated.csv"):
        generatePurchaseCSV()
    if not os.path.exists("Made_Purchase_Data_Generated.csv"):
        generateMadePurchaseCSV(300)
    if not os.path.exists("Appointment_Data_Generated.csv"):
        generateAppointmentCSV()
    if not os.path.exists("Additionally_Scheduled_Data_Generated.csv"):
        GenerateAdditionallyScheduledCSV(300)
    if not os.path.exists("Was_Performed_Data_Generated.csv"):
        GenerateWasPerformedCSV(300)
    if not os.path.exists("Recommends_Data_Generated.csv"):
        GenerateRecommendsCSV(300)
    if not os.path.exists("Was_Replaced_Data_Generated.csv"):
        GenerateWasReplacedCSV(300)
    if not os.path.exists("Failure_Requires_Data_Generated.csv"):
        GenerateFailureRequiresCSV(300)

    print("CSV files successfully generated!")
    print("Import everything but _NF CSV files into the corresponding MySQL Workbench table")