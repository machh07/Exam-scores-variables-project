
# Importing the data 
import pandas as pd
data = pd.read_csv('student_exam_scores.csv')


# Turning data from collums into arrays
import numpy as np

study_hours = np.array(data["hours_studied"])
exam_scores = np.array(data["exam_score"])


# Positions where study hours > 2
positions = []

for i in range(len(study_hours)):
    if study_hours[i] > 2:
        positions = positions + [i]
        
# Using the positions to filter the data
filtered_study_hours = []
filtered_exam_scores = []

for i in positions:
    filtered_study_hours += [study_hours[i]]
    filtered_exam_scores += [exam_scores[i]]

# Turning the data back into arrays and printing them
filtered_study_hours = np.array(filtered_study_hours)
filtered_exam_scores = np.array(filtered_exam_scores)

print("Filtered Study Hours:", filtered_study_hours)
print("Filtered Exam Scores:", filtered_exam_scores)