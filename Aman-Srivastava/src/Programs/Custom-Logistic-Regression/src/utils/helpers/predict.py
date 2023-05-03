import numpy as np


def predict(X_train, parameters):
    weights = parameters["weights"]
    bias = parameters["bias"]
    z = np.dot(X_train, weights) + bias
    hypothesis = 1 / (1 + np.exp(-z))
    predictions = (hypothesis > 0.5).astype(int)
    return predictions
