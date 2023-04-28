def validation(model_data):
    """
    getting the list from training data and dividing it into training and spilt data
    @param model_data
    @return: accuracy
    """
    model = model_data[0]
    X_train = model_data[1]
    X_test = model_data[2]
    y_train = model_data[3]
    y_test = model_data[4]
    if model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10):
        print("Model is trained successfully")
    else:
        print("Model is Failed")
