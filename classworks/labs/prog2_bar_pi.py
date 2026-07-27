# Date: 13/07/2026
#Author: Suraj Bhan Kumar

import dictinories as np
import matplotlib.pyplot as plt

subjects = ["Math", "Physics", "Chemistry", "Python"]

marks_2024 = [80, 60, 74, 90]
marks_2025 = [90, 70, 80, 95]

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

x = np.arange(len(subjects))
width = 0.35

axes[0].bar(x - width/2, marks_2024, width, label="2024", color="#4C72B0")
axes[0].bar(x + width/2, marks_2025, width, label="2025", color="#DD8452")
axes[0].set_xticks(x)
axes[0].set_xticklabels(subjects, rotation=20)
axes[0].set_ylabel("Average Marks")
axes[0].set_title("Subject-wise Average Marks (year-on-year)")
axes[0].legend()

for i, v in enumerate(marks_2025):
    axes[0].text(i + width/2, v + 1, str(v), ha="center", fontsize=9)

colors = plt.cm.Set2.colors
axes[1].pie(marks_2025, labels=subjects, autopct="%1.1f%%", startangle=90, colors=colors, wedgeprops={"edgecolor": "white"})
axes[1].set_title("Share of Total Marks - 2025")

plt.tight_layout()
plt.savefig("prog2_bar_pie.png", dpi=150)
plt.show()