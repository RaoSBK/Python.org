import numpy as np
import pandas as pd
import plotly.express as px


# =========================================================
# 1. CHOROPLETH MAP
# Simulated "Technology Adoption Index"
# =========================================================

countries_iso3 = [
    "IND", "USA", "CHN", "BRA",
    "GBR", "DEU", "JPN", "AUS",
    "ZAF", "CAN", "FRA", "RUS"
]

# Set seed so that the same random values are generated
np.random.seed(8)

# Generate Technology Adoption Index values
tech_index = np.random.uniform(
    40, 95, len(countries_iso3)
).round(1)

# Create DataFrame
choropleth_df = pd.DataFrame({
    "iso_alpha": countries_iso3,
    "TechIndex": tech_index
})


# Create Choropleth Map
fig1 = px.choropleth(
    choropleth_df,
    locations="iso_alpha",
    locationmode="ISO-3",
    color="TechIndex",
    color_continuous_scale="Plasma",
    range_color=(40, 95),
    title="Simulated Technology Adoption Index by Country"
)

# Save the map as HTML
fig1.write_html("program13_choropleth.html")

# Display the map
fig1.show()


# =========================================================
# 2. POINT / BUBBLE MAP
# Indian City-Level Sample Data
# =========================================================

cities = pd.DataFrame({

    "City": [
        "Hyderabad",
        "Delhi",
        "Mumbai",
        "Chennai",
        "Bengaluru",
        "Kolkata",
        "Pune"
    ],

    "Lat": [
        17.3850,
        28.7041,
        19.0760,
        13.0827,
        12.9716,
        22.5726,
        18.5204
    ],

    "Lon": [
        78.4867,
        77.1025,
        72.8777,
        80.2707,
        77.5946,
        88.3639,
        73.8567
    ],

    "Users_Lakh": [
        42,
        68,
        75,
        38,
        60,
        33,
        29
    ]
})


# Create Point/Bubble Map
fig2 = px.scatter_geo(
    cities,
    lat="Lat",
    lon="Lon",
    size="Users_Lakh",
    color="Users_Lakh",
    hover_name="City",
    color_continuous_scale="Viridis",
    scope="asia",
    title="App Users (in Lakh) Across Major Indian Cities"
)

# Configure geographical features
fig2.update_geos(
    showcountries=True,
    showcoastlines=True,
    coastlinecolor="black"
)

# Save the map as HTML
fig2.write_html("program13_pointmap.html")

# Display the map
fig2.show()