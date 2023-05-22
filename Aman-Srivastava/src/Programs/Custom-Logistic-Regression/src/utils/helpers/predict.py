import numpy as np


def predict(x_test_sign, parameters):
    weights = parameters["weights"]
    bias = parameters["bias"]
    z = np.dot(x_test_sign, weights) + bias
    hypothesis = 1 / (1 + np.exp(-z))
    predictions = (hypothesis > 0.5).astype(int)
    return predictions
