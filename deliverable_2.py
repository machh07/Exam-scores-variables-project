
# Importing the data 
import pandas as pd
scores = pd.read_csv('student_exam_scores.csv')


# Turning data from collums into arrays
import numpy as np

study_hours = np.array(scores["hours_studied"])
exam_scores = np.array(scores["exam_score"])


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

#Create the plot
import matplotlib.pyplot as plt
x = filtered_study_hours
y = filtered_exam_scores

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

#Create a bar graph
avg_scores = []

ranges = [(2, 4), (4, 6), (6, 8), (8, 10), (10, 12)]
labels = ['2-4', '4-6', '6-8', '8-10', '10-12']

plt.bar(labels, avg_scores, color='orange')
plt.title('Average Exam Scores by Study Hour Ranges')
plt.xlabel('Study Hours')
plt.ylabel('Average Exam Score')
plt.show()


#Create pie chart
plt.pie(avg_scores,
        labels=labels,
        autopct='%1.1f%%',    
        startangle=140,         
        colors=['orange', 'blue', 'cyan', 'yellow', 'green'])

plt.title('Average Exam Scores by Study Hour Ranges')
plt.show()

#Import seaborn
import seaborn as sns
sns.set_theme()

#Create plot of any type using grid
lineplot=sns.relplot(
    data=scores, 
    x="hours_studied",
    y="exam_score", 
    kind="line",
    errorbar="sd")
#Add a title to line plot
lineplot.fig.suptitle("Exam Score vs Hours Studied")
#You should comment your code with a quick explanation about each plot !!!


