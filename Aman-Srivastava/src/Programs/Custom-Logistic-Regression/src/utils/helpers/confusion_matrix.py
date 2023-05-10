import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix


def check_confusion(y_test, pred, title):
    cm = confusion_matrix(y_test, pred)
    # print(classification_report(y_test, pred))
    # sns.heatmap(cm, annot=True, fmt='g', cbar=False, cmap='BuPu')
    # plt.xlabel('Actual Values')
    # plt.ylabel('Predicted Values')
    # plt.title(title)
    # plt.show()
    return cm
