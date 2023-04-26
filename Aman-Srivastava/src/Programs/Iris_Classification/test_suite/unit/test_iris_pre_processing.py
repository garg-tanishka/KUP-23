import logging
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
import unittest

from src.utils.constants import dataset_path


class Testing_pre_processing:
    def __init__(self):
        self.y_target = None
        self.X_feature = None
        read_file = pd.read_csv(dataset_path)
        self.iris_dataframe = pd.DataFrame(read_file)

    def test_pre_processing(self):
        """
        Function to read csv file and convert that into dataframe,
        @param self.dataset_path: iris_csv_file
        @return: dataframe[X_train, X_test, y_train, y_test]
        @rtype: list
        """
        read_file = pd.read_csv(dataset_path)
        iris_dataframe = pd.DataFrame(read_file)
        if isinstance(iris_dataframe, pd.DataFrame):
            logging.info("This is Dataframe")
        else:
            logging.info("This is not Dataframe")

    def test_divide_feature_target(self):
        """
        Function to divide features and target and also split them,
        @return: dataframe[X_features, X_test, y_train, y_test]
        @rtype: list
        """
        df = self.iris_dataframe
        self.X_feature = df.drop(["Species", "Id"], axis=1)
        self.y_target = df["Species"]

        if len(self.X_feature) > 0 and ("Species" not in self.X_feature.columns):
            logging.info("Features Divided")
        else:
            logging.info("Features Not Divided")


class Test_class(unittest.TestCase):
    def test_for_dataframe(self):
        with self.assertLogs() as captured:
            df_check = Testing_pre_processing()
            df_check.test_pre_processing()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "This is Dataframe")

    def test_for_divide_features(self):
        with self.assertLogs() as captured:
            divide_check = Testing_pre_processing()
            divide_check.test_divide_feature_target()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Features Divided")


if __name__ == '__main__':
    unittest.main()
