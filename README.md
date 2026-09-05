# CreditGuard AI – Credit Card Default Prediction

## Project Overview

CreditGuard AI is a machine learning-based web application designed to predict credit card default risk using customer financial and repayment information.

The project uses a Decision Tree Classifier trained on the UCI Default of Credit Card Clients dataset. The trained machine learning model is integrated with a Flask web application, allowing users to enter customer information and receive an estimated credit default-risk prediction.

This project demonstrates an end-to-end machine learning workflow, including data preprocessing, exploratory data analysis, feature engineering, feature selection, model training, model evaluation, hyperparameter tuning, model serialization, and Flask integration.

## Problem Statement

Credit card default is an important risk factor for financial institutions. Identifying customers who may have a higher probability of default can support better credit-risk assessment and decision-making.

The objective of this project is to develop a machine learning model that analyzes customer financial and repayment information and predicts whether a customer is likely to default on their credit card payment.

## Objectives

- Analyze customer financial and repayment information.
- Perform data cleaning and preprocessing.
- Perform exploratory data analysis.
- Create meaningful financial features.
- Select relevant features for model training.
- Train a Decision Tree Classifier.
- Perform hyperparameter tuning using GridSearchCV.
- Evaluate the model using multiple classification metrics.
- Save the trained machine learning model.
- Integrate the model with a Flask web application.
- Build an interactive credit default prediction system.

## Dataset

### UCI Default of Credit Card Clients Dataset

This project uses the UCI Default of Credit Card Clients dataset.

Dataset details:

- Total records: 30,000
- Original predictor variables: 23
- Final model features: 26
- Target variable: default payment next month

### Target Classes

- 0 → No Default
- 1 → Default

The dataset contains customer information related to:

- Credit limit
- Gender
- Education
- Marital status
- Age
- Repayment status
- Bill amounts
- Payment amounts

## Technologies Used

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- Decision Tree Classifier
- GridSearchCV
- 5-Fold Cross Validation

### Web Development

- Flask
- HTML
- CSS
- JavaScript

### Model Serialization

- Joblib

## Machine Learning Workflow

Data Collection
↓
Data Understanding
↓
Data Cleaning
↓
Exploratory Data Analysis
↓
Feature Engineering
↓
Feature Selection
↓
Train/Test Split
↓
Decision Tree Classifier
↓
Model Evaluation
↓
Hyperparameter Tuning
↓
Final Model
↓
Model Serialization
↓
Flask Web Application

## Data Preprocessing

The dataset was analyzed and prepared before training the machine learning model.

The preprocessing process included:

- Checking data types
- Checking missing values
- Checking duplicate records
- Checking duplicate customer IDs
- Separating features and target variable
- Preparing the dataset for machine learning

## Feature Engineering

Three additional features were created to represent aggregated customer payment and billing behavior.

### TOTAL_PAY_AMT

Represents the total payment amount across six months.

PAY_AMT1 + PAY_AMT2 + PAY_AMT3 + PAY_AMT4 + PAY_AMT5 + PAY_AMT6

### MAX_PAY_DELAY

Represents the maximum repayment-delay status across six repayment-history periods.

max(PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6)

### TOTAL_BILL_AMT

Represents the total bill amount across six months.

BILL_AMT1 + BILL_AMT2 + BILL_AMT3 + BILL_AMT4 + BILL_AMT5 + BILL_AMT6

These engineered features were included in the final model.

## Machine Learning Model

### Decision Tree Classifier

The final machine learning algorithm used in this project is a Decision Tree Classifier.

The Decision Tree learns decision rules from customer financial and repayment information and uses those rules to classify customers into default and non-default categories.

The model was tuned using GridSearchCV with 5-Fold Cross Validation.

### Best Hyperparameters

- max_depth = 5
- min_samples_split = 50
- min_samples_leaf = 1
- random_state = 42

## Hyperparameter Tuning

GridSearchCV was used to find a suitable combination of Decision Tree hyperparameters.

The tuning process considered:

- max_depth
- min_samples_split
- min_samples_leaf
- 5-Fold Cross Validation

### Best Configuration

- max_depth: 5
- min_samples_split: 50
- min_samples_leaf: 1

