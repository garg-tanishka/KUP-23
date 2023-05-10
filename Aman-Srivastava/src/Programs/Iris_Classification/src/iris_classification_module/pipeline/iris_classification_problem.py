from src.iris_classification_module.pre_processing.iris_pre_processing import pre_processing
from src.utils.constants import dataset_path
from src.utils.helpers.sequence_creation import layer_creation


class Iris_Classification:

    def __init__(self):
        self.data_set = dataset_path
        self.model_pipeline()

    def model_pipeline(self):
        pre_processed_data = pre_processing(self.data_set)
        model = layer_creation()

        X_train = pre_processed_data[0]
        X_test = pre_processed_data[1]
        y_train = pre_processed_data[2]
        y_test = pre_processed_data[3]

        if model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20):
            print("Trained Successfully")
        else:
            print("Task Failed Please Check")

