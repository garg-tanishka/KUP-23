from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score

from Sanskriti.clustering_algorithm.src.utils.constant import figure_path


def validation(data_frame):
    """
    getting the list from training function and calculating the evaluation of k-means
    @param data_frame
    @return: silhouette avg
    """

    X = data_frame[0]
    y_means = data_frame[1]
    new_data_frame = data_frame[2]
    kmeans = data_frame[3]

    plt.scatter(X[y_means == 0, 0], X[y_means == 0, 1], color='blue')
    plt.scatter(X[y_means == 1, 0], X[y_means == 1, 1], color='red')
    plt.scatter(X[y_means == 2, 0], X[y_means == 2, 1], color='green')
    plt.scatter(X[y_means == 3, 0], X[y_means == 3, 1], color='yellow')
    plt.scatter(X[y_means == 4, 0], X[y_means == 4, 1], color='black')
    plt.savefig(figure_path/"clusters.png")
    plt.show()

    labels = kmeans.labels_
    silhouette_avg = silhouette_score(new_data_frame, labels)

    return silhouette_avg
