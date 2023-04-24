import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from src.linear_regression.pipeline.constant import file_path


def correlation(data_frame):
    """
    getting the dataframe from feature selection function and calculating the correlation of every feature with respect to the target
    feature price euros.
    @param : dataframe
    @return: list
    """
    target_correlation = data_frame.corr()["Price_euros"].apply(abs).sort_values()
    return target_correlation


def feature_selection(data_frame):
    """
    getting the dataframe from pre processing function and selecting 21 features from last.
    @param : data_frame
    @return: list
    """
    dataframe_correlation = correlation(data_frame)
    selected_features = dataframe_correlation[-21:].index
    print(selected_features)
    return selected_features


def drop_columns(data_frame):
    """"
        getting the dataframe from pre_processing function and dropping the non required columns
        @param : dataframe
        @return : dataframe

        """
    dropping_columns = ["Product", 'Company', 'TypeName', 'ScreenResolution', "Memory_type", 'Cpu', 'Memory', "Gpu",
                        "OpSys",
                        "Cpu_Brand", "Gpu_brand"]

    data_frame = data_frame.drop(dropping_columns, axis=1)
    return data_frame


def one_hot_encoding(data_frame):
    """
        getting the dataframe from pre_processing function and applying one hot encoding
        @param : dataframe
        @return: dataframe
        """
    data_frame = data_frame.join(pd.get_dummies(data_frame.Company))
    data_frame = data_frame.join(pd.get_dummies(data_frame.TypeName))
    data_frame = data_frame.join(pd.get_dummies(data_frame.OpSys))

    cpu_categories = pd.get_dummies(data_frame.Cpu_Brand)
    cpu_categories.columns = [col + "Cpu" for col in cpu_categories.columns]
    data_frame = data_frame.join(cpu_categories)

    gpu_categories = pd.get_dummies(data_frame.Gpu_brand)
    gpu_categories.columns = [col + "Gpu" for col in gpu_categories.columns]
    data_frame = data_frame.join(gpu_categories)

    return data_frame


def turn_memory_into_MB(value):
    if "GB" in value:
        return float(value[:value.find("GB")]) * 1000
    elif "TB" in value:
        return float(value[:value.find("TB")]) * 1000000


def type_conversion(data_frame):
    """
        getting dataframe from the pre_processing function and converting the type of the column
        @param : dataframe
        @:return : dataframe

        """
    # screen resolution column
    data_frame["ScreenResolution"] = data_frame.ScreenResolution.str.split(" ").apply(lambda x: x[-1])
    data_frame["Screen_width"] = data_frame.ScreenResolution.str.split("x").apply(lambda x: x[0])
    data_frame['Screen_height'] = data_frame.ScreenResolution.str.split("x").apply(lambda x: x[1])

    # cpu column
    data_frame['Cpu_Brand'] = data_frame.Cpu.str.split(" ").apply(lambda x: x[0])
    data_frame['Cpu_frequency'] = data_frame.Cpu.str.split(" ").apply(lambda x: x[-1])
    data_frame["Cpu_frequency"] = data_frame["Cpu_frequency"].str[:-3]

    # ram column
    data_frame["Ram"] = data_frame["Ram"].str[:-2]
    data_frame["Ram"] = data_frame["Ram"].astype("int")

    # memory column
    data_frame["Memory_amount"] = data_frame.Memory.str.split(" ").apply(lambda x: x[0])
    data_frame["Memory_type"] = data_frame.Memory.str.split(" ").apply(lambda x: x[1])
    data_frame["Memory_amount"] = data_frame["Memory_amount"].apply(turn_memory_into_MB)

    # weight column
    data_frame["Weight"] = data_frame["Weight"].str[:-2]
    data_frame["Weight"] = data_frame["Weight"].astype("float")

    # gpu column
    data_frame["Gpu_brand"] = data_frame["Gpu"].str.split(" ").apply(lambda x: x[0])

    return data_frame


def pre_processing(dataset):
    data_frame_new = type_conversion(dataset)
    data_frame_encoded = one_hot_encoding(data_frame_new)
    data_frame_dropped = drop_columns(data_frame_encoded)

    feature = feature_selection(data_frame_dropped)
    limited_df = data_frame_dropped[feature]
    plt.figure(figsize=(18, 15))
    sns.heatmap(limited_df.corr(), annot=True, cmap=plt.cm.Blues_r)
    plt.show()
    X, y = limited_df.drop("Price_euros", axis=1), limited_df["Price_euros"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)
    scaler = StandardScaler()
    X_train_scale = scaler.fit_transform(X_train)
    X_test_scale = scaler.transform(X_test)
    x = []
    x = X
    X_train_scale.columns = x.columns
        

