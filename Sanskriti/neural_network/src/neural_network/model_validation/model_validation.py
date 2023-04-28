
def validation(model_data):
    """
    getting the list from training data and dividing it into training and spilt data
    @param model_data
    @return: accuracy
    """
    model = model_data[0]
    print(model)
    X_train = model_data[1]
    X_test = model_data[2]
    y_train = model_data[3]
    y_test = model_data[4]

    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10)
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print('Test loss:', test_loss)
    print('Test accuracy:', test_acc)
    return test_acc




