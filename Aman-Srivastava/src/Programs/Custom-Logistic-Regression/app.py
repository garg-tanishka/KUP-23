from src.custom_logistic_regression.custom_logistic_regression import LogisticRegression
from flask import Flask

app = Flask(__name__)


@app.route('/')
def logistic_regression():
    run = LogisticRegression()
    score = run.model_implementation()
    return str(score)


if __name__ == "__main__":
    app.run(debug=True)
