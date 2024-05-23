import pickle

model = pickle.load(open('models/credit_risk_model.pickle', 'rb'))


def predict(input_data):
    """
    Args:
        input_data (list): input values to predict

    Returns:
        dict: A dictionary containing the predicted response of machine learning model
    """

    predict = model.predict(input_data)
    proba = model.predict_proba(input_data)

    output_data = []

    for i, value in enumerate(input_data):
        if predict[i] == 'No Risk':
            output_data.append(["No Risk", proba[i].tolist()])
        if predict[i] == 'Risk':
            output_data.append(["Risk", proba[i].tolist()])

        
    return  {
                "fields": [ "prediction", "probability" ],
                "values": output_data
            }
