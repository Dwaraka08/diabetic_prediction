import streamlit as st
import numpy as np
import pandas as pd
import dill

st.title("Diabetic Prediction Model")

col1,col2=st.columns(2)

with col1:

    Pregnancies=st.text_input("Enter the pregnancies:")
    Glucose=st.text_input("Enter the Glucose level:")
    BloodPressure=st.text_input("Enter Blood pressure:")
    SkinThickness=st.text_input("Enter the Skin Thickness:")
    Insulin=st.text_input("Enter the Insulin level:")
    BMI=st.text_input("Enter the BMI level:")
    Diabatespedigreefunction=st.text_input("Enter the Diabatespedigree function:")
    Age=st.text_input("Enter the Age:")


    with open(r"dia.dill","rb") as f:
        model=dill.load(f)


with col2:
    st.image("dia.jpeg")

if st.button("prediction"):
    data=[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,Diabatespedigreefunction,Age]]
    data_array=np.array(data,dtype=float).reshape(1,-1)
    prediction=model.predict(data_array)
    if prediction ==1:
        st.write("Diabetic")
    elif prediction==0:
        st.write("Non-Diabetic")
