from tensorflow import keras
import numpy as np

model = keras.models.load_model('models/sentiment_nn_model.keras')


def predict(X):
    """Execute the model to predict sentiment of text

    Args:
        X (list): The text to predict (post text feature engineering)

    Returns:
        dict: A dictionary containing the predicted sentiment and its confidence
    """

    predicted = model.predict(X)
    predicted = predicted[0]
    if predicted[0] > predicted[1]:
        result = {
            'sentiment': 'negative',
            'confidence': np.float64(predicted[0])
        }
    else:
        result = {
            'sentiment': 'positive',
            'confidence': np.float64(predicted[1])
        }
        
    return result
