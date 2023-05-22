from src.k_means_clustering.model_training.k_means_clustering import K_Means
from src.k_means_clustering.preprocessing.preprocessing import PreProcessing


class CustomerSegmentation:

    def __init__(self, user_input):
        self.query = user_input

    @staticmethod
    def get_trained_model():
        """
        Function to get the data after preprocessing,
        then applying the k_mean model on that data.
        @return: Dictionary{Clusters List}
        """
        try:
            preprocessing = PreProcessing()
            processed_data = preprocessing.pre_processing()

            k_mean_model = K_Means(processed_data)
            km_clusters, silhouette_score = k_mean_model.get_k_means_model()

            return km_clusters.to_dict(), f"Silhouette Score {silhouette_score}"

        except Exception as e:
            return str(e)
