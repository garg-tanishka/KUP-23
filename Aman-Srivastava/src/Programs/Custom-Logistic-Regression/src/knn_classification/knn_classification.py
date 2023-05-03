from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from src.utils.helpers.confusion_matrix import check_confusion
import numpy as np


def k_classifier(X_train, X_test, y_train, y_test):
    error_rate = []
    for i in range(1, 40):
        knn = KNeighborsClassifier(n_neighbors=i, metric='minkowski', p=2)
        knn.fit(X_train, y_train)
        pred_i_knn = knn.predict(X_test)
        error_rate.append(np.mean(pred_i_knn != y_test))

    # plt.figure(figsize=(10, 6))
    # plt.plot(range(1, 40), error_rate, color='blue', linestyle='dashed',
    #          marker='o', markerfacecolor='red', markersize=10)
    # plt.title('Error Rate vs. K Value')
    # plt.xlabel('K')
    # plt.ylabel('Error Rate')
    # plt.show()

    knn_classifier = KNeighborsClassifier(n_neighbors=1, metric='minkowski', p=2)
    knn_classifier.fit(X_train, y_train)
    y_pred_knn = knn_classifier.predict(X_test)
    check_knn_cm = check_confusion(y_test, y_pred_knn, 'KNN Confusion Matrix')
    score = accuracy_score(y_test, y_pred_knn)
    return score
