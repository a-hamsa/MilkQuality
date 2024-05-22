from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__, static_folder='static')
model = joblib.load('model_MooQ_dt.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        ph_value = float(request.form['ph_value'])
        temperature = float(request.form['temperature'])
        taste = int(request.form['taste'])
        odor = int(request.form['odor'])
        fat = int(request.form['fat'])
        turbidity = int(request.form['turbidity'])
        colour = int(request.form['colour'])

        features = np.array([[ph_value, temperature, taste, odor, fat, turbidity, colour]])
        prediction = model.predict(features)

        # Convert prediction to a standard Python int
        prediction_int = int(prediction[0])

        return jsonify({'gradeOutput': prediction_int})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
