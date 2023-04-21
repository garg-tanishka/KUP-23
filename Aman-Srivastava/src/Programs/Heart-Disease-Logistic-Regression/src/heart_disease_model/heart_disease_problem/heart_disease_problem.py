import pandas as pd
from heart_disease_model.pre_processing.pre_processing import pre_processing
from src.utils.constants import dataset_path
from sklearn.linear_model import LogisticRegression


class Heart_Disease:

    def __init__(self):
        self.readfile = pd.read_csv(dataset_path)
        self.model_preparation()

    def model_preparation(self):
        processed_data = pre_processing(self.readfile)
        print(processed_data)









