#Date 24-07-2026
#Author- Suraj Bhan Kumar

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr 


#Sample data

#Study hours
x= np.array([1,2,3,4,5,6,7,8,9,10])

#Exam hours
y = np.array([35,40,50,52,60,68,72,80,88,95])

#Attendance Percentage (Third variable)
attendance = np.array([60, 65,70,72,75,80,85,88,92,95])


#person correlation
r, p = pearsonr(x,y)

print("pearson correlation coeffiecient (r): ", round(r,3))


#regression line

m,c = np.polyfit(x,y,1)

regression_line = m*x+c


#Scatter plot with regression

plt.figure(figsize=(8,6))

plt.scatter(x,y, color='blue', label='Data Points')


plt.plot(
    x,
    regression_line,
    color='red',
    linewidth=2,
    label=f'y ={m:.2f}x + {c:.2f}'
)


plt.title("Scatter Plot with regression line")
plt.xlabel("Studey Hours")
plt.ylabel("Exam Marks")
plt.grid(True)
plt.legend()
plt.show()


#Bubble Chart

plt.figure(figsize=(8,6))
bubble_size = attendance*8

scatter = plt.scatter(
    x,
    y,
    s=bubble_size,
    c=attendance,
    camp='viridis',
    alpha=0.7
)

plt.colorbar(scatter, label="Attendance Precetage")


plt.title("Bubble Chart")
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")
plt.grid(True)

plt.show()

