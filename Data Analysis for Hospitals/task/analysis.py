import pandas as pd

pd.set_option('display.max_columns', 8)

# had to recalibrate path to my own PC to pass?
general = pd.read_csv(r"C:\Users\emade\Downloads\test\general.csv")
print(general.head(20))

prenatal = pd.read_csv(r"C:\Users\emade\Downloads\test\prenatal.csv")
print(prenatal.head(20))

sports = pd.read_csv(r"C:\Users\emade\Downloads\test\sports.csv")
print(sports.head(20))