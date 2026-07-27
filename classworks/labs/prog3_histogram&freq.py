# Date: 14 july 2026
# Author: Suraj Bhan Kumar


import dictinories as np
import matplotlib.pyplot as plt

#Generate Random data
np.random.seed(42)
marks = np.random.normal(loc=70, scale=10, size= 500)


#Calculate statistics 
mean = np.mean(marks)
medain = np.median(marks)
std_dev = np.std(marks)

print("Mean: ", round(mean, 2))
print("Medain", round(medain, 2))
print("Standard Deviation: ", round(std_dev, 2))

# create a figure

fig, ax = plt.subplots(1,2, figsize = (14, 6))


#line plot
#compare the histograms with 10 bins and 30 bins

ax[0].hist(
    marks,
    bins =10,
    alpha = 0.6,
    color = "skyblue",
    edgecolor = "black",
    label = "10 Bins"
)

ax[0].hist(
    marks,
    bins = 30,
    alpha = 0.5,
    color = "green",
    edgecolor = "black",
    label  = "30 Bins"
)

ax[0].set_title("Histograms Comparision")
ax[0].set_label("Marks")
ax[0].set_ylabel("Frequency")
ax[0].legend()
ax[0].grid(True)


# Right plot
# Histograms + Frequency Polyon 


counts, bins, patches = ax[1].hist(
    marks,
    bins = 15,
    color = "lightgray",
    edgecolor = "black",
    alpha=0.8
)

#Calcualte Mindpoints
midpoints = (bins[:-1] + bins[1:])/2

#Draw Frequency Ploygon
ax[1].plot(
    midpoints,
    counts,
    color="orange",
    marker = "o",
    linewidth=2,
    label="Frequency Ploygon"
)

ax[1].set_title("Histogram with Frequency Ploygon")
ax[1].set_xlabel("Marks")
ax[1].set_ylabel("Frequency")
ax[1].legend()
ax[1].grid(True)

#Adjust Layout

plt.tight_layout()

#Show Graph
plt.show()