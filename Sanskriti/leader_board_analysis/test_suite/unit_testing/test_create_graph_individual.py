import matplotlib.pyplot as plt
import pandas as pd
import logging

from src.utils.constant import file_path


class testing_create_graph_individual:

    def __init__(self, knolder_id):
        dataset = pd.read_csv(file_path)
        self.data_frame = pd.DataFrame(dataset)
        self.knolder_id = knolder_id
        self.test_create_graph_individual()

    # function1 dataframe of a single knolder
    def test_extract_data_by_knolder_id(self):
        user_data = self.data_frame.loc[self.data_frame['knolder_id'] == self.knolder_id]
        return user_data

    # function2
    def test_get_score_and_name(self):
        if self.knolder_id in self.data_frame['knolder_id'].values:

            user = self.test_extract_data_by_knolder_id()

            contribution = user['contribution'].loc[user['knolder_id'] == self.knolder_id].values
            knolder_name = user['full_name'].iloc[0]
            years = user['year'].unique()

            data = [knolder_name, contribution, years]
            return data
        else:
            return 0

    def test_create_graph_individual(self):

        data = self.test_get_score_and_name()
        if data != 0:
            contribution_sum = sum(i for i in data[1])
            if contribution_sum != 0:
                plt.title(data[0])
                plt.bar(data[2], data[1])
                plt.xlabel("years")
                plt.ylabel('Contribution')
                plt.show()
                logging.info("Creating graph successful")

            else:
                logging.info("contribution check")

        else:
            logging.info("ID non-existing check")
