import numpy as np


def logistic_regression(x_train, y, learning_rate=0.01, num_iterations=1000):
    no_of_training = x_train.shape[0]
    no_of_features = x_train.shape[1]
    weights = np.zeros((no_of_features, 1))
    bias = 0

    # Gradient descent
    for i in range(num_iterations):
        # Calculate hypothesis
        z = np.dot(x_train, weights) + bias
        hypothesis = 1 / (1 + np.exp(-z))

        # Calculate cost function
        cost = (-1 / no_of_training) * np.sum(y * np.log(hypothesis) + (1 - y) * np.log(1 - hypothesis))
        # print(cost)

        # Calculate gradients
        dz = hypothesis - y
        dw = (1 / no_of_training) * np.dot(x_train.T, dz)
        db = (1 / no_of_training) * np.sum(dz)

        # Update parameters
        weights -= learning_rate * dw
        bias -= learning_rate * db

    # Return final parameters
    parameters = {"weights": weights, "bias": bias}
    return parameters
