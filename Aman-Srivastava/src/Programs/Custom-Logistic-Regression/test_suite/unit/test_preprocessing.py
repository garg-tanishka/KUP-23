import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import unittest
from src.utils.constants import dataset

readfile = pd.read_csv(dataset)
dataframe = pd.DataFrame(readfile)
col_correlation = set()


class Test_Pre_Processing:

    def test_convert_dataframe(self):
        try:
            if isinstance(dataframe, pd.DataFrame):
                return "Converted to Dataframe"

        except FileNotFoundError:
            return "Unable to fetch the file please check path!"

        except AttributeError:
            return "Failed to convert to dataframe"

    def test_handle_null_values(self):

        columns_with_null = ["education", "cigsPerDay", "BPMeds", "totChol", "BMI", "glucose", "heartRate"]

        for i in columns_with_null:
            dataframe[i].fillna(dataframe[i].mean(), inplace=True)

        if dataframe.isnull().any().any():
            return 'The DataFrame contains null values'
        else:
            return "Handled Null Values"

    def test_calculate_correlation(self):
        try:
            threshold = 0.7
            corr_matrix = dataframe.corr()
            for i in range(len(corr_matrix.columns)):
                for j in range(i):
                    if (corr_matrix.iloc[i, j]) > threshold:
                        column_name = corr_matrix.columns[i]
                        col_correlation.add(column_name)
            return "Calculated High Correlated Columns"

        except:
            return "error occurred in calculate correlation columns"

    def test_drop_high_correlated(self):
        try:
            dataframe.drop(col_correlation, axis=1)
            return "Dropped High Correlated Columns"
        except:
            return "failed to drop columns!"

    def test_divide_feature_target(self):
        try:
            X_features = dataframe.drop("TenYearCHD", axis=1)
            y_target = dataframe["TenYearCHD"]
            return "Divided Feature and Target"

        except:
            return "failed to divide feature and target!"


class Test(unittest.TestCase):

    def setUp(self):
        self.calc = Test_Pre_Processing()

    def test_for_dataframe(self):
        msg = self.calc.test_convert_dataframe()
        self.assertEqual(msg, "Converted to Dataframe")

    def test_for_null_values(self):
        msg = self.calc.test_handle_null_values()
        self.assertEqual(msg, "Handled Null Values")

    def test_for_correlation(self):
        msg = self.calc.test_calculate_correlation()
        self.assertEqual(msg, "Calculated High Correlated Columns")

    def test_for_drop_columns(self):
        msg = self.calc.test_drop_high_correlated()
        self.assertEqual(msg, "Dropped High Correlated Columns")

    def test_for_divide_feature_target(self):
        msg = self.calc.test_divide_feature_target()
        self.assertEqual(msg, "Divided Feature and Target")


if __name__ == '__main__':
    unittest.main()
