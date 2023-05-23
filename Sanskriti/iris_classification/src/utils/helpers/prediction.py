import pickle
import numpy as np
import pandas as pd

from Sanskriti.iris_classification.src.utils.constant import pickle_file_path

iris_model = pickle.load(open(pickle_file_path, 'rb'))


class PredictionModel:
    def __init__(self, user_input):
        self.input = user_input
        self.species_list = ['setosa', 'versicolor', 'virginica']

    def get_predict(self):
        try:
            user_input = self.input
            if isinstance(user_input, str):
                return "The input value is in string"
            else:
                sepal_length = float(user_input["sepal_length"])
                sepal_width = float(user_input["sepal_width"])
                petal_length = float(user_input["petal_length"])
                petal_width = float(user_input["petal_width"])
                input_values = [sepal_length, sepal_width, petal_length, petal_width]
                valid = True
                for i in input_values:
                    if i < 0:
                        valid = False
                        break

                if valid:
                    user_data = np.array([sepal_length, sepal_width, petal_length, petal_width])
                    if all(0 < item < 9 for item in user_data.tolist()):
                        flower_data = {"SepalLengthCm": [user_data[0]], "SepalWidthCm": [user_data[1]],
                                       "PetalLengthCm": [user_data[2]], "PetalWidthCm": [user_data[3]]
                                       }
                        flower_data_frame = pd.DataFrame(flower_data)
                        prediction = iris_model.predict(flower_data_frame)
                        species = np.argmax(prediction)
                        result = "Classified flower is: " + self.species_list[species].upper()
                        return result
                    else:
                        return "The Input Data is not valid"
                else:
                    return "The input value is negative"

        except Exception as e:
            return str(e)

        except:
            return "Invalid Parameters Provided!"
