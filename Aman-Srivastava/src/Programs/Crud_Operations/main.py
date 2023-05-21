from flask import Flask, request, jsonify
from pydantic import BaseModel, validator
from src.operations.crud_operations import CrudOperations
from src.operations.databse_operations import DatabaseOperations

main = Flask(__name__)
invalid_input = "Invalid input please try again"
negative_value = "Negative values are not allowed"


class DataValidation(BaseModel):
    name: str
    age: int
    phone: int
    email: str
    emp_code: int

    @validator('name', 'email')
    def check_string_values(cls, value):
        if not isinstance(value, str):
            raise ValueError("Only string values are allowed")
        return value

    @validator('age', 'phone', 'emp_code')
    def check_positive_integers(cls, value):
        if value < 0:
            raise ValueError("Negative integer value not allowed")
        return value


class EmpIdValidation(BaseModel):
    emp_id: int

    @validator('emp_id')
    def check_negative_values(cls, value):
        if value < 0:
            raise ValueError(negative_value)
        return value


class DbQueryValidation(BaseModel):
    db_query: str

    @validator('db_query')
    def check_negative_values(cls, value):
        if value == "database":
            return value
        else:
            raise ValueError(negative_value)


@main.route('/database/<param1>', methods=['GET'])
def get_db(param1):
    try:
        db_operation = DatabaseOperations()
        value = DbQueryValidation(db_query=param1)
        if value.db_query:
            result = db_operation.get_database()
            return jsonify(result)
    except ValueError:
        return invalid_input, 400


@main.route('/database/<param1>/<param2>', methods=['PUT'])
def create_db(param1, param2):
    try:
        db_operation = DatabaseOperations()
        value = DbQueryValidation(db_query=param1)
        if value.db_query:
            result = db_operation.create_database(param2)
            return jsonify(result)
    except ValueError:
        return invalid_input, 400


@main.route('/database/<param1>/<param2>', methods=['DELETE'])
def delete_db(param1, param2):
    try:
        db_operation = DatabaseOperations()
        value = DbQueryValidation(db_query=param1)
        if value.db_query:
            result = db_operation.delete_database(param2)
            return jsonify(result)
    except ValueError:
        return invalid_input, 400


@main.route('/knoldus/<value>', methods=['GET'])
def get_employee_data(value):
    operation = CrudOperations()
    if value == "table":
        result = operation.get_tables_data()
        return jsonify(result)
    else:
        try:
            value = int(value)
            value = EmpIdValidation(emp_id=value)
            result = operation.get_individual_entries(value.emp_id)
            return jsonify(result)

        except ValueError:
            return invalid_input, 400


@main.route('/knoldus/<value>', methods=['PUT'])
def put_employee_data(value):
    try:
        value = int(value)
        value = EmpIdValidation(emp_id=value)
        user_data = request.get_json()
        response = []
        try:
            for item in user_data:
                valid_data = DataValidation(**item)
                insertion = CrudOperations()
                result = insertion.update_table_entries(value.emp_id, item)
                response.append(result)

            return jsonify(response)

        except ValueError:
            return invalid_input, 400

    except ValueError:
        return invalid_input, 400


@main.route('/knoldus/<value>', methods=['POST'])
def create_entries(value):
    user_data = request.get_json()
    response = []
    if value == "table":
        try:
            for item in user_data:
                valid_data = DataValidation(**item)
                insertion = CrudOperations()
                result = insertion.update_table(item)
                response.append(result)
            return jsonify(response)

        except ValueError:
            return invalid_input, 400

    else:
        return invalid_input, 400


@main.route('/knoldus/<value>', methods=['DELETE'])
def delete_entries(value):
    operation = CrudOperations()

    if value == "table":
        result = operation.delete_all_entries()
        return jsonify(result)
    else:
        try:
            value = int(value)
            value = EmpIdValidation(emp_id=value)
            result = operation.delete_individual_entries(value.emp_id)
            return jsonify(result)

        except ValueError:
            return invalid_input, 400


if __name__ == "__main__":
    main.run(debug=True)
