from src.iris_classification_module.pipeline.iris_classification_problem import train_decorator
from src.utils.helpers.make_prediction import prediction_decorator


@train_decorator
class TrainModel:

    def __init__(self, user_input):
        self.input = user_input


@prediction_decorator
class PredictModel:

    def __init__(self, flower_dimension):
        self.properties = flower_dimension
