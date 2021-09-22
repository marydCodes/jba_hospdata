import pandas as pd
import operator
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 8)

# import CSVs. Had to recalibrate path to my own PC to pass?
general = pd.read_csv(r"C:\Users\emade\Downloads\test\general.csv")
prenatal = pd.read_csv(r"C:\Users\emade\Downloads\test\prenatal.csv")
sports = pd.read_csv(r"C:\Users\emade\Downloads\test\sports.csv")

# Change column names to all match general
prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

# Merge dfs
hospitals = pd.concat([general, prenatal, sports], ignore_index=True)

# Clear data.
hospitals.drop(columns=['Unnamed: 0'], inplace=True)
hospitals.dropna(axis=0, how='all', inplace=True)

hospitals.loc[hospitals['gender'] == 'male', 'gender'] = 'm'
hospitals.loc[hospitals['gender'] == 'man', 'gender'] = 'm'
hospitals.loc[hospitals['gender'] == 'female', 'gender'] = 'f'
hospitals.loc[hospitals['gender'] == 'woman', 'gender'] = 'f'
hospitals.loc[hospitals['gender'].isnull(), 'gender'] = 'f'
hospitals.fillna(0, inplace=True)

# Count values.
# 1st question
highest_number_of_patients = hospitals.mode()['hospital'][0]

# 2nd question
stomach_issues_in_general =  hospitals.groupby(['hospital','diagnosis']).size()['general']['stomach']
patients_in_general = hospitals.groupby(['hospital']).size()['general']
answer_2 = round(stomach_issues_in_general / patients_in_general, 3)

# 3rd question
dislocation_issues_in_sport = hospitals.groupby(['hospital', 'diagnosis']).size()['sports']['dislocation']
patients_in_sports = hospitals.groupby(['hospital']).size()['sports']
answer_3 = round(dislocation_issues_in_sport / patients_in_sports, 3)

# 4th question
median_age_general = hospitals.groupby(['hospital'])[['age']].median().values[0][0]
median_age_sports = hospitals.groupby(['hospital'])[['age']].median().values[2][0]
answer_4 = int(median_age_general - median_age_sports)

# 5th question
blood_tests_table = pd.pivot_table(hospitals, index='hospital', columns='blood_test', aggfunc='count', fill_value=0).values
blood_tests_in_general = blood_tests_table[0][2]
blood_tests_in_prenatal = blood_tests_table[1][2]
blood_tests_in_sports = blood_tests_table[2][2]
blood_tests = {'general': blood_tests_in_general, 'prenatal': blood_tests_in_prenatal, 'sports': blood_tests_in_sports}

answer_5_value = max(blood_tests.values())
answer_5 = max(blood_tests.items(), key=operator.itemgetter(1))[0]

# Viz1
# What is the most common age of a patient among all hospitals?
# Choose one of the following age ranges:
# 0 - 15, 15 - 35, 35 - 55, 55 - 70, or 70 - 80
viz1 = sns.histplot(hospitals["age"])
plt.show()
ans1 = "15 - 35"

# Viz2
# What is the most common diagnosis among patients in all hospitals?
viz2 = plt.pie(hospitals["diagnosis"].value_counts())
plt.show()
ans2 = "pregnancy"

# Viz3
# Build a violin plot of height distribution by hospitals.
# Try to answer the questions.
# What is the main reason for the gap in values?
# Why there are two peaks, which correspond to the relatively small and big values?
viz3 = sns.violinplot(x='height',
                      data=hospitals)
plt.show()
ans3 = "It's because the units are not the same."

# Print result.
print(f'The answer to the 1st question: {ans1}')
print(f'The answer to the 2nd question: {ans2}')
print(f'The answer to the 3rd question: {ans3}')
# print(f'The answer to the 4th question is {answer_4}')
# print(f'The answer to the 5th question is {answer_5}, {answer_5_value} blood tests')
