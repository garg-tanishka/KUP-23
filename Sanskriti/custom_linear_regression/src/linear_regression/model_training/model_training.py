import numpy as np
import pandas as pd
from keras.losses import mean_squared_error
from sklearn.metrics import r2_score
from src.linear_regression.pre_processing.processing import pre_processing
from src.utils.constant import file_path

dataset = pd.read_csv(file_path,encoding='latin-1')


def get_mean(arr):
    return np.sum(arr) / len(arr)


def get_variance(arr, mean):
    return np.sum((arr - mean) ** 2)


def get_covariance(x, mean_x, y, mean_y):
    covar = 0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    print(covar)
    return covar



def get_coefficients(x, y):
    n = len(x)
    x_mean = x.mean()
    y_mean = y.mean()

    m = get_covariance(x, x_mean, y, y_mean) / get_variance(x, x_mean)
    b = y_mean - x_mean * m
    return m, b
    # numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    # denominator = sum((x[i] - x_mean) ** 2 for i in range(n))
    # slope = numerator / denominator
    # intercept = y_mean - slope * x_mean
    # print(slope)
    # print(intercept)
    # return slope, intercept


def training_linear_regression(scaled_data):
    X_train = scaled_data[0]
    X_test = scaled_data[1]
    y_train = scaled_data[2]
    y_test = scaled_data[3]
    prediction = []
    m, b = get_coefficients(X_train, y_train)
    for x in X_test:
        y = m * x + b
        prediction.append(y)
    r2 = r2_score(prediction, y_test)
    mse = mean_squared_error(prediction, y_test)
    print("The R2 score of the model is: ", r2)
    print("The MSE score of the model is: ", mse)
    return prediction



