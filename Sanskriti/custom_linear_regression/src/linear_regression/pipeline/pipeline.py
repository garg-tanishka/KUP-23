from src.linear_regression.model_training.model_training import training_linear_regression
from src.utils.constant import file_path
import pandas as pd
from src.linear_regression.pre_processing.processing import pre_processing


class Custom_Linear_Regression:
    def __init__(self):
        """
        getting data from preprocessing function and calculating the accuracy of linear regression
         @param dataframe
        @type dataframe
        """
        self.dataset = pd.read_csv(file_path, encoding='latin-1')
        self.data_frame = pd.DataFrame(self.dataset)
        self.pipeline()

    def pipeline(self):
        """
        getting the dataframe and calling all the steps in building the model
        @return: accuracy
        """
        processed_dataframe = pre_processing(self.dataset)
        trained_model = training_linear_regression(processed_dataframe)
