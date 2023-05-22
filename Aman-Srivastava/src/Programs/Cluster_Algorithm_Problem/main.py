from src.k_means_clustering.pipeline.pipeline import CustomerSegmentation
from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError, validator


class QueryParams(BaseModel):
    query: str

    @validator('query')
    def validate_input(cls, value):
        if value.isdigit():
            raise ValueError('Integer values are not allowed for "input" field')
        elif value != "train":
            raise ValueError('Invalid Input! Please Try: input')
        else:
            return value


main = Flask(__name__)


@main.route('/', methods=['POST'])
def process_data():
    try:
        form_data = QueryParams(**request.form)
    except ValidationError as e:
        errors = []
        for error in e.errors():
            errors.append({
                'field': error['loc'][0],
                'message': error['msg']
            })
        return jsonify({'errors': errors}), 400

    response = []
    input_query = form_data.query
    model_trigger = CustomerSegmentation(input_query)
    result = model_trigger.get_trained_model()
    response.append(result)
    return jsonify(response), 200


if __name__ == "__main__":
    main.run(debug=True)
