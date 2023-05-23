import pandas as pd
from sklearn.preprocessing import StandardScaler


def pre_processing(data_frame):
    """
        getting the dataframe and pre processing it
        @param data_frame
        @return dataframe
    """
    read_file = pd.read_csv(data_frame)
    data_frame = pd.DataFrame(read_file)
    processed_data = drop_columns(data_frame)
    scaled_data = scaling(processed_data)
    return scaled_data


def drop_columns(data_frame):
    """
    getting the dataframe and dropping the un_necessary column
    @param data_frame
    @return data_frame
    """
    dropping_columns = ['Gender', 'CustomerID','Age']
    data_frame = data_frame.drop(dropping_columns, axis=1)

    return data_frame


def scaling(data_frame):
    """
    getting the dataframe and normalizing it
    @param data_frame
    @return data_frame
    """
    scale = StandardScaler()
    scaled_data = pd.DataFrame(scale.fit_transform(data_frame))
    scaled_data.columns = data_frame.columns

    return scaled_data
