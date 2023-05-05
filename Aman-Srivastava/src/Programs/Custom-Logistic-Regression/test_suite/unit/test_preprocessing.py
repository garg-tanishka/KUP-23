import logging
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import unittest
from src.utils.constants import dataset


class TestPreprocessing:

    def test_convert_dataframe(self):
        file_path = dataset
        readfile = pd.read_csv(file_path)
        heart_df = pd.DataFrame(readfile)
        try:
            if isinstance(heart_df, pd.DataFrame):
                pass

            return heart_df

        except FileNotFoundError:
            return "Unable to fetch the file please check path!"

        except AttributeError:
            return "Failed to convert to dataframe"

    def test_handle_null_values(self):

        readfile = pd.read_csv(dataset)
        self.heart_df = pd.DataFrame(readfile)

        columns_with_null = ["education", "cigsPerDay", "BPMeds", "totChol", "BMI", "glucose", "heartRate"]
        try:
            for i in columns_with_null:
                self.heart_df[i].fillna(self.heart_df[i].mean(), inplace=True)

            return self.heart_df
        except:
            return "Failed to handle null values!"

    def test_calculate_correlation(self):
        readfile = pd.read_csv(dataset)
        heart_df = pd.DataFrame(readfile)

        try:
            threshold = 0.7
            col_correlation = set()
            corr_matrix = heart_df.corr()
            for i in range(len(corr_matrix.columns)):
                for j in range(i):
                    if (corr_matrix.iloc[i, j]) > threshold:
                        column_name = corr_matrix.columns[i]
                        col_correlation.add(column_name)
            return col_correlation

        except:
            return "error occurred in calculate correlation columns"

    def test_drop_high_correlated(self):
        corr_col = ["cigsPerDay", "diaBP"]
        try:
            self.heart_df.drop(corr_col, axis=1)
            return self.heart_df
        except:
            return "failed to drop columns!"


class Test(unittest.TestCase):

    def setUp(self):
        self.file_path = dataset
        readfile = pd.read_csv(self.file_path)
        self.heart_df = pd.DataFrame(readfile)
        self.corr_col = None
        self.dropped_data = None

    def test_df_convert(self):
        my_class = TestPreprocessing()
        result = my_class.test_convert_dataframe()
        pd.testing.assert_frame_equal(result, self.heart_df)

    def test_for_null(self):
        my_class = TestPreprocessing()
        result = my_class.test_handle_null_values()
        self.assertFalse(result.isnull().values.any())

    def test_for_high_corr_col(self):
        my_class = TestPreprocessing()
        result = my_class.test_calculate_correlation()
        self.corr_col = result
        self.assertEqual(result, {'cigsPerDay', 'diaBP'})

    def test_for_drop(self):
        corr_col = ["cigsPerDay", "diaBP"]
        self.dropped_data = pd.DataFrame(self.heart_df.drop(corr_col, axis=1))
        my_class = TestPreprocessing()
        my_class.test_drop_high_correlated()

        self.assertNotIn('cigsPerDay', self.dropped_data.columns)
        self.assertNotIn('diaBP', self.dropped_data.columns)


if __name__ == '__main__':
    unittest.main()
