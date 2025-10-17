# Importing the data 
import pandas as pd
import numpy as np



data = pd.read_csv('student_exam_scores.csv')


# Turning data from collums into arrays


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


import matplotlib.pyplot as plt
import numpy as np

# Attempted a bar plot as a workaround because the original data was complicated,
# and we were unable to make it work the “correct” way.

x = np.arange(len(filtered_exam_scores))  
y = filtered_exam_scores                 
#plotting the graph
plt.bar(x, y, color='pink')            
plt.xlabel("Hours Studied")    
plt.ylabel("Exam Scores")
plt.title("Exam Scores for Students Who Studied > 2 Hours") 
plt.show()

# Plot of any type containing 2 subplots side by side: plotting two scatter plots
plt.scatter(x,y, color="red", alpha = 0.7)
plt.title("Scatter Plot of Exam Scores vs Study Time")
plt.xlabel("Number of hours studied")
plt.ylabel("Exam scores")
plt.subplot(1,2,2)
plt.scatter(x,y)
# Display the graph
plt.show()

# A pie chart
# Randomly select 15 samples from the 'previous_scores' column 
# and count how many times each score appears
pie_data = data["previous_scores"].sample(15).value_counts()
# Create a pie chart using the counts and label each slice with the score value
plt.pie(pie_data, labels=pie_data.index)
# Display the chart
plt.show()

# Scatter plot with grid
plt.scatter(x,y, color="red", alpha = 0.7)
plt.title("Scatter Plot of Exam Scores vs Study Time")
plt.xlabel("Number of hours studied")
plt.ylabel("Exam scores")
plt.grid(color='gray')
plt.show()

#Create a scatter plot
plt.scatter(x,y, color="red", alpha = 0.7)
plt.title("Scatter Plot of Exam Scores vs Study Time")
plt.xlabel("Number of hours studied")
plt.ylabel("Exam scores")
plt.show()

#Create a histogram
plt.hist(y, bins=25, color='purple', alpha=0.8)
plt.xlabel("Exam scores")
plt.ylabel("Frequency")
plt.title("Histogram of Exam Scores")
plt.show()
