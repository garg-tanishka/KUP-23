import pandas as pd
from heart_disease_model.pre_processing.pre_processing import pre_processing
from src.utils.helpers.backward_elimination import backward_elimination
from src.utils.helpers.K_Classification import k_classifier
from src.utils.constants import dataset_path


class Heart_Disease:
    def __init__(self):
        self.processed_data = pre_processing(dataset_path)
        self.apply_model()

    def apply_model(self):
        """
        Applying backward-elimination to get only significant columns,
        and then KNN Classification algorithm.
        """
        X_train = self.processed_data[0]
        X_test = self.processed_data[1]
        y_train = self.processed_data[2]
        y_test = self.processed_data[3]

        significant_X_train_test = backward_elimination(X_train, X_test, y_train, y_test)

        X_train_sign = significant_X_train_test[0]
        X_test_sign = significant_X_train_test[1]

        k_classifier(X_train_sign, X_test_sign, y_train, y_test)
