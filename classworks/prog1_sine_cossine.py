# Date: 13/07/2026
#Author: Suraj Bhan Kumar


import dictinories as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

#create the fig and the axis
fig, ax = plt.subplots(figsize=(8,5))


#ploting sin (x)
ax.plot(x, y_sin, color = "royalblue", linewidth = 2, linestyle = "-", label = "sin(x)")

#ploting cos(x)
ax.plot(x, y_cos, color = "crimson", linewidth = 2, linestyle = '--', label = "cos(x)")

# Add a title
# ax.set_title("Suraj Bhan ", fontsize = 14, fontweight = "bold")
ax.set_title("Sine and Cosine waves", fontsize = 14, fontweight = "bold")


#label the axes
ax.set_xlabel("x, radians")
ax.set_ylabel("Amplitude")

#Draw a reference line

ax.axhline(0, color='grey', linewidth = 0.8)


#Adding a legend
ax.legend(loc= "upper right")


#Add a grid
ax.grid(True, linestyle=":", alpha = 0.6)



plt.tight_layout()
plt.savefig("program1_sine_cosine.png", dpi = 150)

plt.show()