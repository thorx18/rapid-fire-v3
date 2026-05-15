# =========================================
# SEABORN VISUALIZATION ON STUDENT DATASET
# =========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATASET
df = pd.read_csv("students.csv")

# =========================================
# 1. SCATTER PLOT
# =========================================

plt.figure(figsize=(10,6))

sns.scatterplot(
    x='StudyHours',
    y='FinalExamMarks',
    hue='Result',
    data=df
)

plt.title('Study Hours vs Final Exam Marks')

plt.xlabel('Study Hours')

plt.ylabel('Final Exam Marks')

plt.show()

# =========================================
# 2. HISTOGRAM
# =========================================

plt.figure(figsize=(10,6))

sns.histplot(
    data=df,
    x='Attendance',
    hue='Result',
    kde=True
)

plt.title('Attendance Distribution')

plt.xlabel('Attendance')

plt.show()

# =========================================
# 3. BAR PLOT
# =========================================

plt.figure(figsize=(10,6))

sns.barplot(
    x='Name',
    y='FinalExamMarks',
    data=df,
    palette='viridis'
)

plt.title('Student Final Exam Marks')

plt.xlabel('Student Name')

plt.ylabel('Marks')

plt.xticks(rotation=45)

plt.show()

# =========================================
# 4. BOX PLOT
# =========================================

plt.figure(figsize=(8,6))

sns.boxplot(
    x='Result',
    y='FinalExamMarks',
    data=df
)

plt.title('Result vs Final Exam Marks')

plt.show()

# =========================================
# 5. VIOLIN PLOT
# =========================================

plt.figure(figsize=(8,6))

sns.violinplot(
    x='Result',
    y='Attendance',
    data=df
)

plt.title('Attendance Distribution')

plt.show()

# =========================================
# 6. COUNT PLOT
# =========================================

plt.figure(figsize=(6,5))

sns.countplot(
    x='Result',
    data=df
)

plt.title('Pass and Fail Count')

plt.show()

# =========================================
# 7. HEATMAP
# =========================================

plt.figure(figsize=(8,6))

correlation = df.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Heatmap')

plt.show()

# =========================================
# 8. PAIR PLOT
# =========================================

sns.pairplot(
    df[
        [
            'Attendance',
            'StudyHours',
            'InternalMarks',
            'FinalExamMarks'
        ]
    ]
)

plt.show()