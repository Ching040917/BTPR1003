import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Updated data of tourist attractions
data = {
    'Name': ['Petronas Twin Towers', 'Batu Caves', 'Mount Kinabalu', 'Perhentian Islands', 'Gunung Mulu National Park', 'Genting Highlands', 'Cameron Highlands'],
    'Latitude': [3.15785, 3.2379, 6.075, 5.91667, 4.0483, 3.42178, 4.4904],
    'Longitude': [101.7114, 101.6841, 116.558, 102.73333, 114.8125, 101.79347, 101.3899],
    'Description': [
        'The tallest twin towers in the world, located in Kuala Lumpur.',
        'A limestone hill with a series of caves and cave temples in Gombak.',
        'The highest peak in Southeast Asia, located in Sabah.',
        'A group of islands known for their clear waters and coral reefs.',
        'A national park famous for its limestone karst formations and caves.',
        'A hill resort with theme parks, casinos, and entertainment in Pahang.',
        'A highland region known for its tea plantations, cool climate, and strawberry farms.'
    ],
    'Type': ['Historical Site', 'Natural Wonder', 'Natural Wonder', 'Natural Wonder', 'Natural Wonder', 'Amusement Park', 'Natural Wonder']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Interactive Map of Tourist Attractions in Malaysia")

# Display total number of attractions
total_attractions = len(df)
st.write(f"**Total Attractions on the Map: {total_attractions}**")

# Create a Folium map
m = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

# Add markers to the map
for _, row in df.iterrows():
    color = 'blue' if row['Type'] == 'Historical Site' else \
            'green' if row['Type'] == 'Natural Wonder' else 'orange'

    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<strong>{row['Name']}</strong><br>{row['Description']}",
        tooltip=row['Name'],
        icon=folium.Icon(color=color)
    ).add_to(m)

# Display the map in Streamlit
st_folium(m, width=700, height=500)

# Hosting instructions
st.write("""
### Hosting Instructions:
1. Run the app locally using `streamlit run app.py`.
2. To host online, deploy the app on **Streamlit Community Cloud**:
   - [Streamlit Cloud](https://streamlit.io/cloud)
   - Login with your GitHub account.
   - Upload the project files or link to your GitHub repository.
   - Deploy your app in just a few clicks.
""")

