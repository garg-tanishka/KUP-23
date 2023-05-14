
def linear_regression(data_frame):
    X_train = data_frame[0]
    X_test = data_frame[1]
    y_train = data_frame[2]
    y_test = data_frame[3]
    num = 0
    den = 0
    for i in range(len(X_train)):
        x_mean = X_train.mean()
        y_mean = y_train.mean()

        num = num + ((X_train[i] - x_mean) * (y_train[i] - y_mean))
        den = den + ((X_train[i] - x_mean) * (X_train[i] - x_mean))

    m = num / den
    b = y_train.mean() - (m * X_train.mean())
    y_predict = m * X_test + b

    validation = [y_predict, y_test]

    return validation
