import numpy as np
import matplotlib.pyplot as plt


#Generate sample data

np.random.seed(42)

section_A = np.random.normal(70,8,50)
section_B = np.random.normal(68, 10,50)


#Section C contains outliers
section_C = np.append(
    np.random.normal(72,7,48),
    [40,110]
)

section_D = np.random.normal(69, 9, 50)

sections = {
    "Section A": section_A,
    "Section B": section_B,
    "Section C": section_C,
    "Section D": section_D
}


#Function to proint statistics

def describe(data, name):
    print("="*40)
    print(name)
    print("="*40)

    print("Count :", len(data))
    print("Mean :", round(np.mean(data),2))
    print("Std :", round(np.std(data),2))
    print("Min :", round(np.min(data),2))
    print("Q1 :", round(np.percentile(data, 25), 2))
    print("Median :", round(np.median(data),2))
    print("Q3 :", round(np.percentile(data, 75),2))
    print("Max :", round(np.max(data),2))


    #IQR
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data,75)
    iqr = q3-q1

    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr


#printing status
for name, data in sections.items():
    describe(data,name)


#Draw Box plot

fig,ax = plt.subplots(figsize=(10,6))


box = ax.boxplot(
    sections.values(),
    patch_artist=True,
    tick_labels=list(sections.keys())
)


colors = ["skyblue", "lightgreen", "orange", "pink"]

for patch,color in zip(box["boxes"],colors):
    patch.set_facecolor(color)

ax.set_title("Box plot for Four sections")
ax.set_xlabel("Sections")
ax.set_ylabel("Marks")

ax.grid(True)

plt.show()