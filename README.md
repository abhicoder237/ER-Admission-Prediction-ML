🏥 Predicting Emergency Department Admissions
📌 Project Overview

Emergency Departments (EDs) often face overcrowding, leading to longer waiting times, resource strain, and reduced quality of care.
This project aims to predict whether a patient visiting the Emergency Department will be admitted or discharged, using real-world hospital data and supervised machine learning techniques.

The goal is to support better hospital resource planning and patient flow management.

🎯 Problem Statement

Can we predict ED admission outcomes using patient demographics, triage information, and clinical indicators at the time of arrival?

Accurate predictions can help hospitals:

Allocate beds and staff proactively

Reduce overcrowding

Improve patient experience and operational efficiency

📂 Dataset

Source:
Emergency Department Admissions Dataset (Iran) – Mendeley Data

Real, anonymized hospital records

Multi-year data (2017–2022)

Large-scale and messy real-world dataset

Key Data Characteristics:

Patient demographics (age, gender)

Triage level

Vital signs

Admission & discharge outcomes

Temporal features (date, time)

⚠️ Patient identities are anonymized to ensure privacy.

🎯 Target Variable

Admission Outcome

1 → Admitted

0 → Discharged

This makes the problem a Supervised Classification Task.

🧠 Planned Machine Learning Approach
Models

Logistic Regression (baseline)

Random Forest Classifier

XGBoost Classifier

Evaluation Metrics

Accuracy

Precision, Recall, F1-score

ROC-AUC

🔍 Project Workflow

Data Understanding & Cleaning

Exploratory Data Analysis (EDA)

Feature Engineering

Train-Test Split

Model Training & Evaluation

Model Explainability (SHAP / Feature Importance)

Insights & Conclusions

🛠️ Tools & Technologies

Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

XGBoost

SHAP

📈 Expected Outcomes

A robust ML model to predict ED admission likelihood

Identification of key factors influencing admission decisions

Insights useful for hospital operations and planning

🚀 Future Enhancements

Length of Stay (LOS) prediction

Time-series modeling for hourly/daily ED load

Deployment as a simple dashboard (Streamlit)

Generalization to other hospitals or regions
