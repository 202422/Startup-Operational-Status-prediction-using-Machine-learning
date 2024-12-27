# Topic: Startup Operational Status prediction using Machine learning

# Objective:
The objective of this project is to predict the current status of a startup—whether it is Operating, IPO, Acquired, or Closed. This problem will be addressed using a Supervised Machine Learning approach by training models based on the historical data of startups across all four categories.

# Summary:

The data contains industry trends, investment insights and individual company information. Since the data was acquired on a trial basis, it only contains information about companies. After training the model, we predict whether startups still operating, IPO, acquired, or closed.

# Data:

### Link to raw data(Huge JSON and Excel fiel):
        https://drive.google.com/file/d/1tWYkHYHm2HoiCajZ49Cs1K7sklWTdAbV/view


### Data types:

There are 196553 lines and  44 columns out of which will be used as features. The rest provide more information about the data, but will not be used for model training (like normalized name, entity id, short description etc.)

# Data Preprocessing:

### A. Data Cleaning
    1. Delete irrelevant & redundant information.
    2. Remove noise or unreliable data (missing values and outliers).

### B. Date variables Transformation
    1. Changes in original variables
    2. Create new variables from original variables

### C. Remaining missing values handling

# Exploratory Data Analysis:

### A. Univariate Analysis
    1. Numerical features
    2. Categorical features

### B. Bivariate Analysis
    1. Numerical-Numerical relationships
    2. Categorical-Categorical relationships
    3. Categorical-Numerical relationships

### C. Multivariate Analysis

# Feature Engineering

### A. Feature selection
    1. Numerical features
    2. Categorical features

### B. Log transformation and standardisation
    1. Log transformation
    2. Standardisation

### C. Creation of new features

### D. Feature encoding
    1. Target
    2. Categorical features

### E. Feature engineering Documentation

# Modelling

## Binary Classification:

### A. Binary labeling

### B. Oversampling and spliting

### C. Training models and Results
    1. Logistic Regression 
    2. Naive Bayes

## Multiclass Classification:

### A. Oversampling and spliting
### B. Training models and Results
    1. AdaBoostClassifier
    2. GradientBoostingClassifier