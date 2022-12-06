"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Hepatic Disease Predictor")

    # Add image to the home page
    st.image("./images/home.jpeg")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Damage to the brain from interruption of its blood supply.
A stroke is a medical emergency. Symptoms of stroke include trouble walking, speaking and understanding, as well as paralysis or numbness of the face, arm or leg. Early treatment with medication like tPA (clot buster) can minimise brain damage. Other treatments focus on limiting complications and preventing additional strokes.</p>
    """, unsafe_allow_html=True)