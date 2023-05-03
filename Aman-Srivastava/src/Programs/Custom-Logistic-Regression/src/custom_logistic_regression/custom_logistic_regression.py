from src.knn_classification.knn_classification import k_classifier
from src.preprocessing.preprocessing import Pre_Processing
from src.utils.constants import dataset
from sklearn.metrics import accuracy_score
from src.custom_logistic_regression.logistic_function import logistic_regression
from src.utils.helpers.backward_elimination import backward_elimination
from src.utils.helpers.predict import predict


class Logistic_Regression:

    def __init__(self):
        self.file_path = dataset

    def model_implementation(self):
        """
        Function where processed data is return after preprocessing,
        then applying logistic function and check accuracy, due to
        low accuracy choosing only significant columns using backward elimination,
        then applying KNN on that data to improve the accuracy.
        """
        data = Pre_Processing(self.file_path)
        processed_data = data.convert_dataframe()

        X_train = processed_data[0]
        X_test = processed_data[1]
        y_train = processed_data[2]
        y_test = processed_data[3]

        parameters = logistic_regression(X_train, y_train[0])
        prediction = predict(X_test, parameters)

        logistic_accuracy = accuracy_score(y_test, prediction)
        print("Accuracy using logistic function:", logistic_accuracy)

        significant_columns = backward_elimination(X_train, X_test, y_train)

        X_train_sign = significant_columns[0]
        X_test_sign = significant_columns[1]

        knn_accuracy = k_classifier(X_train_sign, X_test_sign, y_train, y_test)
        print("Accuracy using KNN Classification:", knn_accuracy)







