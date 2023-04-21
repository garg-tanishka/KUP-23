from collections import Counter
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler


def under_balancing_data(prepared_data):
    X_train = prepared_data[0]
    X_test = prepared_data[1]
    y_train = prepared_data[2]
    under_sample = RandomUnderSampler(sampling_strategy="majority")
    X_train_sample, y_train_sample = under_sample.fit_resample(X_train, y_train)
    # counter = Counter(y_train_sample)
    return 0


def train_and_test(feature_and_target):
    features = feature_and_target[0]
    target = feature_and_target[1]
    X_train, X_test, y_train, y_test = train_test_split(
        features, target,
        test_size=0.4, random_state=42)
    prepared_data = [X_train, X_test, y_train, y_test]
    return prepared_data


def divide_feature_target(data_frame):
    """
    Dividing features and target from dataframe
    @param data_frame: heart_dataframe
    @return: list[training_features, target]
    @rtype: list
    """
    X_independent = data_frame.drop("TenYearCHD", axis=1)
    y_target = data_frame["TenYearCHD"]
    divided_data = [X_independent, y_target]
    return divided_data


def drop_high_correlated(data_frame, high_corr_column):
    """
    Dropping Highly Correlated Columns to resolve
    Multi-Collinearity.
    @param data_frame: heart_dataframe
    @param high_corr_column: columns that are highly correlated
    @return: heart_dataframe after dropping columns
    @rtype: dataframe
    """
    data_frame.drop(high_corr_column, axis=1)
    drop_data = data_frame.drop("education", axis=1, )
    return drop_data


def correlation(data_frame):
    """
    Function to find to correlation between feature
    having more than 0.6 threshold.
    @param data_frame: heart_dataframe
    @return: set(columns that have high correlation)
    @rtype: set
    """
    threshold = 0.6
    col_correlation = set()
    corr_matrix = data_frame.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i, j]) > threshold:
                column_name = corr_matrix.columns[i]
                col_correlation.add(column_name)
    return col_correlation


def fill_null_values(data_frame):
    """
    Filling columns having null values with its means values
    with its mean values.
    @param data_frame: heart_dataframe
    @return: heart_dataframe after filling null values
    @rtype: dataframe
    """
    columns_with_null = ["education", "cigsPerDay", "BPMeds", "totChol", "BMI", "glucose"]
    for i in columns_with_null:
        data_frame[i].fillna(data_frame[i].mean(), inplace=True)
    return data_frame


def pre_processing(data_frame):
    """
    Doing all the pre-processing of data:
    Cleaning,Filling,Feature_Selection etc.
    @param data_frame: heart_data
    @return: heart_data after pre-processing
    @rtype: dataframe
    """
    heart_data = pd.DataFrame(data_frame)
    handled_null = fill_null_values(heart_data)
    corr_column = correlation(handled_null)
    dropped_df = drop_high_correlated(handled_null, corr_column)
    feature_and_target = divide_feature_target(dropped_df)
    prepared_data = train_and_test(feature_and_target)
    under_sampled_data = under_balancing_data(prepared_data)
    return under_sampled_data
