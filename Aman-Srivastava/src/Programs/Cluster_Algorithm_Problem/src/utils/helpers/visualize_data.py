from matplotlib import pyplot as plt

from src.utils.constants import figure_path


def visualize_data(processed_data, labels):
    plt.scatter(processed_data['annual_income'], processed_data['spending_score_1_to_100'], c=labels, cmap=plt.cm.Set1)
    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score (1-100)')
    plt.title('Mall Customer Segmentation')
    plt.savefig(figure_path / "clusters_plot.png")
    plt.show()
