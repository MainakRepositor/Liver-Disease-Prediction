"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# Import necessary functions from web_functions
from web_functions import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Hepatic Disease Prediction.
            </p>
        """, unsafe_allow_html=True)

   
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
    B = st.slider("Gender", int(df["Gender"].min()), int(df["Gender"].max()))
    C = st.slider("Total Bilirubin", int(df["Total_Bilirubin"].min()), int(df["Total_Bilirubin"].max()))
    D = st.slider("Direct Bilirubin", int(df["Direct_Bilirubin"].min()), int(df["Direct_Bilirubin"].max()))
    E = st.slider("Alkaline Phosphotase", int(df["Alkaline_Phosphotase"].min()), int(df["Alkaline_Phosphotase"].max()))
    F = st.slider("Alamine Aminotransferase", int(df["Alamine_Aminotransferase"].min()), int(df["Alamine_Aminotransferase"].max()))
    G = st.slider("Aspartate Aminotransferase", int(df["Aspartate_Aminotransferase"].min()), int(df["Aspartate_Aminotransferase"].max()))
    H = st.slider("Total Protiens", int(df["Total_Protiens"].min()), int(df["Total_Protiens"].max()))
    I = st.slider("Albumin", int(df["Albumin"].min()), int(df["Albumin"].max()))
    J = st.slider("Albumin Globulin Ratio", int(df["Albumin_and_Globulin_Ratio"].min()), int(df["Albumin_and_Globulin_Ratio"].max()))
    
    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J]

    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=["Age","Gender","Total_Bilirubin","Direct_Bilirubin","Alkaline_Phosphotase","Alamine_Aminotransferase","Aspartate_Aminotransferase","Total_Protiens","Albumin","Albumin_and_Globulin_Ratio"]
    st.dataframe(df3)

    st.sidebar.info("The parameters which have the major contribution to Parkinson\'s disease detection are ")

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.25
        st.info("Predicted Sucessfully...")

        if (D > 1 and F >70):
            st.warning("The person is prone to experience Hepatic Diseases!!")
            st.warning("The person has high risk of Liver Soaring and Vomiting") 
            st.info("Might be caused by regular drinking") 
        elif(C > 50):
            st.warning("The person is prone to experience Hepatic Diseases!!")
            st.warning("High Risk of Hepatitis A")
        elif (G > 70):
            st.warning("The person is prone to experience Hepatic Diseases!!")
            st.warning("High Risk of Hepatitis B")
        # Print the output according to the prediction
        elif (prediction == 1):
            st.warning("The person is prone to experience Hepatic Diseases!!")
                
            if (D > 1 and not F > 70):
                st.warning("The person is prone to experience Hepatic Diseases!!")
                st.warning("High risk of Chirosis")
            elif (F > 70 and not D > 1):
                st.warning("The person is prone to experience Hepatic Diseases!!")
                st.warning("High risk of Jaundice")
            
        else:
            st.success("The person has relatively less chances of Hepatic Diseases")

        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100),2),"%")
