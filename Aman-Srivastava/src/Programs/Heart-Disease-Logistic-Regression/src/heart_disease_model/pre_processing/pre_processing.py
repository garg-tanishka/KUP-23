import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE


def scaling_data(X_train, X_test):
    """
    Performing Standardization on both training and
    testing data by scaling them to unit variance
    @param X_train: Training dataset
    @param X_test: Testing dataset
    @return: dataframes[X_train, X_test, y_train, y_test]
    @rtype: list
    """
    scaling = StandardScaler()
    X_train = pd.DataFrame(scaling.fit_transform(X_train))
    X_test = pd.DataFrame(scaling.transform(X_test))
    scaled_data = [X_train, X_test]
    return scaled_data


def train_and_test_split(X_sampled, y_sampled, X):
    """
    Function to perform splitting data into training and testing set,
    calling function("scaling_data()") to perform Standard_Scaling datasets,
    assigning back the name of columns to scaled datasets (X_train, X_test),
    @param X_sampled: Features
    @param y_sampled: Target
    @param X:
    @return: dataframes[X_train, X_test, y_train, y_test]
    @rtype: list
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X_sampled, y_sampled, train_size=0.7, test_size=0.3, random_state=100)

    X_train, X_test = scaling_data(X_train, X_test)

    X_train.columns = X.columns
    X_test.columns = X.columns

    y_train.index = X_train.index
    y_test.index = X_test.index

    split_data = [X_train, X_test, y_train, y_test]
    return split_data


def over_sample(X_features, y_target):
    """
    Performing over_sampling to balance the ratio of data on both
    majority and minority classes, and also calling: function(train_and_test_split()),
    @param X_features: Training Features
    @param y_target: Target Feature
    @return: dataframes[X_train, X_test, y_train, y_test]
    @rtype: list
    """
    smote = SMOTE()

    X_extra_1000 = X_features.iloc[:2000]
    y_extra_1000 = y_target.iloc[:2000]

    X_features = pd.concat([X_features, X_extra_1000], ignore_index=True)
    y_target = pd.concat([y_target, y_extra_1000], ignore_index=True)

    X_os, y_os = smote.fit_resample(X_features, y_target)

    # y_os.value_counts().plot(kind='bar')
    # plt.show()

    partitioned_data = train_and_test_split(X_os, y_os, X_features)
    return partitioned_data


def divide_feature_target(data_frame):
    """
    Dividing features and target from dataframe,
    calling method to perform under-sampling of data
    @param data_frame: heart_dataframe
    @return: dataframes[X_train_scaled, X_test_scaled, y_train, y_test]
    @rtype: list
    """
    X_features = data_frame.drop("TenYearCHD", axis=1)
    y_target = data_frame["TenYearCHD"]
    data_frames = over_sample(X_features, y_target)
    return data_frames


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
    data_frames = divide_feature_target(data_frame)
    return data_frames


def calculate_correlation(data_frame):
    """
    Function to find to correlation between feature
    having more than 0.6 threshold.
    @param data_frame: heart_dataframe
    @return: dataframes[X_train_scaled, X_test_scaled, y_train, y_test]
    @rtype: list
    """
    threshold = 0.7
    col_correlation = set()
    corr_matrix = data_frame.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i, j]) > threshold:
                column_name = corr_matrix.columns[i]
                col_correlation.add(column_name)
    data_frames = drop_high_correlated(data_frame, col_correlation)
    return data_frames


def fill_null_values(data_frame):
    """
    Filling columns having null values with its means values.
    @param data_frame: heart_dataframe
    @return: dataframes[X_train_scaled, X_test_scaled, y_train, y_test]
    @rtype: list
    """
    columns_with_null = ["education", "cigsPerDay", "BPMeds", "totChol", "BMI", "glucose", "heartRate"]
    for i in columns_with_null:
        data_frame[i].fillna(data_frame[i].mean(), inplace=True)

    data_frame = calculate_correlation(data_frame)
    return data_frame


def pre_processing(dataset_path):
    """
    Doing all the pre-processing of data:
    Cleaning,Filling,Feature_Selection etc.
    @param dataset_path: heart_data
    @return: heart_data after pre-processing
    @rtype: dataframe
    """
    readfile = pd.read_csv(dataset_path)
    heart_data = pd.DataFrame(readfile)
    processed_df = fill_null_values(heart_data)
    return processed_df
