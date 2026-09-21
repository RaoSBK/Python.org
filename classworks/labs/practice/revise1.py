import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2**np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(8,5))

ax.plot(x, y_sin, color = "royalblue", linewidth = 2, linestyle = "-", label = "sin(x)")

ax.plot(x, y_cos, color = "crimson", linewidth = 2, linestyle = "--", label = "cos(x)")

ax.set_xlabel("x, radians")
ax.set_ylabel("Ampletude")

ax.axhline(0, color = 'grey', linewidth = 0.8)
ax.legend(loc = "upper right")

ax.grid(True, linestyle = ":", alpha = 0.6)
plt.tight_layout()
plt.savefig("prog1", dpi = 100)

plt.show()