"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st



# Import necessary functions from web_functions
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title='Liver Disease Detector',
    page_icon='beer',
    layout='wide',
    initial_sidebar_state='auto'
)

# Import pages
from Tabs import home, data, predict, visualise

# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise
}

# Create a sidebar
# Add title to sidebar
st.sidebar.title("Navigation")

# Create horizontal navigation bar
nav_selection = st.sidebar.radio("Pages", list(Tabs.keys()), index=0)

# Loading the dataset.
df, X, y = load_data()

# Call the app function of selected page to run
if nav_selection in ["Prediction", "Visualisation"]:
    Tabs[nav_selection].app(df, X, y)
elif nav_selection == "Data Info":
    Tabs[nav_selection].app(df)
else:
    Tabs[nav_selection].app()
