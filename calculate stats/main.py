from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

def calculate_stats(df):
    # Calculate sum, average, and standard deviation for each subject
    stats = {}
    subjects = df.columns[1:]  # Assuming first column is Roll No

    for subject in subjects:
        stats[subject] = {
            'sum': df[subject].sum().astype(str),
            'average': df[subject].mean().astype(str),
            'std_deviation': df[subject].std().astype(str)
        }

    return stats

@app.route('/api/calculate', methods=['POST'])
def calculate():
    print(request)
    print(request.files)

    try:
        if 'csv_file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        
        file = request.files['csv_file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and file.filename.endswith('.csv'):
            # Read CSV file into pandas dataframe
            df = pd.read_csv(file)

            # Check if DataFrame has expected columns
           # expected_columns = ['Roll No', 'English', 'Maths', 'Phy', 'Chem', 'Bio']
            #if not all(col in df.columns for col in expected_columns):
                #return jsonify({'error': 'CSV file does not have expected columns: Roll No, English, Maths, Phy, Chem, Bio'}), 400

            # Calculate statistics
            stats = calculate_stats(df)

            return jsonify(stats)
        
        else:
            return jsonify({'error': 'Uploaded file is not a CSV file or does not have .csv extension'}), 400
    
    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
