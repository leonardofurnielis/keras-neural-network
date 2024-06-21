import os
import json

from flask_cors import CORS
from flask import Flask, request
from utils.prediction import predict

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return 'Flask is running!'


@app.route('/api/v1/predict', methods=['POST'])
def __predict__():
    request_data = request.get_json(force=True)
    input_data = request_data['values']

    if input_data is None: 
        input_data = request_data['input_data'][0]
        input_data = input_data['values']

    if input_data is None: 
        response = app.response_class(response=json.dumps({"error": "Invalid request syntax"}),
                                  status=400,
                                  mimetype='application/json')
    else:
        output = predict(input_data)
        response = app.response_class(response=json.dumps(output),
                                  status=200,
                                  mimetype='application/json')
        
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=3000)
