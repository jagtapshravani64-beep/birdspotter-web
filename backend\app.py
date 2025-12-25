from flask import Flask, request, jsonify
from model import predict_bird

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    result = predict_bird(file)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