The tuned model was selected as the final Decision Tree model.

## Model Evaluation

The final Decision Tree model achieved approximately 82.1% test accuracy.

### Evaluation Details

- Test Accuracy: 82.1%
- Train/Test Split: 80/20
- Cross Validation: 5-Fold

### Classification Report

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| No Default (0) | 0.84 | 0.95 | 0.89 |
| Default (1) | 0.67 | 0.36 | 0.47 |
| Accuracy | - | - | 0.82 |

Because the target classes are imbalanced, accuracy alone is not sufficient to evaluate the complete model performance. Precision, recall, and F1-score were also considered.

## Feature Importance

Feature importance from the final Decision Tree model showed that repayment-related features had a strong influence on the predictions.

### Top Features

| Feature | Importance |
|---|---:|
| PAY_0 | 0.673801 |
| MAX_PAY_DELAY | 0.156329 |
| PAY_2 | 0.036381 |
| TOTAL_BILL_AMT | 0.033284 |
| LIMIT_BAL | 0.017565 |
| TOTAL_PAY_AMT | 0.016559 |

PAY_0 was the most influential feature in the final Decision Tree model.

## Flask Web Application

The trained machine learning model was integrated into a Flask web application called CreditGuard AI.

The application provides a multi-step prediction interface.

### Customer Information

Users provide:

- Credit limit
- Gender
- Education
- Marital status
- Age

### Repayment History

Users provide:

- PAY_0
- PAY_2
- PAY_3
- PAY_4
- PAY_5
- PAY_6

### Billing Information

Users provide:

- BILL_AMT1
- BILL_AMT2
- BILL_AMT3
- BILL_AMT4
- BILL_AMT5
- BILL_AMT6

### Payment Information

Users provide:

- PAY_AMT1
- PAY_AMT2
- PAY_AMT3
- PAY_AMT4
- PAY_AMT5
- PAY_AMT6

### Automatic Feature Calculation

The application automatically calculates:

- TOTAL_PAY_AMT
- MAX_PAY_DELAY
- TOTAL_BILL_AMT

The final 26-feature input is passed to the trained Decision Tree model.

## Prediction Results

The application provides two main prediction outcomes.

### Low Default Risk

Prediction: No Default

### High Default Risk

Prediction: Default

The prediction represents the output generated by the trained machine learning model based on the information entered by the user.

## Application Pages

### Home

Introduces CreditGuard AI and explains the purpose of the application.

### Prediction

Provides a multi-step form for entering customer financial information.

### Review

Displays the entered information and automatically calculated features before prediction.

### Result

Displays the predicted credit card default risk.

### About Model

Provides information about the dataset, machine learning model, features, evaluation, and methodology.

## Project Structure

Credit_Card_Default/
│
├── app.py
├── credit_card_default_model.pkl
│
├── templates/
│   ├── index.html
│   ├── prediction.html
│   ├── result.html
│   └── about.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js

## How to Run the Project

### 1. Clone the Repository

git clone https://github.com/vishnu2007-design/CreditGuard-AI.git

### 2. Navigate to the Project

cd CreditGuard-AI

### 3. Install Required Libraries

pip install flask pandas numpy scikit-learn joblib

### 4. Run the Flask Application

python app.py

### 5. Open the Application

Open the local Flask URL displayed in the terminal.

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Python programming
- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Feature selection
- Classification
- Decision Tree algorithms
- Hyperparameter tuning
- GridSearchCV
- Cross Validation
- Model evaluation
- Feature importance analysis
- Model serialization
- Flask development
- Frontend and backend integration
- Building an end-to-end machine learning application

## Future Improvements

Future improvements could include:

- Improving recall for the default class.
- Experimenting with additional machine learning algorithms.
- Adding probability-based risk scores.
- Implementing model explainability using SHAP.
- Deploying the application to a suitable cloud platform.
- Adding database integration.
- Adding user authentication.
- Implementing model monitoring and performance tracking.

## Disclaimer

CreditGuard AI is an educational machine learning project.

The predictions generated by this application are model-based estimates and should not be considered professional financial advice or the sole basis for real-world credit decisions.

## Author

Jaini Vishnu

Engineering Student | Machine Learning | Python | Data Science

## Project Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.
