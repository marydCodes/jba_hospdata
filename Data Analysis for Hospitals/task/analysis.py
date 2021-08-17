import pandas as pd

pd.set_option('display.max_columns', 8)

# import CSVs. Had to recalibrate path to my own PC to pass?
general = pd.read_csv(r"C:\Users\emade\Downloads\test\general.csv")
prenatal = pd.read_csv(r"C:\Users\emade\Downloads\test\prenatal.csv")
sports = pd.read_csv(r"C:\Users\emade\Downloads\test\sports.csv")

# Change column names to all match general
prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

# Merge dfs
merged = pd.concat([general, prenatal, sports], ignore_index=True)

# Delete 'Unnamed: 0' column
merged.drop(columns='Unnamed: 0', inplace=True)

print(merged.sample(n=20, random_state=30))
