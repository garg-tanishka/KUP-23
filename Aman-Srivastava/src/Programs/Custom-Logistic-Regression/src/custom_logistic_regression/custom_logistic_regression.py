from src.knn_classification.knn_classification import k_classifier
from src.preprocessing.preprocessing import PreProcessing
from src.utils.constants import dataset
from sklearn.metrics import accuracy_score
from src.custom_logistic_regression.logistic_function import logistic_regression
from src.utils.helpers.backward_elimination import backward_elimination
from src.utils.helpers.confusion_matrix import check_confusion
from src.utils.helpers.predict import predict


class LogisticRegression:

    def __init__(self):
        self.file_path = dataset

    def model_implementation(self):
        """
        Function where processed data is return after preprocessing,
        then applying logistic function and check accuracy, due to
        low accuracy choosing only significant columns using backward elimination,
        then applying KNN on that data to improve the accuracy.
        """
        data = PreProcessing(self.file_path)
        processed_data = data.convert_dataframe()

        x_train = processed_data[0]
        x_test = processed_data[1]
        y_train = processed_data[2]
        y_test = processed_data[3]

        significant_columns = backward_elimination(x_train, x_test, y_train)

        x_train_sign = significant_columns[0]
        x_test_sign = significant_columns[1]

        knn_accuracy = k_classifier(x_train_sign, x_test_sign, y_train, y_test)
        return knn_accuracy
