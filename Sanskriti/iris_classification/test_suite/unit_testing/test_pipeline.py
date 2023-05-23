import pandas as pd
from pandas import DataFrame
import logging
import unittest

from Sanskriti.neural_network.src.utils.constant import file_path


class Testing_Neural_Network:
    def __init__(self):
        """
        getting data from preprocessing function and calculating the accuracy of neural network
         @param dataframe
        @type dataframe
        """
        read_file = pd.read_csv(file_path)
        self.iris_dataframe = pd.DataFrame(read_file)

    def test_pre_processing(self):
        """
        getting the dataframe and pre processing it
        @param data_frame
        @return dataframe
        @rtype list
        """
        read_file = pd.read_csv(file_path)
        data_frame = pd.DataFrame(read_file)

        if isinstance(data_frame, pd.DataFrame):
            logging.info("This is a Dataframe")
        else:
            logging.info("This is not Dataframe")

    def test_target_feature(self):
        """
        getting the dataframe and dividing it into training and testing data
        @param self.dataset
        @return: dataframe
        """

        X_feature = self.iris_dataframe.drop("Species", axis=1)
        target = self.iris_dataframe["Species"]

        if len(X_feature) > 0 and ("Species" not in X_feature.columns):
            logging.info("Features Divided")
        else:
            logging.info("Features Not Divided")


class Test_class(unittest.TestCase):
    def test_for_dataframe(self):
        with self.assertLogs() as captured:
            df_check = Testing_Neural_Network()
            df_check.test_pre_processing()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "This is a Dataframe")

    def test_for_divide_features(self):
        with self.assertLogs() as captured:
            divide_check = Testing_Neural_Network()
            divide_check.test_target_feature()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Features Divided")


if __name__ == '__main__':
    unittest.main()
