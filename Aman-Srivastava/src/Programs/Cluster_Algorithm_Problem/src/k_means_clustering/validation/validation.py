from sklearn.metrics import silhouette_score


def get_silhouette_score(processed_data, labels):
    """
    Function to calculate silhouette score
    @param processed_data: preprocessed data
    @param labels: label of data
    @return: score
    @return type: float
    """
    silhouette_avg = silhouette_score(processed_data, labels)
    return silhouette_avg
