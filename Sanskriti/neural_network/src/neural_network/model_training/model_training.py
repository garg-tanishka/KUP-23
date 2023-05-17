
from Sanskriti.neural_network.src.utils.helpers.sequence import layer_creation


def training_model(data_frame):
        """
        getting the list from preprocessing function and dividing it into 4 train and test data and finding the accuracy
         of the model
         @param : list
        @return: accuracy
        """
        model = layer_creation()

        X_train = data_frame[0]
        X_test = data_frame[1]
        y_train = data_frame[2]
        y_test = data_frame[3]

        data = [model, X_train, X_test, y_train, y_test]
        return data
