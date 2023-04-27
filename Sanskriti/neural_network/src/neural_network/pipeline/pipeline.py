from src.utils.constant import file_path
import pandas as pd

from Sanskriti.neural_network.src.neural_network.pre_processing.processing import pre_processing


class Neural_Network:

    def __init__(self):
        """
        getting data from pre processing function and calculating the accuracy of the model using random forest
         @param dataframe
        @type dataframe
        """
        self.dataset = pd.read_csv(file_path)
        self.training_model()

    def training_model(self):
        """
        getting the list from pre processing function and dividing it into 4 train and test data and finding the accuracy
         of the model
         @param : list
        @return: accuracy
        """
        processed_data = pre_processing(self.dataset)


