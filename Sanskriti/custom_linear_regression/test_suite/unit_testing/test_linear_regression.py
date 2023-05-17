import logging
import unittest

import pandas as pd

from Sanskriti.custom_linear_regression.src.utils.constant import file_path


class Test_Custom_Linear_Regression:
    def __init__(self):
        """
        getting data from preprocessing function and calculating the accuracy of linear regression
         @param dataframe
        @type dataframe
        """
        self.dataset = pd.read_csv(file_path)
        self.data_frame = pd.DataFrame(self.dataset)

    def test_pre_processing(self):
        """
        getting the dataframe and pre-processing it and splitting it into training and testing data
        :param dataframe
        :return list[X_train,X_test,y_train,y_test]
        @param data_frame:
        """

        X = self.data_frame.iloc[:, 0].values
        y = self.data_frame.iloc[:, 1].values
        length_X = X.shape[0]

        if length_X == 200:
            logging.info("Dataframe is in right length")
        else:
            logging.info("Dataframe is in wrong length")


class Test_class(unittest.TestCase):
    def test_pre_processing(self):
        with self.assertLogs() as captured:
            call_fun = Test_Custom_Linear_Regression()
            call_fun.test_pre_processing()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Dataframe is in right length")
