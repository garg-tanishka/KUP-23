from flask import Flask, request, jsonify

from src.crud_operations.crud_operations import CrudOperations

main = Flask(__name__)


@main.route('/<param>', methods=['GET'])
def crud_operation(param):
    table_instance = CrudOperations
    result = table_instance.get_table_data()
    response = {}
    return jsonify(response)


if __name__ == "__main__":
    main.run()
