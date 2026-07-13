import matplotlib.pyplot as plt

# X-axis value

x = [1,2,3,4,5]

#Y-axis value
y = [10,20,30,40,50]

#creating a figure
plt.figure(figsize=(8,5))

#plot the line graph
plt.plot(x, y, color='blue', linewidth = 2, marker = "o", linestyle = "-", label = "Sales")


#Title 
plt.title("Basic line plots")

#Axis labels
plt.xlabel("Day")
plt.ylabel("Sales")


#Grid 
plt.grid(True)

#Legend

plt.legend()

plt.show()