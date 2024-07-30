import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the pre-trained model
with open('xgb_diamond_price_model.pkl', 'rb') as file:
    dtr_model = pickle.load(file)

# Function to make predictions
def predict_price(carat, cut, color, clarity, depth, table, x, y, z):
    input_data = np.array([[carat, cut, color, clarity, depth, table, x, y, z]])
    prediction = dtr_model.predict(input_data)
    return prediction[0]

# Streamlit app
st.set_page_config(page_title="Diamond Price Prediction", page_icon="💎")

st.title("Diamond Price Prediction App")
st.image("diamond.jpg", use_column_width=True)
st.markdown("""
<style>
body {
    background-color: #f0f0f5;
}
.main .block-container {
    padding: 2rem 2rem 2rem 2rem;
    border-radius: 10px;
    background-color: white;
}
</style>
""", unsafe_allow_html=True)

st.write("Enter the characteristics of the diamond:")

col1, col2 = st.columns(2)

with col1:
    carat = st.number_input("Carat (weight of the diamond)", min_value=0.0, max_value=5.0, step=0.01)
    cut = st.selectbox("Cut (Fair=0, Ideal=4)", ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    color = st.selectbox("Color (J (worst), D (best))", ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
    clarity = st.selectbox("Clarity (I1 (worst), IF (best))", ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

with col2:
    table = st.number_input("Table (width of top of diamond relative to widest point)", min_value=0.0, max_value=100.0, step=0.1)
    x = st.number_input("X (length in mm)", min_value=0.0, max_value=10.0, step=0.01)
    y = st.number_input("Y (width in mm)", min_value=0.0, max_value=10.0, step=0.01)
    z = st.number_input("Z (depth in mm)", min_value=0.0, max_value=10.0, step=0.01)
depth = st.number_input("Depth (total depth percentage)", min_value=0.0, max_value=100.0, step=0.1)

# Ordinal encoding for categorical features
cut_mapping = {'Fair': 0, 'Good': 1, 'Very Good': 2, 'Premium': 3, 'Ideal': 4}
color_mapping = {'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6}
clarity_mapping = {'I1': 0, 'SI2': 1, 'SI1': 2, 'VS2': 3, 'VS1': 4, 'VVS2': 5, 'VVS1': 6, 'IF': 7}

cut = cut_mapping[cut]
color = color_mapping[color]
clarity = clarity_mapping[clarity]

if st.button("Predict Price"):
    price = predict_price(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f"The predicted price of the diamond is ${price:.2f}")

st.markdown("""
    <br>
    <center>
        <strong>Developed by Muneeb Ul Hassan</strong>
        <a href="https://www.linkedin.com/in/muneeb-ul-hassan-machine-learning-expert/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width:20px;height:20px;margin-left:8px;">
        </a>
    </center>
    """, unsafe_allow_html=True)
