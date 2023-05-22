from sklearn.cluster import KMeans
from src.k_means_clustering.validation.validation import get_silhouette_score
from src.utils.helpers.visualize_data import visualize_data


class K_Means:

    def __init__(self, processed_data):
        self.processed_data = processed_data

    def get_k_means_model(self):
        processed_data = self.processed_data
        km_clusters = KMeans(n_clusters=6, init='k-means++').fit(processed_data)

        labels = km_clusters.labels_

        km_clustered = processed_data.copy()
        km_clustered.loc[:, 'Cluster'] = km_clusters.labels_

        km_clust_sizes = km_clustered.groupby('Cluster').size().to_frame()
        km_clust_sizes.columns = ["KM_size"]

        visualize_data(processed_data, labels)

        score = get_silhouette_score(processed_data, labels)
        silhouette_score = str(round(score, 2))
        return km_clust_sizes, silhouette_score
