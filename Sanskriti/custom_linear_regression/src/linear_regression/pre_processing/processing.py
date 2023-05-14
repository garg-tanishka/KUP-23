
from sklearn.model_selection import train_test_split


def pre_processing(data_frame):
    """
    getting the dataframe and pre-processing it and splitting it into training and testing data
    :param dataframe
    :return list[X_train,X_test,y_train,y_test]
    @param data_frame:
    """

    X = data_frame.iloc[:, 0].values
    y = data_frame.iloc[:, 1].values
    print(y.shape)
    print(X.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=3)

    splitted_data = [X_train, X_test, y_train, y_test]
    return splitted_data
