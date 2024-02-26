import os
import json
import pickle
from flask_cors import CORS
from flask import Flask, request
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from utils.prediction import predict
from utils.preprocessing import tokenization, remove_stop_words, stem_porter, rejoin_words, word2vec_tfidf

app = Flask(__name__)
CORS(app)
tfidf_vectorizer = pickle.load(open('models/tfidf_text_vectorizer.pickle', 'rb'))

@app.route("/")
def index():
    return 'Flask is running!'


@app.route('/api/v1/predict', methods=['POST'])
def __predict__():
    """
    Args:
        text (str): The text to be predicted

    Returns:
        dict: The result of predictin and it's confidence
    """
    input_text = request.json.get('text')

    input_tokens = tokenization(input_text)
    input_tokens = remove_stop_words(input_tokens)
    input_tokens = stem_porter(input_tokens)
    input_text_cleaned = rejoin_words(input_tokens)

    input_vector = word2vec_tfidf(tfidf_vectorizer, input_text_cleaned)

    output = predict(input_vector)

    response = app.response_class(response=json.dumps(output),
                                  status=200,
                                  mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=3000)
