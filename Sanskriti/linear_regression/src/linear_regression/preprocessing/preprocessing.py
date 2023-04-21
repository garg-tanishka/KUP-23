import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

from src.utils.constant import file_path

class apply_linear_regression:
    def __init__(self, file_path):
        """
        getting dataframe from main function and setting its reference
         @param dataframe
        @type knolder_id: integer
        """
        dataset = pd.read_csv(file_path)
        self.data_frame = DataFrame(dataset)
        self.file_path = file_path
        self.create_graph_individual()
