import pandas as pd
import collections
import glob
import random
import itertools

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
    print("Checking for duplicates")
    checkIDDuplication(glob.glob("*.csv"))
    print()
    print("Generating files with foreign keys")
    generatePartCSV()
    generateUsedInCSV(500)