from Sanskriti.iris_classification.src.neural_network.model_validation.model_validation import validation
from Sanskriti.iris_classification.src.neural_network.pre_processing.processing import pre_processing
from Sanskriti.iris_classification.src.neural_network.model_training.model_training import training_model
from Sanskriti.iris_classification.src.utils.constant import file_path



class Neural_Network:
    def __init__(self):
            """
            getting data from preprocessing function and calculating the accuracy of neural network
            @param dataframe
            @type dataframe
            """
            self.dataset = file_path

    def pipeline(self):
            """
            getting the dataframe and calling all the steps in building the model
            @return: accuracy
            """
            processed_dataframe = pre_processing(self.dataset)

            trained_model = training_model(processed_dataframe)
            accuracy = validation(trained_model)
            return accuracy


