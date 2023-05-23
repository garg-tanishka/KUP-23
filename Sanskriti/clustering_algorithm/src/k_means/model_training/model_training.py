from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def training_model(data_frame):
    """
    getting the model from pre-processing function and training it
    @param data_frame
    @return list
    """
    plt.scatter(data_frame['Annual Income (k$)'], data_frame['Spending Score (1-100)'])
    plt.show()

    k_means = []
    for i in range(1, 25):
        km = KMeans(n_clusters=i)
        km.fit(data_frame)
        k_means.append(km.inertia_)

    plt.plot(range(1, 25), k_means)
    plt.show()

    X = data_frame.iloc[:, :].values
    clusters = KMeans(n_clusters=5)
    y_means = clusters.fit_predict(X)
    data = [X, y_means,data_frame,clusters]
    return data
