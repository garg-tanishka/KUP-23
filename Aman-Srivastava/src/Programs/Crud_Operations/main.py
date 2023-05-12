from flask import Flask, request, jsonify
from pydantic import BaseModel, validator, ValidationError
from src.operations.crud_operations import CrudOperations

main = Flask(__name__)
no_input = "No Input Provided!"


@main.route('/database_operation', methods=['GET', 'PUT', 'DELETE'])
def db_query():
    query = request.form['query']

    if not query:
        return no_input

    db_task = CrudOperations(query)

    if request.method == 'GET':
        result = db_task.get_database()
        return jsonify(result)

    elif request.method == 'PUT':
        result = db_task.create_database()
        return jsonify(result)

    elif request.method == 'DELETE':
        result = db_task.delete_database()
        return jsonify(result)

    else:
        return "invalid request!"


class DataValidation(BaseModel):
    table: str
    name: str
    age: int
    phone: int
    email: str
    emp_code: int

    @validator('table', 'name', 'age', 'phone', 'email', 'emp_code')
    def check_data(cls, values):
        if values:
            return values


@main.route('/table_operation', methods=['GET', 'PUT', 'DELETE', 'POST'])
def tables_operation():
    if request.method == 'GET':
        query = request.form['query']
        get_data = CrudOperations(query)
        result = get_data.get_table_data()
        return jsonify(result)
    elif request.method == 'PUT':
        query = request.form['query']
        get_data = CrudOperations(query)
        result = get_data.create_table()
        return jsonify(result)
    elif request.method == 'DELETE':
        query = request.form['query']
        get_data = CrudOperations(query)
        result = get_data.delete_table_data()
        return jsonify(result)

    elif request.method == 'POST':
        user_data = request.get_json()
        response = []
        try:
            for item in user_data:
                valid_query = DataValidation(**item)

                if valid_query:
                    insertion = CrudOperations(item)
                    result = insertion.insert_data()
                    response.append(result)

            return jsonify(response)

        except ValidationError as e:
            return str(e)
    else:
        return "invalid request!"


if __name__ == "__main__":
    main.run(debug=True)
