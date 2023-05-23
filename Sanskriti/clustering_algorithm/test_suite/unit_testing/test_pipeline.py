import logging
import unittest

import pandas as pd

from Sanskriti.clustering_algorithm.src.k_means.pre_processing.pre_processing import drop_columns
from Sanskriti.clustering_algorithm.src.utils.constant import file_path


class Testing_K_Means:
    def __init__(self):
        """
        getting data from preprocessing function and calculating the accuracy of k-means
         @param dataframe
        @type dataframe
        """
        self.dataset = file_path

    def test_pre_processing(self):
        """
            getting the dataframe and pre processing it
            @param data_frame
            @return dataframe
        """
        read_file = pd.read_csv(file_path)
        read_data_frame = pd.DataFrame(read_file)
        processed_data = drop_columns(read_data_frame)

        if isinstance(read_data_frame, pd.DataFrame):
            logging.info("This is a Dataframe")
        else:
            logging.info("This is not Dataframe")
        return processed_data

    def test_drop_columns(self):
        """
        getting the dataframe and dropping the un_necessary column
        @param data_frame
        @return data_frame
        """
        read_file = pd.read_csv(file_path)
        data_frame = pd.DataFrame(read_file)
        dropping_columns = ['Gender', 'CustomerID']
        new_data_frame = data_frame.drop(dropping_columns, axis=1)
        if len(new_data_frame) == 200:
            logging.info("The Dataframe is in right length")
        else:
            logging.info("The Dataframe is in wrong length")
        return new_data_frame


class Test_class(unittest.TestCase):
    def test_for_dataframe(self):
        with self.assertLogs() as captured:
            df_check = Testing_K_Means()
            df_check.test_pre_processing()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "This is a Dataframe")

    def test_for_length_of_dataframe(self):
        with self.assertLogs() as captured:
            divide_check = Testing_K_Means()
            divide_check.test_drop_columns()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "The Dataframe is in right length")
