# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PDjC1a7l-AvQYzLhZ3nF1XWExQyXGERk
"""

import streamlit as st
from joblib import load
import numpy as np
import pandas as pd

# Load model
model = load('random_forest_model.joblib')

# App title
st.title("Anemia Detection System")
st.write("Enter gender, RGB values, and hemoglobin level to check for anemia")

# Sidebar inputs
st.sidebar.header("Input Data")

# Gender selection with encoding
sex = st.sidebar.selectbox(
    "Gender",
    options=['Male', 'Female']
)
# Convert gender to numeric (assuming Male=1, Female=0 as per training)
sex_encoded = 1 if sex == 'Male' else 0

# RGB value inputs
red_pixel = st.sidebar.slider("Red Pixel Percentage (%Red Pixel)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
green_pixel = st.sidebar.slider("Green Pixel Percentage (%Green pixel)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
blue_pixel = st.sidebar.slider("Blue Pixel Percentage (%Blue pixel)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)

# Hemoglobin input
hb_level = st.sidebar.number_input(
    "Hemoglobin Level (g/dL)",
    min_value=0.0,
    max_value=25.0,
    value=13.0,
    step=0.1,
    help="Hemoglobin level measured in grams per deciliter (g/dL)"
)

# Display user inputs
st.write("Your input data:")
st.write(f"Gender: {sex}")
st.write(f"Red Pixel Percentage: {red_pixel}%")
st.write(f"Green Pixel Percentage: {green_pixel}%")
st.write(f"Blue Pixel Percentage: {blue_pixel}%")
st.write(f"Hemoglobin Level: {hb_level} g/dL")

# Add reference ranges for hemoglobin
st.sidebar.markdown("""
---
**Normal Hemoglobin Ranges:**
- Adult Males: 13.5-17.5 g/dL
- Adult Females: 12.0-15.5 g/dL
""")

# Prediction button
if st.button("Predict Anemia Status"):
    try:
        # Create input DataFrame with encoded gender
        input_data = pd.DataFrame({
            'Sex': [sex_encoded],
            '%Red Pixel': [red_pixel],
            '%Green pixel': [green_pixel],
            '%Blue pixel': [blue_pixel],
            'Hb': [hb_level]
        })

        # Make prediction
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)

        # Display results
        st.subheader("Prediction Results")
        if prediction[0] == "Yes":
            st.write("Result: Anemic")
        else:
            st.write("Result: Non-Anemic")

        # Display probabilities
        st.write("Prediction Probabilities:")
        st.write(f"Non-Anemic (No): {prediction_proba[0][0]:.2f}")
        st.write(f"Anemic (Yes): {prediction_proba[0][1]:.2f}")

    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")

