from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model("models/phishing_model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url_features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(url_features)
    result = "Phishing" if prediction[0] > 0.5 else "Legitimate"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
