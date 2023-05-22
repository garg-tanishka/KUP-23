from flask import Flask, request, jsonify
from src.utils.helpers.predict_flower import TrainModel, PredictModel
from pydantic import BaseModel, validator, ValidationError

main = Flask(__name__)


class CommandCheck(BaseModel):
    user_input: str

    @validator('user_input')
    def check_command(cls, value):
        if value == "train":
            return value
        else:
            raise ValueError("input must be: train or Train")


@main.post("/train")
def train_model():
    try:
        user_input = request.get_json()
        response = []
        for item in user_input:
            valid = CommandCheck(user_input=item["command"])

            if valid:
                result = train(valid)
                response.append(result)

        return jsonify(response)

    except ValidationError as e:
        return str(e)


def train(item):
    train_instance = TrainModel(item)
    result = train_instance.get_model()
    return result


class FlowerParametersCheck(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    @validator('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
    def check_flower_parameters(cls, values):
        if values < 9.0:
            return values
        else:
            raise ValueError("input values are not valid please try again")


@main.post("/predict")
def predict_flower():
    try:
        flower_data = request.get_json()
        response = []
        for item in flower_data:
            valid = FlowerParametersCheck(sepal_length=item["sepal_length"], sepal_width=item["sepal_width"],
                                          petal_length=item["petal_length"], petal_width=item["petal_width"])
            if valid:
                result = predict_process(item)
                response.append(result)

        return jsonify(response)
    except ValidationError as e:
        return str(e)


def predict_process(item):
    predict_instance = PredictModel(item)
    result = predict_instance.get_predict()
    return result


if __name__ == "__main__":
    main.run(debug=True, port=5050)
