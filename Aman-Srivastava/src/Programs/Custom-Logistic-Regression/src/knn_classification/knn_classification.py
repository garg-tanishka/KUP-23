from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from src.utils.helpers.confusion_matrix import check_confusion
import numpy as np


def k_classifier(x_train, x_test, y_train, y_test):
    error_rate = []
    for i in range(1, 40):
        knn = KNeighborsClassifier(n_neighbors=i, metric='minkowski', p=2)
        knn.fit(x_train, y_train)
        pred_i_knn = knn.predict(x_test)
        error_rate.append(np.mean(pred_i_knn != y_test))

    knn_classifier = KNeighborsClassifier(n_neighbors=1, metric='minkowski', p=2)
    knn_classifier.fit(x_train, y_train)
    y_pred_knn = knn_classifier.predict(x_test)
    score = accuracy_score(y_test, y_pred_knn)
    return score
