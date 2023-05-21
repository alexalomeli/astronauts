import streamlit as st
import pandas as pd
import json
import requests

# Print out all the names of the astronauts who are right now in space. You get the information about the Web APU from herehttp://open-notify.org/Open-Notify-API/People-In-Space/

# Make a request to the People in Space API and retrieve the response
response = requests.get("http://api.open-notify.org/astros.json")

#Add a title

st.title("People in space")

# Convert the response data from JSON to a Python dictionary
data = json.loads(response.text)


# Get the names of the astronauts currently in space
astronauts_names = [person["name"] for person in data["people"]]

# Print the number of people currently in space
st.write("Number of people in space:", data["number"])

# Print the names of the astronauts currently in space
st.write("Astronauts names:")
for name in astronauts_names:
    st.write(name)

def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    if data["message"] == "success":
        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]["longitude"])
        return latitude, longitude
    else:
        return None

def main():
    st.title("International Space Station Tracker")
    st.write("This app tracks the current location of the ISS.")

    # Fetch ISS location
    location = get_iss_location()
    if location:
        latitude, longitude = location
        df = pd.DataFrame({"LATITUDE": [latitude], "LONGITUDE": [longitude]})
        st.write("Current Latitude:", latitude)
        st.write("Current Longitude:", longitude)
        st.map(df)

    # Add a short description for the map
    st.write("Map showing the current location of the International Space Station.")

if __name__ == "__main__":
    main()


