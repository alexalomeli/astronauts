import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import json
import requests

# Print out all the names of the astronauts who are right now in space. You get the information about the Web APU from herehttp://open-notify.org/Open-Notify-API/People-In-Space/

# Make a request to the People in Space API and retrieve the response
response = requests.get("http://api.open-notify.org/astros.json")

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



