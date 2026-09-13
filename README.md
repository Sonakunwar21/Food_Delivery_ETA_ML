<div align="center">

# 🚀 Food Delivery ETA Prediction

### End-to-End Machine Learning & MLOps Project

<p>
  Predict food delivery time using Machine Learning and deploy the model
  through a production-style MLOps pipeline.
</p>

<br>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

---

## 🎯 Project Overview

**Food Delivery ETA Prediction** is an end-to-end Machine Learning and MLOps project that predicts the estimated delivery time of a food order.

The project covers the complete journey from:

**Data → EDA → Machine Learning → Model Tracking → Containerization → CI/CD → AWS Deployment**

The application allows users to enter delivery-related information and receive an estimated delivery time through an interactive Streamlit interface.

> **Dataset Note:** This project uses a public historical food-delivery dataset. It is not live or real-time Zomato data.

---

## 📊 Dataset

The dataset contains approximately **45,000+ food delivery records** with information related to:

| Category | Features |
|---|---|
| 👤 Delivery | Age, Ratings, Vehicle Condition |
| 📍 Location | Restaurant & Delivery Coordinates |
| 🌦️ Environment | Weather, Traffic Density |
| 🛵 Order | Order Type, Vehicle Type, Multiple Deliveries |
| 📅 Time | Order Date, Order Time, Pickup Time |
| 🎯 Target | `Time_taken (min)` |

---

## 🔍 Exploratory Data Analysis

The dataset was explored through:

- Univariate analysis
- Bivariate analysis
- Multivariate analysis
- Correlation analysis
- Delivery distance analysis
- Weather vs delivery time
- Vehicle type vs delivery time
- Traffic conditions vs delivery time
- City and order-type analysis

### Key Observations

- Delivery ratings show a relationship with delivery time.
- Multiple deliveries tend to increase delivery time.
- Vehicle condition has an observable relationship with delivery duration.
- Traffic and environmental conditions contribute to delivery-time variation.

---

## 🤖 Machine Learning

Two regression models were evaluated:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 4.961 | 6.262 | 0.555 |
| **Random Forest** | **3.298** | **4.177** | **0.802** |

### 🏆 Best Model

**Random Forest Regression**

The Random Forest model achieved an **R² score of 0.802**, explaining approximately 80% of the variation in delivery time on the test data.

The trained model is saved as:

```text
models/best_model.pkl