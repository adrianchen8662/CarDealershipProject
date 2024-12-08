import pandas as pd
import collections
import glob

def CheckIDDuplication(csv_list):
    print("Duplicate Primary Keys:")
    for i in csv_list:
        df = pd.read_csv(i)
        matrix2 = df[df.columns[0]]
        id_List = matrix2.tolist()
        print(i, " ", [item for item, count in collections.Counter(id_List).items() if count > 1])

if __name__ == "__main__":
    CheckIDDuplication(glob.glob("*.csv"))