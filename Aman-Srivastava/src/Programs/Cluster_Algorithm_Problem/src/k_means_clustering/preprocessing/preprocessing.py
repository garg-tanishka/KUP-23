import pandas as pd
from src.utils.constants import dataset_path
from sklearn.preprocessing import StandardScaler


class PreProcessing:

    def __init__(self):
        self.customer_dataset = dataset_path

    def pre_processing(self):
        """
        Function to do all preprocessing by calling functions
        @return: processed data (dataframe)
        """
        customer_dataframe = self.get_dataframe(self.customer_dataset)
        customer_dataframe = self.get_rename_column(customer_dataframe)
        customer_dataframe_subset = self.get_subset(customer_dataframe)
        scaled_data = self.get_scaled_data(customer_dataframe_subset)
        return scaled_data

    @staticmethod
    def get_dataframe(customer_dataset):
        """
        Function to convert dataset to dataframe
        @param customer_dataset:
        @return: dataframe
        """
        readfile = pd.read_csv(customer_dataset)
        customer_dataframe = pd.DataFrame(readfile)
        return customer_dataframe

    @staticmethod
    def get_rename_column(customer_dataframe):
        """
         Function to rename columns
         @param customer_dataframe:
         @return: renamed dataframe
         """
        customer_dataframe.rename(columns={'Annual Income (k$)': 'annual_income'}, inplace=True)
        customer_dataframe.rename(columns={'Spending Score (1-100)': 'spending_score_1_to_100'}, inplace=True)
        return customer_dataframe

    @staticmethod
    def get_subset(customer_dataframe):
        """
        Function to create subset of dataframe
        @param customer_dataframe:
        @return: dataframe subset
        """
        customer_dataframe_subset = customer_dataframe[
            ['annual_income', 'spending_score_1_to_100']]
        return customer_dataframe_subset

    @staticmethod
    def get_scaled_data(customer_dataframe):
        """
        Function to standardize the values of dataframe
        @param customer_dataframe: dataframe
        @return: standardized dataframe
        """
        scale = StandardScaler()
        scaled_data = pd.DataFrame(scale.fit_transform(customer_dataframe))
        scaled_data.columns = customer_dataframe.columns
        return scaled_data
