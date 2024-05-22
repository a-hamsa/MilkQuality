from flask import Flask, request, jsonify, render_template
import joblib

# # Load the trained model
# model = joblib.load('model_MooQ_dt.pkl')

# # Initialize the Flask app
# app = Flask(__name__, static_url_path='/templates/assets', static_folder='static')

# @app.route('/')
# def serve_index():
#     return render_template('/index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     features = [
#         data['ph_value'],
#         data['temperature'],
#         data['taste'],
#         data['odor'],
#         data['fat'],
#         data['turbidity'],
#         data['colour']
#     ]
#     prediction = model.predict([features])
#     return jsonify({'grade': prediction[0]})


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Your prediction logic goes here
    return jsonify({'grade': 'A'})  # Placeholder response

if __name__ == '__main__':
    app.run(debug=True)
