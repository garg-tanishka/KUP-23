from flask import Flask, jsonify, request

from Sanskriti.iris_classification.src.neural_network.pipeline.pipeline import Neural_Network
from Sanskriti.iris_classification.src.utils.helpers.prediction import PredictionModel

main = Flask(__name__)


@main.route('/train', methods=['GET'])
def train_model():
    run = Neural_Network()
    accuracy = run.pipeline()
    output = {}
    output['result'] = accuracy

    return jsonify(output)


@main.route('/predict', methods=['POST'])
def get_prediction():
    try:
        data = request.get_json()
        response = []
        for item in data:
            predict = PredictionModel(item)
            result = predict.get_predict()
            response.append(result)
        return jsonify(response)
    except ValueError:
        return "Invalid Input data"


if __name__ == "__main__":
    main.run(debug=True, port=9000)
