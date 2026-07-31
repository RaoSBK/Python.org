#Date: 31/07/2026
#Author: Suraj Bhan Kumar

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


iris = sns.load_dataset("iris")


print("First 5 Rows of Iris Dataset:\n")
print(iris.head())

print("\n Grouped Descriptive Statistics: \n")
print(iris.groupby("species").describe())


fig, axes = plt.subplots(1,2, figsize=(14,6))


#Histogram with KDE
sns.histplot(
    data=iris,
    x="petal_length",
    hue='species',
    kde=True,
    element="step",
    stat='density',
    common_norm=False,
    ax=axes[0]
)




axes[0].set_title("Petal Length Distribution")


sns.violinplot(
    data=iris,
    x='species',
    y='sepal_width',
    palette='Set2',
    ax=axes[1]
)




axes[1].set_title("Sepal Width by species")


plt.tight_layout()
plt.show()



#Second figure


sns.pairplot(
    iris,
    hue="species",
    corner=True,
    diag_kind="kde"
)


plt.show()