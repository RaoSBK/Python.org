import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


 
# Create Sample Data
 

np.random.seed(42)

data = pd.DataFrame({
    "Study_Hours": np.random.randint(1, 10, 50),
    "Attendance": np.random.randint(50, 100, 50),
    "Marks": np.random.randint(40, 100, 50),
    "Assignments": np.random.randint(1, 10, 50)
})

# Create categorical columns
data["Gender"] = np.random.choice(
    ["Male", "Female"],
    size=50
)

data["Grade"] = np.random.choice(
    ["A", "B", "C", "D"],
    size=50
)


 
# Calculate Correlation Matrix
 

corr = data[
    ["Study_Hours", "Attendance", "Marks", "Assignments"]
].corr()


 
# Create Mask for Upper Triangle
 

mask = np.triu(
    np.ones_like(corr, dtype=bool)
)


 
# Create Figure
 

fig, axes = plt.subplots(
    1,
    2,
    figsize=(14, 6)
)



# LEFT PANEL
# Correlation Heatmap


sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    center=0,
    ax=axes[0]
)

axes[0].set_title(
    "Correlation Heatmap"
)


 
# RIGHT PANEL
# Cross-tabulation Heatmap
 

cross_tab = pd.crosstab(
    data["Gender"],
    data["Grade"]
)

sns.heatmap(
    cross_tab,
    annot=True,
    fmt="d",
    cmap="Blues",
    ax=axes[1]
)

axes[1].set_title(
    "Gender × Grade Cross-tabulation"
)

axes[1].set_xlabel("Grade")
axes[1].set_ylabel("Gender")


 
# Adjust Layout


plt.tight_layout()

 
# Display
 

plt.show()