import numpy as np
import matplotlib.pyplot as plt


# ============================================
# Create Figure
# ============================================

fig = plt.figure(figsize=(14, 6))


# ============================================
# LEFT PANEL - 3D Surface Plot
# ============================================

ax1 = fig.add_subplot(
    121,
    projection="3d"
)

# Create X and Y values
x = np.linspace(-6, 6, 150)
y = np.linspace(-6, 6, 150)

# Create 2D coordinate grid
X, Y = np.meshgrid(x, y)

# Create ripple/wave function
R = np.sqrt(X**2 + Y**2)

Z = np.sin(R)

# Create surface
surface = ax1.plot_surface(
    X,
    Y,
    Z,
    cmap="coolwarm",
    edgecolor="none"
)

# Add colorbar
fig.colorbar(
    surface,
    ax=ax1,
    shrink=0.6,
    pad=0.1
)

# Titles and labels
ax1.set_title("3D Ripple / Wave Surface")

ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

# Set viewing angle
ax1.view_init(
    elev=30,
    azim=45
)


# ============================================
# RIGHT PANEL - 3D Scatter Plot
# ============================================

ax2 = fig.add_subplot(
    122,
    projection="3d"
)

# Set random seed
np.random.seed(42)

# --------------------------------------------
# Cluster 1
# --------------------------------------------

cluster1 = np.random.normal(
    loc=[-4, -2, 0],
    scale=0.6,
    size=(40, 3)
)

# --------------------------------------------
# Cluster 2
# --------------------------------------------

cluster2 = np.random.normal(
    loc=[0, 3, 2],
    scale=0.6,
    size=(40, 3)
)

# --------------------------------------------
# Cluster 3
# --------------------------------------------

cluster3 = np.random.normal(
    loc=[4, -1, 4],
    scale=0.6,
    size=(40, 3)
)


# --------------------------------------------
# Plot Cluster 1
# --------------------------------------------

ax2.scatter(
    cluster1[:, 0],
    cluster1[:, 1],
    cluster1[:, 2],
    label="Cluster 1",
    s=40
)


# --------------------------------------------
# Plot Cluster 2
# --------------------------------------------

ax2.scatter(
    cluster2[:, 0],
    cluster2[:, 1],
    cluster2[:, 2],
    label="Cluster 2",
    s=40
)


# --------------------------------------------
# Plot Cluster 3
# --------------------------------------------

ax2.scatter(
    cluster3[:, 0],
    cluster3[:, 1],
    cluster3[:, 2],
    label="Cluster 3",
    s=40
)


# Titles and labels
ax2.set_title("3D Scatter Plot")

ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")

# Add legend
ax2.legend()

# Set viewing angle
ax2.view_init(
    elev=30,
    azim=45
)


# ============================================
# Final Layout
# ============================================

plt.tight_layout()

plt.show()