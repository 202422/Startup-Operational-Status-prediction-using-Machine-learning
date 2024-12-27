# Topic: Startup Operational Status prediction using Machine learning

# Objective:
The objective of this project is to predict the current status of a startup—whether it is Operating, IPO, Acquired, or Closed. This problem will be addressed using a Supervised Machine Learning approach by training models based on the historical data of startups across all four categories.

## Data:

## Link to raw data(Huge JSON and Excel fiel):
        https://drive.google.com/file/d/1tWYkHYHm2HoiCajZ49Cs1K7sklWTdAbV/view

### Summary:

The data contains industry trends, investment insights and individual company information. Since the data was acquired on a trial basis, it only contains information about companies. After training the model, we predict whether startups still operating, IPO, acquired, or closed.

### Data types:

There are 196553 lines and  44 columns out of which will be used as features. The rest provide more information about the data, but will not be used for model training (like normalized name, entity id, short description etc.)

## Data Preprocessing

### A. Data Cleaning
    1. Delete irrelevant & redundant information.
    2. Remove noise or unreliable data (missing values and outliers).

### B. Date variables Transformation
    It can be divided into two successive phases.
    1. Changes in original variables
    2. Create new variables from original variables

### C. Remaining missing values handling


## Data Cleaning:
In data cleaning I removed the inappropriate & unncessary information from raw data(main data), after which I performed data cleaning involving following steps:
* Checking the percentage of NaN(null values) values present in each feature
* Removing duplicates
* Dropping columns which have NaN values.
* Remove unnecessary and corrupted data.
* Data Labelling.
