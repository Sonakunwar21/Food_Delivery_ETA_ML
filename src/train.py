# Load data, create useful features, and split into train/test sets

from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Track experiments with MLflow
import mlflow
import mlflow.sklearn

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "delivery_data.csv"


# Load dataset
df = pd.read_csv(DATA_PATH)


# Convert date and time columns
df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%d-%m-%Y", errors="coerce")
df["Time_Orderd"] = pd.to_datetime(df["Time_Orderd"], format="%H:%M", errors="coerce")
df["Time_Order_picked"] = pd.to_datetime(
    df["Time_Order_picked"], format="%H:%M", errors="coerce"
)
# Create time-based features
df["order_hour"] = df["Time_Orderd"].dt.hour
df["order_day"] = df["Order_Date"].dt.dayofweek
df["is_weekend"] = (df["order_day"] >= 5).astype(int)

# Calculate approximate distance from coordinates
lat_diff = df["Delivery_location_latitude"] - df["Restaurant_latitude"]
lon_diff = df["Delivery_location_longitude"] - df["Restaurant_longitude"]

df["distance_km"] = 111 * np.sqrt(lat_diff**2 + lon_diff**2)

# Define features and target
TARGET = "Time_taken (min)"
X = df.drop(columns=[TARGET])
y = df[TARGET]

# Remove identifier columns
X = X.drop(columns=["ID", "Delivery_person_ID"], errors="ignore")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)
print("Target:", TARGET)
# Prepare preprocessing for numeric and categorical features

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# Remove raw date/time columns after extracting useful features
X = X.drop(
    columns=["Order_Date", "Time_Orderd", "Time_Order_picked"],
    errors="ignore"
)
numeric_features = X.select_dtypes(include=np.number).columns.tolist()
categorical_features = X.select_dtypes(exclude=np.number).columns.tolist()

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])
preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

# Train baseline regression models
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
    n_estimators=50,
    max_depth=10,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
    )
}
trained_models = {}
for name, model in models.items():

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)
    trained_models[name] = pipeline

    print(f"{name} trained successfully.")

    # Evaluate model performance

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
results = []
for name, model in trained_models.items():

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    results.append({
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    })
results_df = pd.DataFrame(results).sort_values("MAE")

print("\nModel Comparison:")
print(results_df.round(3))

# Select the model with the lowest MAE

best_model_name = results_df.iloc[0]["Model"]
best_model = trained_models[best_model_name]

print(f"\nBest model: {best_model_name}")

# Use a project-local MLflow tracking database
DB_PATH = BASE_DIR / "mlflow.db"
mlflow.set_tracking_uri(f"sqlite:///{DB_PATH}")

# Track the best model with MLflow
mlflow.set_experiment("Food_Delivery_ETA")
with mlflow.start_run(run_name=best_model_name) as run:
    predictions = best_model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    mlflow.log_param("model", best_model_name)
    mlflow.log_metric("MAE", mae)
    mlflow.log_metric("RMSE", rmse)
    mlflow.log_metric("R2", r2)

    mlflow.sklearn.log_model(
    best_model,
    name="model",
    skops_trusted_types=["numpy.dtype"])

    print("Best model logged to MLflow.")
    # Register the best model
    
    registered_model_name = "Food_Delivery_ETA_Model"

    mlflow.register_model(
        model_uri=f"runs:/{run.info.run_id}/model",
        name=registered_model_name
    )
# Save the best trained model

import joblib
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"
# Create model directory if it does not exist
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(best_model, MODEL_PATH, compress=3)
print(f"Best model saved at: {MODEL_PATH}")

# Test prediction on one sample order
sample = X_test.iloc[[0]]
prediction = best_model.predict(sample)[0]
print(f"Predicted delivery time: {prediction:.2f} minutes")
print(f"Actual delivery time: {y_test.iloc[0]:.2f} minutes")