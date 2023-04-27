import matplotlib.pyplot as plt
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from src.utils.constant import file_path
from src.linear_regression.preprocessing.processing import pre_processing


class Linear_Regression:

    def __init__(self):
        """
        getting data from pre processing function and calculating the accuracy of the model using random forest
         @param dataframe
        @type dataframe
        """
        self.dataset = pd.read_csv(file_path, encoding='latin-1')
        self.data_frame = pd.DataFrame(self.dataset)
        self.processed = pre_processing(self.data_frame)
        self.training_model()

    def training_model(self):
        """
        getting the list from pre processing function and dividing it into 4 train and test data and finding the accuracy
         of the model
         @param : list
        @return: accuracy
        """
        X_train = self.processed[0]
        X_test = self.processed[1]
        y_train = self.processed[2]
        y_test = self.processed[3]

        forest = RandomForestRegressor()
        forest.fit(X_train, y_train)
        accuracy = forest.score(X_test, y_test)


        y_predict = forest.predict(X_test)
        plt.scatter(y_predict, y_test)

        plt.figure(figsize=(12, 8))
        plt.scatter(y_predict, y_test)
        plt.plot(range(0, 3000), range(0, 3000), c="red")
        plt.show()

        return accuracy
