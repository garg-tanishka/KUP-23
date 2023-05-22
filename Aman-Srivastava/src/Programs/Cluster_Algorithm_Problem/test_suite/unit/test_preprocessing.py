import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.utils.constants import dataset_path
import unittest
from pandas.util.testing import assert_frame_equal


class PreProcessing:

    def __init__(self):
        self.customer_dataset = dataset_path

    def test_pre_processing(self):
        """
        Function to do all preprocessing by calling functions
        @return: processed data (dataframe)
        """
        customer_dataframe = self.test_get_dataframe(self.customer_dataset)
        customer_dataframe = self.test_get_rename_column(customer_dataframe)
        customer_dataframe_subset = self.test_get_subset(customer_dataframe)
        return customer_dataframe_subset

    @staticmethod
    def test_get_dataframe(customer_dataset):
        """
        Function to convert dataset to dataframe
        @param customer_dataset:
        @return: dataframe
        """
        readfile = pd.read_csv(customer_dataset)
        customer_dataframe = pd.DataFrame(readfile)
        return customer_dataframe

    @staticmethod
    def test_get_rename_column(customer_dataframe):
        """
        Function to rename columns
        @param customer_dataframe:
        @return: renamed dataframe
        """
        customer_dataframe.rename(columns={'Annual Income (k$)': 'annual_income'}, inplace=True)
        customer_dataframe.rename(columns={'Spending Score (1-100)': 'spending_score_1_to_100'}, inplace=True)
        expected_col_name = customer_dataframe.columns.tolist()

        return expected_col_name

    @staticmethod
    def test_get_subset(customer_dataframe):
        """
        Function to create subset of dataframe
        @param customer_dataframe:
        @return: dataframe subset
        """
        customer_dataframe_subset = customer_dataframe[
            ['annual_income', 'spending_score_1_to_100']]

        return "Created Subset Successfully"

    @staticmethod
    def test_get_scaled_data(customer_dataframe):
        """
        Function to standardize the values of dataframe
        @param customer_dataframe: dataframe
        @return: standardized dataframe
        """
        scale = StandardScaler()
        scaled_data = pd.DataFrame(scale.fit_transform(customer_dataframe))
        scaled_data.columns = customer_dataframe.columns
        return "Scaled Data Successfully"


class TestClass(unittest.TestCase):

    def test_for_dataframe(self):
        readfile = pd.read_csv(dataset_path)
        customer_dataframe = pd.DataFrame(readfile)

        check_df = PreProcessing()
        result = check_df.test_get_dataframe(dataset_path)
        assert_frame_equal(result, customer_dataframe)

    def test_col_rename(self):
        readfile = pd.read_csv(dataset_path)
        customer_dataframe = pd.DataFrame(readfile)

        check_name_df = pd.DataFrame(readfile)
        check_name_df.rename(columns={'Annual Income (k$)': 'annual_income'}, inplace=True)
        check_name_df.rename(columns={'Spending Score (1-100)': 'spending_score_1_to_100'}, inplace=True)
        expected_col_name = check_name_df.columns.tolist()

        check_col = PreProcessing()
        result = check_col.test_get_rename_column(customer_dataframe)
        self.assertEquals(result, expected_col_name)

    def test_subset(self):
        readfile = pd.read_csv(dataset_path)
        check_df = pd.DataFrame(readfile)
        check_df.rename(columns={'Annual Income (k$)': 'annual_income'}, inplace=True)
        check_df.rename(columns={'Spending Score (1-100)': 'spending_score_1_to_100'}, inplace=True)

        check_subset = PreProcessing()
        result = check_subset.test_get_subset(check_df)

        self.assertEqual(result, "Created Subset Successfully")

    def test_scaled_data(self):
        readfile = pd.read_csv(dataset_path)
        check_df = pd.DataFrame(readfile)
        check_df.rename(columns={'Annual Income (k$)': 'annual_income'}, inplace=True)
        check_df.rename(columns={'Spending Score (1-100)': 'spending_score_1_to_100'}, inplace=True)
        customer_dataframe_subset = check_df[
            ['annual_income', 'spending_score_1_to_100']]

        check_subset = PreProcessing()
        result = check_subset.test_get_scaled_data(customer_dataframe_subset)

        self.assertEqual(result, "Scaled Data Successfully")


if __name__ == '__main__':
    unittest.main()
