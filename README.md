# Diabetes Prediction System

This project implements a **Diabetes Prediction System** using machine learning and web technologies. The system allows doctors to input patient data, make predictions on whether the patient has diabetes, and provides medical recommendations. The model is built using a **Stacking Classifier** with base models including **XGBoost**, **Logistic Regression**, and **Support Vector Classifier** (SVC).

## Features
- Predict whether a patient has diabetes or not based on their health data.
- Provide medical recommendations for patients diagnosed with diabetes.
- Includes basic information on diet, exercise, and medication for the doctor’s guidance.
- Built as a web application using **Flask**.
  
## Model Overview
The model is a **Stacking Classifier** that combines the following base learners:
1. **XGBoost**: A powerful gradient boosting model used for classification tasks.
2. **Support Vector Classifier (SVC)**: A linear classifier used to separate data points.
3. **Logistic Regression**: A linear model for binary classification.

The final predictions are made by a **meta-model** (Logistic Regression), which aggregates the results from the base learners.

### Technologies Used
- **Flask**: Web framework used to create the web interface.
- **XGBoost**: A gradient boosting model used in the stacking classifier for predicting diabetes.
- **Scikit-learn**: Library used for data preprocessing, model building (StackingClassifier, LogisticRegression, SVC), and evaluation.
- **Joblib**: Used for saving and loading the trained model.
- **NumPy**: Used for data manipulation and numerical operations.
- **HTML/CSS/JavaScript**: For the frontend web interface.

### Model Evaluation
The model is evaluated using the **accuracy score**, providing a measure of the model's overall performance on the test dataset.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.x
- Flask
- Scikit-learn
- XGBoost
- Joblib
- NumPy

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Anastasia-35/diabetes-prediction-system.git
   cd diabetes-prediction-system
