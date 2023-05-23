from Sanskriti.clustering_algorithm.src.k_means.pipeline.pipeline import K_Means


def input_function():
    query = input("Enter command: ")
    if query == "train":
        clusters = K_Means()
        result = clusters.pipeline()
        print(result)
    else:
        print("Invalid Command")


if __name__ == "__main__":
    input_function()
