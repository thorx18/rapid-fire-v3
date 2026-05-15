# =========================
# MOST IMPORTANT PANDAS COMMANDS
# =========================

import pandas as pd

# LOAD DATASET
df = pd.read_csv("students.csv")

# DISPLAY DATASET
print(df)

# FIRST 5 ROWS
print(df.head())

# LAST 5 ROWS
print(df.tail())

# DATASET INFORMATION
print(df.info())

# SHAPE (ROWS, COLUMNS)
print(df.shape)

# COLUMN NAMES
print(df.columns)

# DATATYPES
print(df.dtypes)

# STATISTICAL SUMMARY
print(df.describe())

# SELECT SINGLE COLUMN
print(df['Name'])

# SELECT MULTIPLE COLUMNS
print(df[['Name', 'FinalExamMarks']])

# FILTER PASSED STUDENTS
print(df[df['Result'] == 'Pass'])

# FILTER FAILED STUDENTS
print(df[df['Result'] == 'Fail'])

# FILTER MARKS > 70
print(df[df['FinalExamMarks'] > 70])

# SORT VALUES
print(df.sort_values(by='FinalExamMarks'))

# COUNT VALUES
print(df['Result'].value_counts())

# CHECK NULL VALUES
print(df.isnull().sum())

# MEAN
print(df['FinalExamMarks'].mean())

# MAXIMUM
print(df['FinalExamMarks'].max())

# MINIMUM
print(df['FinalExamMarks'].min())

# CREATE NEW COLUMN
df['TotalMarks'] = (
    df['InternalMarks']
    + df['PracticalMarks']
    + df['FinalExamMarks']
)

print(df)

# SAVE NEW CSV FILE
df.to_csv("new_students.csv", index=False)
