import pandas as pd

from src.linear_regression.pipeline.constant import file_path
from src.linear_regression.preprocessing.processing import pre_processing


class Linear_Regression:
    def __init__(self):
        """
        getting dataframe from main function and setting its reference
         @param dataframe
        @type dataframe
        """
        self.dataset = pd.read_csv(file_path, encoding='latin-1')
        self.data_frame = pd.DataFrame(self.dataset)
        self.processed = pre_processing(self.data_frame)









