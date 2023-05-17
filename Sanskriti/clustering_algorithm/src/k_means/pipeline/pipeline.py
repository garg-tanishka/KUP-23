from Sanskriti.clustering_algorithm.src.k_means.model_training.model_training import training_model
from Sanskriti.clustering_algorithm.src.k_means.model_validation.model_validation import validation
from Sanskriti.clustering_algorithm.src.k_means.pre_processing.pre_processing import pre_processing
from Sanskriti.clustering_algorithm.src.utils.constant import file_path


class K_Means:
    def __init__(self):
        """
        getting data from preprocessing function and calculating the accuracy of k-means
         @param dataframe
        @type dataframe
        """
        self.dataset = file_path

    def pipeline(self):
        """
        getting the dataframe and calling all the steps in building the model
        @return: accuracy
        """
        processed_dataframe = pre_processing(self.dataset)
        trained_model = training_model(processed_dataframe)
        accuracy = validation(trained_model)
        print(accuracy)