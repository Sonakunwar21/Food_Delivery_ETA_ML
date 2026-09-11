# Load the registered model and predict delivery time

from pathlib import Path
import pandas as pd
import mlflow


# Project path
BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "mlflow.db"

mlflow.set_tracking_uri(f"sqlite:///{DB_PATH}")

# Load the registered model (Version 1)

model_uri = "models:/Food_Delivery_ETA_Model/1"
model = mlflow.sklearn.load_model(model_uri)

# Example new order
new_order = pd.DataFrame([{
    "Delivery_person_Age": 27,
    "Delivery_person_Ratings": 4.6,
    "Restaurant_latitude": 22.5726,
    "Restaurant_longitude": 88.3639,
    "Delivery_location_latitude": 22.5958,
    "Delivery_location_longitude": 88.4009,
    "Order_Date": "12-09-2026",
    "Time_Orderd": "20:00",
    "Time_Order_picked": "20:10",
    "Weather_conditions": "Sunny",
    "Road_traffic_density": "High",
    "Vehicle_condition": 2,
    "Type_of_order": "Meal",
    "Type_of_vehicle": "motorcycle",
    "multiple_deliveries": 1,
    "Festival": "No",
    "City": "Metropolitan",
    "order_hour": 20,
    "order_day": 5,
    "is_weekend": 1,
    "distance_km": 4.5
}])


prediction = model.predict(new_order)[0]

print(f"Predicted Delivery Time: {prediction:.2f} minutes")