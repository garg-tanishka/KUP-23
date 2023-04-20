import pandas as pd

import matplotlib.pyplot as plt
from pandas import DataFrame

from src.utils.constant import file_path

class create_graph_individual:

    def __init__(self, knolder_id):
        """
        getting knolder's ID from main function and setting its reference
         @param knolder_id: user ID of knolder's employee's
        @type knolder_id: integer
        """
        dataset = pd.read_csv(file_path)
        self.data_frame = DataFrame(dataset)
        self.knolder_id = knolder_id
        self.create_graph_individual()


    def extract_data_by_knolder_id(self):
        """
        storing only particular user's dataFrame in user_data
        @return: individual data
        @rtype: dataFrame
        """
        single_individual_data = self.data_frame.loc[self.data_frame['knolder_id'] == self.knolder_id]
        return single_individual_data

    # function2
    def get_score_and_name(self):
        """
        extracting particular data of an individual
        @return:  name, contribution , years
        @rtype: list[string,integers array, integers Array]
        """
        if self.knolder_id in self.data_frame['knolder_id'].values:

            user = self.extract_data_by_knolder_id()

            contribution = user['contribution'].loc[user['knolder_id'] == self.knolder_id].values
            knolder_name = user['full_name'].iloc[0]
            years = user['year'].unique()

            user_data = [knolder_name, contribution, years]
            return user_data
        else:
            return 0

    def create_graph_individual(self):
        """
        plotting user contribution and name in Particular years using bar-plot
        """

        user_data = self.get_score_and_name()
        if user_data != 0:
            contribution_sum = sum(i for i in user_data[1])
            if contribution_sum != 0:
                plt.title(user_data[0])
                plt.bar(user_data[2], user_data[1])
                plt.xlabel("years")
                plt.ylabel('Contribution')
                plt.show()

            else:
                print("The person did no contribution")
        else:
            print("There is no knolder id with this number")