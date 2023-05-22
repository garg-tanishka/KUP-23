from src.iris_classification_module.pre_processing.iris_pre_processing import pre_processing
from src.utils.constants import dataset_path, model_path
from src.utils.helpers.sequence_creation import layer_creation
import pickle


def train_decorator(train_class):
    class IrisClassification:

        def __init__(self, user_input):
            self.data_set = dataset_path
            self.user_input = train_class(user_input)

        def get_model(self):
            return self.model_pipeline()

        def model_pipeline(self):
            try:
                pre_processed_data = pre_processing(self.data_set)
                model = layer_creation()

                x_train = pre_processed_data[0]
                x_test = pre_processed_data[1]
                y_train = pre_processed_data[2]
                y_test = pre_processed_data[3]

                history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=20)
                pickle.dump(model, open(model_path / 'iris_model.pkl', 'wb'))

                score = history.history["accuracy"][-1]
                accuracy_score = round(score, 2)

                if 0.95 < accuracy_score < 0.98:
                    return "model trained with accuracy: " + str(accuracy_score)
                else:
                    return "model not good enough try training model again"

            except Exception as e:
                return str(e)

    return IrisClassification
