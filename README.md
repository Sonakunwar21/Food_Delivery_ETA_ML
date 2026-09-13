<div align="center">

# 🍔 Food Delivery ETA Prediction

### End-to-End Machine Learning & MLOps Project

Predicting food delivery time using Machine Learning, MLflow, Docker,
GitHub Actions and AWS.

<br>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-ECS%20%7C%20ECR-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

<br><br>

**📦 Data → 🤖 ML → 🧪 MLflow → 🐳 Docker → 🔄 CI/CD → ☁️ AWS → 🌐 Streamlit**

</div>

---

## 📌 Overview

**Food Delivery ETA Prediction** is an end-to-end Machine Learning and
MLOps project designed to predict the estimated delivery time of food orders.

The project demonstrates the complete ML lifecycle:

> **Data Understanding → EDA → Model Training → Evaluation → Experiment Tracking → Containerization → CI/CD → Cloud Deployment**

The final model is served through an interactive **Streamlit application**
deployed on **Amazon ECS**.

> **Dataset Note:** This project uses a public historical food-delivery
> dataset. It is not live or real-time Zomato data.

---

## 🎯 Objective

Build a Machine Learning system that can estimate delivery time based on
factors such as:

- 👤 Delivery person information
- ⭐ Delivery ratings
- 📍 Restaurant & delivery location
- 🌦️ Weather conditions
- 🚦 Road traffic density
- 🛵 Vehicle information
- 📦 Order characteristics
- 🏙️ City
- 📅 Order timing

### Target

```text
Time_taken (min)
```
---

## 🔎 Exploratory Data Analysis

EDA was performed to understand the structure of the dataset and identify
the factors that influence delivery time.

### Analysis Performed

- 📊 Univariate Analysis
- 🔗 Bivariate Analysis
- 🧩 Multivariate Analysis
- 📈 Correlation Analysis
- 📍 Delivery Distance Analysis
- 🌦️ Weather vs Delivery Time
- 🛵 Vehicle Type vs Delivery Time
- 📦 Order Type vs Delivery Time
- 🏙️ City vs Delivery Time

### Key Insights

| Factor | Observation |
|---|---|
| ⭐ Ratings | Delivery ratings show a relationship with delivery time |
| 📦 Multiple Deliveries | Multiple deliveries tend to increase delivery duration |
| 🛵 Vehicle Condition | Vehicle condition has an observable relationship with delivery time |
| 🚦 Traffic | Traffic conditions contribute to delivery-time variation |
| 🌦️ Weather | Weather conditions show differences in delivery duration |

---

## 🤖 Machine Learning

The problem was treated as a **Regression** task because the target
variable represents delivery time in minutes.

### Models Evaluated

| Model | MAE ↓ | RMSE ↓ | R² ↑ |
|:---|---:|---:|---:|
| Linear Regression | 4.961 | 6.262 | 0.555 |
| **Random Forest** 🏆 | **3.298** | **4.177** | **0.802** |

---

## 🏆 Best Model — Random Forest

After comparing the evaluated models, **Random Forest Regression** was
selected as the best-performing model.

<div align="center">

| 📊 Metric | Result |
|:---:|:---:|
| **R² Score** | **0.802** |
| **MAE** | **3.298 min** |
| **RMSE** | **4.177 min** |

</div>

### Why Random Forest?

Random Forest performed better than Linear Regression on the test set,
achieving lower prediction errors and a substantially higher R² score.

The trained model is saved as:

```text
models/best_model.pkl
