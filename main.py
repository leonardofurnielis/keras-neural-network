import os
import json
import uuid
import certifi

from flask_cors import CORS
from flask import Flask, request
from ibm_watson_openscale import APIClient
from ibm_watson_openscale.supporting_classes.payload_record import PayloadRecord
from ibm_watson_openscale.utils import IAMAuthenticator

from utils.prediction import predict

os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return 'Flask is running!'


@app.route('/api/v1/predict', methods=['POST'])
def __predict__():
    request_data = request.get_json(force=True)
    input_data = request_data.get('values')
    input_fields = request_data.get("fields")

    if (input_data is None) or (input_fields is None):
        request_data = request_data['input_data'][0]
        input_data = request_data.get('values')
        input_fields = request_data.get('fields')

    if input_data is None: 
        response = app.response_class(response=json.dumps({"error": "Invalid request syntax, `input_data` is required`"}),
                                  status=400,
                                  mimetype='application/json')
    else:
        wos_payload_logging_data = {"fields": input_fields, "values": input_data}
        predicted_values = predict(input_data)
        response = app.response_class(response=json.dumps(predicted_values),
                                  status=200,
                                  mimetype='application/json')

        payload_logging(wos_payload_logging_data, predicted_values)
        
    return response


def payload_logging(payload_scoring, scoring_response):
    authenticator = IAMAuthenticator(apikey="<API_KEY>",
                                     disable_ssl_verification=True)
    wos_client = APIClient(authenticator=authenticator)

    scoring_id = str(uuid.uuid4())
    records_list = []

    pl_record = PayloadRecord(scoring_id=scoring_id, request=payload_scoring, response=scoring_response,
                              response_time=int(460))
    records_list.append(pl_record)
    wos_client.data_sets.store_records(data_set_id="<DATA_SET_ID>", request_body=records_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=3000)
