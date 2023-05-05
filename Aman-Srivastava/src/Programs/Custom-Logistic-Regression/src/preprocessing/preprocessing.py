import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class PreProcessing:
    def __init__(self, dataset):
        self.file_path = dataset

    def convert_dataframe(self):
        try:
            readfile = pd.read_csv(self.file_path)
            heart_df = pd.DataFrame(readfile)
            return self.handle_null_values(heart_df)

        except FileNotFoundError:
            return "Unable to fetch the file please check path!"

        except AttributeError:
            return "Failed to convert to dataframe"

    def handle_null_values(self, heart_df):
        columns_with_null = ["education", "cigsPerDay", "BPMeds", "totChol", "BMI", "glucose", "heartRate"]
        try:
            for i in columns_with_null:
                heart_df[i].fillna(heart_df[i].mean(), inplace=True)
            return self.calculate_correlation(heart_df)

        except:
            return "Failed to handle null values!"

    def calculate_correlation(self, heart_df):
        try:
            threshold = 0.7
            col_correlation = set()
            corr_matrix = heart_df.corr()
            for i in range(len(corr_matrix.columns)):
                for j in range(i):
                    if (corr_matrix.iloc[i, j]) > threshold:
                        column_name = corr_matrix.columns[i]
                        col_correlation.add(column_name)
            return self.drop_high_correlated(heart_df, col_correlation)

        except:
            return "error occurred in calculate correlation columns"

    def drop_high_correlated(self, heart_df, col_correlation):
        try:
            heart_df.drop(col_correlation, axis=1)
            return self.divide_feature_target(heart_df)
        except:
            return "failed to drop columns!"

    def divide_feature_target(self, heart_df):
        try:
            x_features = heart_df.drop("TenYearCHD", axis=1)
            y_target = heart_df["TenYearCHD"]
            return self.over_sample(x_features, y_target)

        except:
            return "failed to divide feature and target!"

    def over_sample(self, x_features, y_target):
        try:
            smote = SMOTE()
            x_extra_1000 = x_features.iloc[:2000]
            y_extra_1000 = y_target.iloc[:2000]
            x_features = pd.concat([x_features, x_extra_1000], ignore_index=True)
            y_target = pd.concat([y_target, y_extra_1000], ignore_index=True)
            x_sampled, y_sampled = smote.fit_resample(x_features, y_target)
            return self.train_and_test_split(x_sampled, y_sampled, x_features)

        except:
            return "failed to perform oversampling of data!"

    def train_and_test_split(self, x_sampled, y_sampled, x_features):

        try:
            x_train, x_test, y_train, y_test = train_test_split(
                x_sampled, y_sampled, train_size=0.7, test_size=0.3, random_state=100)

            x_train, x_test = self.scaling_data(x_train, x_test)

            x_train.columns = x_features.columns
            x_test.columns = x_features.columns

            y_train.index = x_train.index
            y_test.index = x_test.index

            split_data = [x_train, x_test, y_train, y_test]
            return split_data

        except:
            return "failed to split data into training and testing!"

    @staticmethod
    def scaling_data(x_train, x_test):
        try:
            scaling = StandardScaler()
            x_train = pd.DataFrame(scaling.fit_transform(x_train))
            x_test = pd.DataFrame(scaling.transform(x_test))
            scaled_data = [x_train, x_test]
            return scaled_data
        except:
            return "failed to perform scaling of data!"
