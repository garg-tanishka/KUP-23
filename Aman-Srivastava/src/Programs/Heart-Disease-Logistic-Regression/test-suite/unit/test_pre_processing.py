import logging
import pandas as pd
from src.utils.constants import dataset_path
import unittest


class Test_heart_disease_problem:

    def __init__(self):
        self.csv_file = dataset_path
        self.test_pre_processing()

    def test_calculate_correlation(self):

        threshold = 0.7
        col_correlation = set()
        corr_matrix = self.dataframe.corr()
        for i in range(len(corr_matrix.columns)):
            for j in range(i):
                if (corr_matrix.iloc[i, j]) > threshold:
                    column_name = corr_matrix.columns[i]
                    col_correlation.add(column_name)

        if len(col_correlation) > 0:
            logging.info("Correlated Columns Assigned")
        else:
            logging.info("No Columns Assigned")

    def test_divide_feature_target(self):

        self.X_features = self.dataframe.drop("TenYearCHD", axis=1)
        self.y_target = self.dataframe["TenYearCHD"]

        if len(self.X_features) > 0 & ("TenYearCHD" not in self.X_features.columns):
            logging.info("X features divided and Y target also")
        else:
            logging.info("Not divided properly")

    def test_fill_null_values(self):
        """
        Filling columns having null values with its means values.
        @param self.dataframe: heart_dataframe
        @return: dataframes[X_train_scaled, X_test_scaled, y_train, y_test]
        @rtype: list
        """
        columns_with_null = ["education", "cigsPerDay", "BPMeds", "totChol", "BMI", "glucose", "heartRate"]
        for i in columns_with_null:
            self.dataframe[i].fillna(self.dataframe[i].mean(), inplace=True)

        if self.dataframe.isnull().any().any():
            logging.info("Null Exists!")
        else:
            logging.info("No Null Exists")

    def test_pre_processing(self):
        """
        Doing all the pre-processing of data:
        Cleaning,Filling,Feature_Selection etc.
        @param self.csv_file : heart_data_csv
        @return: heart_data after pre-processing
        @rtype: dataframe
        """
        readfile = pd.read_csv(self.csv_file)
        heart_data = pd.DataFrame(readfile)
        self.dataframe = heart_data

        if isinstance(heart_data, pd.DataFrame):
            logging.info("This is Dataframe")
        else:
            logging.info("This is Not Dataframe")


class Test_Class(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def test_for_dataframe(self):
        with self.assertLogs() as captured:
            class_call = Test_heart_disease_problem()
            class_call.test_pre_processing()
        self.assertEqual(len(captured.records), 2)
        self.assertEqual(captured.records[0].getMessage(), "This is Dataframe")

    def test_for_filled_null(self):
        with self.assertLogs() as captured:
            test_df = Test_heart_disease_problem()
            test_df.test_fill_null_values()
        self.assertEqual(len(captured.records), 2)
        self.assertEqual(captured.records[1].getMessage(), "No Null Exists")

    def test_for_correlated_col(self):
        with self.assertLogs() as captured:
            test_corr = Test_heart_disease_problem()
            test_corr.test_calculate_correlation()
        self.assertEqual(len(captured.records), 2)
        self.assertEqual(captured.records[1].getMessage(), "Correlated Columns Assigned")

    def test_for_dividing_X_and_y(self):
        with self.assertLogs() as captured:
            test_div = Test_heart_disease_problem()
            test_div.test_divide_feature_target()
        self.assertEqual(len(captured.records), 2)
        self.assertEqual(captured.records[1].getMessage(), "X features divided and Y target also")


if __name__ == '__main__':
    unittest.main()
