from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and features
try:
    model = joblib.load('random_forest_regressor_model.joblib')
    model_features = joblib.load('model_features.joblib')
    print("Model and features loaded successfully.")
except FileNotFoundError:
    print("Error: Model or feature files not found. Please ensure 'random_forest_regressor_model.joblib' and 'model_features.joblib' are in the same directory as app.py.")
    model = None
    model_features = None

def get_prediction(data):
    if not model or not model_features:
        return None

    # Create a feature array of zeros with the same length as the model's features
    features = np.zeros(len(model_features))
    
    # Map user inputs to the correct feature indices
    try:
        input_data = {
            'AREA': data.get('area'),
            'MZZONE': data.get('mzzone'),
            'SALE_COND': data.get('sale_cond'),
            'N_BEDROOM': data.get('n_bedroom'),
            'N_BATHROOM': data.get('n_bathroom'),
            'PARK_FACIL': data.get('park_facil')
        }

        for key, value in input_data.items():
            if value:
                if key in ['N_BEDROOM', 'N_BATHROOM']:
                    feature_name = f'{key}_{value}'
                elif key == 'PARK_FACIL':
                    feature_name = f'{key}_Yes'
                else:
                    feature_name = f'{key}_{value}'

                try:
                    # Find the index of the feature in the model_features list (which is a list now)
                    feature_index = model_features.index(feature_name)
                    features[feature_index] = 1
                except ValueError:
                    print(f"Warning: Feature '{feature_name}' not found in model features. It will be treated as zero.")
                except Exception as e:
                    print(f"Unexpected error for feature '{feature_name}': {e}")
        
    except Exception as e:
        print(f"Error mapping features: {e}")
        return None
        
    prediction = model.predict([features])[0]
    return float(prediction)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not model_features:
        return jsonify({'error': 'Prediction model is not available.'}), 500
        
    try:
        data = request.json
        predicted_price = get_prediction(data)

        if predicted_price is None:
             return jsonify({'error': 'Could not process the prediction.'}), 500

        return jsonify({'price': predicted_price})
    
    except Exception as e:
        return jsonify({'error': 'Could not process the prediction.'}), 500

if __name__ == '__main__':
    app.run(debug=True)