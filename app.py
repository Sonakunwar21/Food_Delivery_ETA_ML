# Streamlit app for Food Delivery ETA prediction

import streamlit as st
import pandas as pd
from pathlib import Path
import joblib

# Project paths
BASE_DIR = Path(__file__).resolve().parent

# Load the trained model from the project
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"
model = joblib.load(MODEL_PATH)


# App title
st.title("🍔 Food Delivery ETA Prediction")
st.write("Predict the estimated delivery time for a food order.")


# User inputs
age = st.number_input("Delivery Person Age", 18, 70, 27)
rating = st.number_input("Delivery Person Rating", 1.0, 5.0, 4.5)

weather = st.selectbox(
    "Weather Conditions",
    ["Sunny", "Cloudy", "Windy", "Stormy", "Sandstorms", "Fog"]
)

traffic = st.selectbox(
    "Road Traffic Density",
    ["Low", "Medium", "High", "Jam"]
)

vehicle_condition = st.number_input(
    "Vehicle Condition", 0, 5, 2
)

order_type = st.selectbox(
    "Type of Order",
    ["Snack", "Meal", "Drinks", "Buffet"]
)

vehicle_type = st.selectbox(
    "Type of Vehicle",
    ["motorcycle", "scooter", "electric_scooter", "bicycle"]
)

multiple_deliveries = st.number_input(
    "Multiple Deliveries", 0, 3, 1
)

festival = st.selectbox(
    "Festival", ["No", "Yes"]
)

city = st.selectbox(
    "City", ["Urban", "Metropolitan", "Semi-Urban"]
)

distance = st.number_input(
    "Distance (km)", 0.1, 30.0, 4.5
)

order_hour = st.slider(
    "Order Hour", 0, 23, 20
)

order_day = st.slider(
    "Day of Week", 0, 6, 5
)

is_weekend = int(order_day >= 5)


# Prediction
if st.button("Predict Delivery Time"):

    input_data = pd.DataFrame([{
        "Delivery_person_Age": age,
        "Delivery_person_Ratings": rating,
        "Restaurant_latitude": 22.5726,
        "Restaurant_longitude": 88.3639,
        "Delivery_location_latitude": 22.5958,
        "Delivery_location_longitude": 88.4009,
        "Vehicle_condition": vehicle_condition,
        "Type_of_order": order_type,
        "Type_of_vehicle": vehicle_type,
        "multiple_deliveries": multiple_deliveries,
        "Weather_conditions": weather,
        "Road_traffic_density": traffic,
        "Festival": festival,
        "City": city,
        "order_hour": order_hour,
        "order_day": order_day,
        "is_weekend": is_weekend,
        "distance_km": distance
    }])

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Delivery Time: {prediction:.1f} minutes"
    )