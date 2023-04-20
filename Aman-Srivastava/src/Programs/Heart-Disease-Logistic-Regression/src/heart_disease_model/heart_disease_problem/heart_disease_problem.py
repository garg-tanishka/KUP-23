import pandas as pd
from heart_disease_model.pre_processing.pre_processing import pre_processing
from src.utils.constants import dataset_path


class Heart_Disease:

    def __init__(self, user_input):
        self.user_input = user_input
        self.readfile = pd.read_csv(dataset_path)
        self.processing_data()

    def processing_data(self):
        if self.user_input == "Check":
            val = pre_processing(self.readfile)
            print(val)






