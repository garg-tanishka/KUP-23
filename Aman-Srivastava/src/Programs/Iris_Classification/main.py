from flask import Flask, request, jsonify
from src.utils.helpers.predict_flower import TrainModel, PredictModel
from pydantic import BaseModel, ValidationError

main = Flask(__name__)


@main.post("/train")
def train_model():
    user_input = request.get_json()
    response = []
    for item in user_input:
        result = train(item)
        response.append(result)
    return jsonify(response)


def train(item):
    train_instance = TrainModel(item)
    result = train_instance.get_model()
    return result


@main.post("/predict")
def predict_flower():
    flower_data = request.get_json()
    response = []
    for item in flower_data:
        result = predict_process(item)
        response.append(result)
    return jsonify(response)


def predict_process(item):
    predict_instance = PredictModel(item)
    result = predict_instance.get_predict()
    return result


if __name__ == "__main__":
    main.run(debug=True, port=5050)
