import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.utils import np_utils


def pre_processing(dataset):
    """
    Function to read csv file and convert that into dataframe,
    @param dataset: iris_csv_file
    @return: dataframe[X_train, X_test, y_train, y_test]
    @rtype: list
    """
    read_file = pd.read_csv(dataset)
    iris_dataframe = pd.DataFrame(read_file)
    pre_processed_data = divide_feature_target(iris_dataframe)
    return pre_processed_data


def divide_feature_target(iris_dataframe):
    """
    Function to divide features and target and also split them,
    @param iris_dataframe: iris_dataframe
    @return: dataframe[X_features, X_test, y_train, y_test]
    @rtype: list
    """
    X_feature = iris_dataframe.drop(["Species", "Id"], axis=1)
    y_target = iris_dataframe["Species"]
    y_target = categorical_conversion(y_target)
    pre_processed_data = split_data(X_feature, y_target)
    return pre_processed_data


def categorical_conversion(y_target):
    """
     Function to convert categorical data into numeric data,
     @param y_target: target values
     @return: y_target[numeric series of categories]
     @rtype: dataframe
     """
    change_label = LabelEncoder()
    y_target = pd.DataFrame(change_label.fit_transform(y_target))
    y_target = np_utils.to_categorical(y_target)
    return y_target


def split_data(X_feature, y_target):
    """
    Function to perform split operations on feature and target
    @param X_feature: features
    @param y_target: target value
    @return: dataframe[X_features, X_test, y_train, y_test]
    @rtype: dataframe
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X_feature, y_target, test_size=0.2, random_state=42)
    divided_data = [X_train, X_test, y_train, y_test]
    return divided_data
