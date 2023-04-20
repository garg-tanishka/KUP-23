import logging
import pandas as pd
import matplotlib.pyplot as plt
import unittest
from src.utils.constants import dataset_path


class Testing_Plot_Class:

    def __init__(self, knolder_id):
        """
        Getting Knolder's ID from main function and setting its reference
        @param knolder_id: User ID of Knolder's Employee's
        @type knolder_id: Integer
        """
        read_file = pd.read_csv(dataset_path)
        self.data_frame = pd.DataFrame(read_file)
        self.knolder_id = knolder_id
        self.test_plot_scores()

    def test_return_single_user_data(self):
        """
        Storing Only Particular User's DataFrame in single_user_df
        @return: Single User Data
        @rtype: DataFrame
        """
        single_user_df = self.data_frame.loc[self.data_frame["knolder_id"] == self.knolder_id]
        return single_user_df

    def test_extract_scores(self):
        """
        Extracting particular data of an individual
        @return: Contribution Name, Scores, Years
        @rtype: List[String,Integers Array, Integers Array]
        """
        if self.knolder_id in self.data_frame["knolder_id"].values:
            data_frame = self.test_return_single_user_data()

            user_score = data_frame["total_score"].loc[data_frame["knolder_id"] == self.knolder_id].values
            years = data_frame["year"].loc[data_frame["knolder_id"] == self.knolder_id].values
            user_name = data_frame['full_name'].iloc[0]

            user_data = [user_name, user_score, years]
            return user_data

        else:
            return 0

    def test_plot_scores(self):
        """
        Plotting Users Scores, Name in Particular Years using Bar-Plot
        """
        user_data = self.test_extract_scores()
        if user_data != 0:
            check_sum = sum(i for i in user_data[1])
            if check_sum != 0:
                plt.title(user_data[0])
                plt.bar(user_data[2], user_data[1])
                plt.ylabel("Score Count")
                plt.xlabel('All Present Years')
                plt.show()
                logging.info("Plot Successful")
            else:
                logging.info("Zero Contribution Check")

        else:
            logging.info("Non Existing Check")


class Test_Class(unittest.TestCase):

    def test_for_int(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(25)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Plot Successful")

    def test_for_zero_contribution(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(484)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Zero Contribution Check")

    def test_for_double(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(45.3365859965333)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")

    def test_for_float(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(2.7)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")

    def test_for_string(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class("UserName")
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")

    def test_for_negative(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(-8)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")

    def test_for_symbols(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class("%$=-=")
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")


if __name__ == '__main__':
    unittest.main()
