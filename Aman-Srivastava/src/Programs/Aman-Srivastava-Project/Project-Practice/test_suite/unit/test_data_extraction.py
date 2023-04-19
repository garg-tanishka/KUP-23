import logging
import pandas as pd
import matplotlib.pyplot as plt


class Testing_Plot_Class:

    def __init__(self, knolder_id):
        """
        Getting Knolder's ID from main function and setting its reference
        @param knolder_id: User ID of Knolder's Employee's
        @type knolder_id: Integer
        """
        read_file = pd.read_csv("/home/knoldus/Aman/Project-Practice/DataSets/individual_contribution.csv")
        self.data_frame = pd.DataFrame(read_file)
        self.knolder_id = knolder_id
        self.test_plot_Scores()

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

    def test_plot_Scores(self):
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


