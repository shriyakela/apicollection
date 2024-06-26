from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained Random Forest model
model_path = 'C:/Users/Shriya.Kela/winequality/random_forest_model.pkl'
print(f"Loading model from {model_path}")
model = joblib.load(model_path)
print("Model loaded successfully")

# Define a route to handle POST requests for file upload
@app.route('/api/predict_wine_quality', methods=['POST'])
def predict_wine_quality():
    
    
    # Ensure the request contains a file in 'csv_file' key
    if 'csv_file' not in request.files:
        print("No file part in the request")
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['csv_file']
    print(f"Received file: {file.filename}")
    
    # Check if the file is a CSV file
    if file.filename.endswith('.csv'):
        try:
            print("Reading CSV file")
            # Read CSV file into pandas dataframe
            df = pd.read_csv(file)
            
            
            # Drop the 'quality' column if it exists
            if 'quality' in df.columns:
                df = df.drop(columns=['quality'])
            
            # Make predictions using the loaded model
            print("Making predictions")
            predictions = model.predict(df)
            
            # Add predictions to the dataframe
            df['predicted_quality'] = predictions
            print("Predictions added to dataframe")
            
            # Convert dataframe to JSON response
            response = df.to_dict(orient='records')
            return jsonify(response)
        
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'error': str(e)}), 500
    
    else:
        print("Uploaded file is not a CSV file")
        return jsonify({'error': 'Uploaded file is not a CSV file'}), 400

if __name__ == '__main__':
    app.run(debug=True)
