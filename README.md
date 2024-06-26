# Wine Quality Prediction Flask API

This Flask project provides an API for predicting wine quality based on certain features using a pre-trained Random Forest model.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-project.git
   cd flask-project
                Install the dependencies:


pip install -r requirements.txt
                Run the Flask application:

python app.py
                API Endpoints
  
Predict Wine Quality
URL: /api/predict_wine_quality
Method: POST
Description: Upload a CSV file to predict wine quality.
Request Body: csv_file (file)
              Example Request (Postman)
Open Postman.
Create a new POST request.
Set the URL to http://127.0.0.1:5000/api/predict_wine_quality.
In the Body tab, select form-data.
Add a key csv_file with type File and choose your CSV file.
Send the request.
             Example CSV Format
The CSV file should contain the features required by the model, excluding the target variable quality if it exists. Example:
fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol
7.4,0.7,0,1.9,0.076,11,34,0.9978,3.51,0.56,9.4
6.3,0.3,0.34,1.6,0.049,14,132,0.994,3.3,0.49,9.5

