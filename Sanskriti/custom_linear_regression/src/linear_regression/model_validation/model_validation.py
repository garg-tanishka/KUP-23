from matplotlib import pyplot as plt
from sklearn.metrics import r2_score


def model_validation(data_frame):
    y_predict = data_frame[0]
    y_test = data_frame[1]
    r2 = r2_score(y_predict, y_test)
    return r2
