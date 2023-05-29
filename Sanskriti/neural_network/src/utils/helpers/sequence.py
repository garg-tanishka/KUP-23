from keras import Sequential
from keras.layers import Dense


def layer_creation():
    model = Sequential([

        # Input Layer
        Dense(units=5, input_shape=(4,), activation="relu"),

        # Hidden Layer
        Dense(units=10, activation="sigmoid"),
        Dense(units=8, activation="sigmoid"),

        # Output Layer
        Dense(units=3, activation="sigmoid"),
    ])
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model