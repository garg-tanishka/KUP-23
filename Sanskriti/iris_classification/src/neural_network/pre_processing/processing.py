import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.model_selection import train_test_split


def pre_processing(data_frame):
    """
    getting the dataframe and pre processing it
    @param data_frame
    @return dataframe
    """
    print("abc")
    read_file = pd.read_csv(data_frame)
    data_frame = pd.DataFrame(read_file)

    processed_data = target_feature(data_frame)
    return processed_data


def target_feature(iris_dataframe):
    """
    getting the dataframe and dividing it into training and testing data
    @param iris_dataframe
    @return: dataframe
    """
    X_feature = iris_dataframe.drop("Species", axis=1)
    target = iris_dataframe["Species"]
    target = encoding(target)
    pre_processed_data = splitting_dataset(X_feature, target)
    return pre_processed_data


def encoding(target):
    """
    getting the target dataframe and applying encoding to transform into categorical form
    @param target 
    @return: dataframe
    """
    change_label = LabelEncoder()
    target = pd.DataFrame(change_label.fit_transform(target))
    target = np_utils.to_categorical(target)
    return target


def splitting_dataset(X_feature, target):
    """
    getting dataframe and splitting them into training and test data 
    @param X_feature , target
    @return : list[X_train, X_test, y_train, y_test] 
    """
    X_train, X_test, y_train, y_test = train_test_split(X_feature, target, test_size=0.20, random_state=50)
    splitted_data = [X_train, X_test, y_train, y_test]
    return splitted_data


if __name__ == "__main__":
    path = '/home/knoldus/PycharmProjects/KUP-23/Sanskriti/iris_classification/src/dataset/iiris.csv'
    run = pre_processing(path)
    print(run)
