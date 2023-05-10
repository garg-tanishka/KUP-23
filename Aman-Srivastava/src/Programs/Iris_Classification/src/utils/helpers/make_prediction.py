import pickle
import numpy as np
import pandas as pd
from src.utils.constants import ml_model

iris_model = pickle.load(open(ml_model, 'rb'))


def prediction_decorator(prediction_class):
    class MakePrediction:

        def __init__(self, user_input):

            self.input = prediction_class(user_input)
            self.species_list = ['setosa', 'versicolor', 'virginica']

        def get_predict(self):
            try:
                user_input = self.input.properties

                sepal_length = float(round(user_input["sepal_length"], 1))
                sepal_width = float(round(user_input["sepal_width"], 1))
                petal_length = float(round(user_input["petal_length"], 1))
                petal_width = float(round(user_input["petal_width"], 1))

                input_data = np.array(
                    [sepal_length, sepal_width,
                     petal_length, petal_width])

                flower_data = {"SepalLengthCm": [input_data[0]],
                               "SepalWidthCm": [input_data[1]],
                               "PetalLengthCm": [input_data[2]],
                               "PetalWidthCm": [input_data[3]]
                               }

                flower_dimensions = pd.DataFrame(flower_data)
                prediction = iris_model.predict(flower_dimensions)
                species = np.argmax(prediction)
                result = "Classified flower is: " + self.species_list[species].upper()

                return result

            except Exception as e:
                return str(e)

            except:
                return "Invalid Parameters Provided!"

    return MakePrediction
