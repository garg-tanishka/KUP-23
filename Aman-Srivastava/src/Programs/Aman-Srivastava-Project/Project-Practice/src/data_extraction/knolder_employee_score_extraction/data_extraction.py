import logging
import pandas as pd
import matplotlib.pyplot as plt
from src.utils.constants import dataset_path


class Plot_Class:

    def __init__(self, knolder_id):
        """
        Getting Knolder's ID from main function and setting its reference
        @param knolder_id: User ID of Knolder's Employee's
        @type knolder_id: Integer
        """
        # not hard coding
        read_file = pd.read_csv(dataset_path)
        self.data_frame = pd.DataFrame(read_file)
        self.knolder_id = knolder_id
        self.plot_scores()

    def return_single_user_data(self):
        """
        Storing Only Particular User's DataFrame in single_user_df
        @return: Single User Data
        @rtype: DataFrame
        """
        single_user_df = self.data_frame.loc[self.data_frame["knolder_id"] == self.knolder_id]
        return single_user_df

    def extract_scores(self):
        """
        Extracting particular data of an individual
        @return: Contribution Name, Scores, Years
        @rtype: List[String,Integers Array, Integers Array]
        """
        if self.knolder_id in self.data_frame["knolder_id"].values:
            data_frame = self.return_single_user_data()

            user_score = data_frame["total_score"].loc[data_frame["knolder_id"] == self.knolder_id].values

            years = data_frame["year"].loc[data_frame["knolder_id"] == self.knolder_id].values

            user_name = data_frame['full_name'].iloc[0]
            user_data = [user_name, user_score, years]
            return user_data

        else:
            return 0

    def plot_scores(self):
        """
        Plotting Users Scores, Name in Particular Years using Bar-Plot
        """
        user_data = self.extract_scores()
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
                print("This Person Has No Contribution")

        else:
            # also use try and catch block
            logging.info("Non Existing Check")
            print("There is No User of this ID:", self.knolder_id)


