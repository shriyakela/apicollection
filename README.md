# Wine Quality Prediction Flask API

This Flask project provides an API for predicting wine quality based on certain features using a Random Forest model.
## Prerequisites
- Python 3.8
- Postman


## Setup

1. Clone the repository:
   ```bash
   git clone  https://github.com/shriyakela/apicollection.git
   cd flask-project
## Run
Install the necessary dependencies with pip install -r requirements.txt, then run the Flask application using python app.py. 

  ## API Endpoints

Predict Wine Quality
URL: /api/predict_wine_quality
Method: POST
Description: Upload a CSV file to predict wine quality.
Request Body
csv_file (file): The CSV file containing wine features.
Example Request (using Postman)
Open Postman.
Create a new POST request.
Set the URL to http://127.0.0.1:5000/api/predict_wine_quality.
In the Body tab, select form-data.
Add a key csv_file with type File and choose your CSV file.
Send the request.
CSV Format
The CSV file should contain the following features required by the model, excluding the target variable quality if it exists:

fixed acidity
volatile acidity
citric acid
residual sugar
chlorides
free sulfur dioxide
total sulfur dioxide
density
pH
sulphates
alcohol
