import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import int64, float64
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from src.linear_regression.pipeline.constant import file_path
import unittest
import logging

from src.linear_regression.preprocessing.processing import type_conversion, one_hot_encoding, drop_columns, \
    feature_selection, pre_processing, turn_memory_into_MB


class Test_Linear_Regression:

    def __init__(self):
        """
        getting data from pre processing function and calculating the accuracy of the model using random forest
         @param dataframe
        @type dataframe
        """
        self.dataset = pd.read_csv(file_path, encoding='latin-1')
        self.data_frame = pd.DataFrame(self.dataset)
        self.processed = pre_processing(self.data_frame)

    def test_drop_columns(self):
        """"
            getting the dataframe from pre_processing function and dropping the non required columns
            @param : dataframe
            @return : dataframe

            """
        dropping_columns = ["Product", 'Company', 'TypeName', 'ScreenResolution', "Memory_type", 'Cpu', 'Memory', "Gpu",
                            "OpSys", "Cpu_Brand", "Gpu_brand"]

        self.data_frame = self.data_frame.drop(dropping_columns, axis=1)
        column_length_dataframe = self.data_frame.columns
        length_dataframe = len(column_length_dataframe)

        if length_dataframe == 9:
            logging.info("Dataframe is in right length")
        else:
            logging.info("Dataframe is in wrong length")

        return self.data_frame

    def test_type_conversion(self):
        """
            getting dataframe from the pre_processing function and converting the type of the column
            @param : dataframe
            @:return : dataframe

            """
        # screen resolution column
        self.data_frame["ScreenResolution"] = self.data_frame.ScreenResolution.str.split(" ").apply(lambda x: x[-1])
        self.data_frame["Screen_width"] = self.data_frame.ScreenResolution.str.split("x").apply(lambda x: x[0])
        self.data_frame['Screen_height'] = self.data_frame.ScreenResolution.str.split("x").apply(lambda x: x[1])
        self.data_frame["Screen_width"] = self.data_frame["Screen_width"].astype("int")
        self.data_frame["Screen_height"] = self.data_frame["Screen_height"].astype("int")

        # cpu column
        self.data_frame['Cpu_Brand'] = self.data_frame.Cpu.str.split(" ").apply(lambda x: x[0])
        self.data_frame['Cpu_frequency'] = self.data_frame.Cpu.str.split(" ").apply(lambda x: x[-1])
        self.data_frame["Cpu_frequency"] = self.data_frame["Cpu_frequency"].str[:-3]
        self.data_frame["Cpu_frequency"] = self.data_frame["Cpu_frequency"].astype("float")

        # ram column
        # self.data_frame["Ram"] = self.data_frame["Ram"].str[:-2]
        # self.data_frame["Ram"] = self.data_frame["Ram"].astype("int")

        # memory column
        self.data_frame["Memory_amount"] = self.data_frame.Memory.str.split(" ").apply(lambda x: x[0])
        self.data_frame["Memory_type"] = self.data_frame.Memory.str.split(" ").apply(lambda x: x[1])
        self.data_frame["Memory_amount"] = self.data_frame["Memory_amount"].apply(turn_memory_into_MB)

        # weight column
        # self.data_frame["Weight"] = self.data_frame["Weight"].str[:-2]
        # self.data_frame["Weight"] = self.data_frame["Weight"].astype("float")

        # gpu column
        self.data_frame["Gpu_brand"] = self.data_frame["Gpu"].str.split(" ").apply(lambda x: x[0])

        screen_width_type = self.data_frame.Screen_width.dtypes
        screen_height_type = self.data_frame.Screen_height.dtypes
        Cpu_frequency_type = self.data_frame.Cpu_frequency.dtypes
        Memory_amount_type = self.data_frame.Memory_amount.dtypes

        if screen_width_type == int64 and screen_height_type == int64 and Cpu_frequency_type == float64 and Memory_amount_type == float64:
            logging.info("Type is correct")
        else:
            logging.info("Type is Wrong")

        return self.data_frame


class Test_class(unittest.TestCase):

    def test_type_conversion(self):
        with self.assertLogs() as captured:
            call_fun = Test_Linear_Regression()
            call_fun.test_type_conversion()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Type is correct")

    def test_drop_columns(self):
        with self.assertLogs() as captured:
            call_fun = Test_Linear_Regression()
            call_fun.test_drop_columns()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Dataframe is in right length")


if __name__ == "__main__":
    unittest.main()
