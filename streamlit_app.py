# Make sure to install the required packages before running the script:
# pip install streamlit
# pip install folium
# pip install streamlit-folium

import streamlit as st
import folium
from streamlit_folium import st_folium

# Sample data
attractions = [
    {"name": "Petronas Twin Towers", "latitude": 3.1579, "longitude": 101.7123, "description": "Iconic twin skyscrapers in Kuala Lumpur.", "type": "historical site"},
    {"name": "Langkawi Sky Bridge", "latitude": 6.3810, "longitude": 99.6653, "description": "Curved pedestrian bridge in Langkawi.", "type": "natural wonder"},
    {"name": "Legoland Malaysia", "latitude": 1.4264, "longitude": 103.6318, "description": "Theme park in Johor Bahru.", "type": "amusement park"},
    # Add more attractions as needed
]

# Create a map centered around Malaysia
m = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

# Define a function to assign colors based on attraction type
def get_marker_color(attraction_type):
    if attraction_type == 'historical site':
        return 'red'
    elif attraction_type == 'natural wonder':
        return 'green'
    elif attraction_type == 'amusement park':
        return 'purple'
    else:
        return 'blue'

# Add markers to the map
for attraction in attractions:
    folium.Marker(
        location=[attraction['latitude'], attraction['longitude']],
        popup=f"<strong>{attraction['name']}</strong><br>{attraction['description']}",
        icon=folium.Icon(color=get_marker_color(attraction['type']))
    ).add_to(m)

# Display the total number of attractions
total_attractions = len(attractions)
folium.Marker(
    location=[4.2105, 101.9758],
    popup=f"Total Attractions: {total_attractions}",
    icon=folium.Icon(color='darkblue')
).add_to(m)

# Display the map in Streamlit
st.title('Tourist Attractions in Malaysia')
st_folium(m, width=700, height=500)
