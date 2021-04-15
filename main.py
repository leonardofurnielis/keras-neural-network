import json
from flask_cors import CORS
from flask import Flask, request
from flask_restful import Api
import os
import json
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from src.preprocessing import pre_processing
from src.prediction import model_predict

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route("/")
def index():
    return 'Flask is running!'


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    input_text = pre_processing(request.json.get('text'))
    output = model_predict(input_text)

    response = app.response_class(response=json.dumps(output),
                                  status=200,
                                  mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')