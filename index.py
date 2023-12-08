import streamlit as st
import joblib
import pandas as pd 

import os
print(os.getcwd())

with open("model.pkl", "rb") as f:
    model = joblib.load(f)

s_p_l = st.number_input('Sepal Length')
s_p_w = st.number_input('Sepal Width')
p_t_l = st.number_input('Petal Length')
p_t_w = st.number_input('Petal Width')

if st.button("predict"):
    data = {
        "SepalLengthCm":[s_p_l],
        "SepalWidthCm":[s_p_w],
        "PetalLengthCm":[p_t_l],
        "PetalWidthCm":[p_t_w]  
    }

    df = pd.DataFrame(data)

    pred = model.predict(df)
    """
    ## Inputs
    """
    df

    """
    ## Predicted Class
    """

    pred