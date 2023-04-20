import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def selecting_features(heart_data):
    training_features = heart_data.columns.unique()
    return training_features


def pre_processing(heart_data):
    """
    Dropping Education column from dataset because it has no effect on target
    @param heart_data: CSV_DATA
    @return: dataframe
    """
    heart_data = pd.DataFrame(heart_data)
    heart_data = heart_data.drop("education", axis=1)
    features = selecting_features(heart_data)
    return features
