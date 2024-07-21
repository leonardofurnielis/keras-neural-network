import pickle

model = pickle.load(open('models/credit_risk_model.pickle', 'rb'))


def predict(input_data):
    """
    Args:
        input_data (list): input values to predict
    Returns:
        dict: A dictionary containing the predicted response of machine learning model
    """

    predicted_values = model.predict(input_data)
    predicted_probability = model.predict_proba(input_data)

    output_data = []

    for i, value in enumerate(input_data):
        if predicted_values[i] == 'No Risk':
            output_data.append(["No Risk", predicted_probability[i].tolist()])
        if predicted_values[i] == 'Risk':
            output_data.append(["Risk", predicted_probability[i].tolist()])

        
    return {
                "fields": [ "prediction", "probability" ],
                "values": output_data
            }
