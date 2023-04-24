import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor

    def training_model():
        forest = RandomForestRegressor()
        forest.fit(X_train_scale, y_train)
        forest.score(X_test_scale, y_test)
        y_pred = forest.predict(X_test_scale)
        plt.scatter(y_pred, y_test)
        plt.figure(figsize=(12, 8))
        plt.figure(figsize=(12, 8))
        plt.scatter(y_pred, y_test)
        plt.plot(range(0, 3000), range(0, 3000), c="black")
