import statsmodels.api as sm
import pandas as pd


def backward_elimination(X_train, X_test, y_train):

    regressor_ols = sm.OLS(endog=y_train, exog=X_train).fit()

    X_opt_train = pd.DataFrame(X_train[:], dtype=float)
    while True:
        for h in range(X_opt_train.shape[1]):
            regressor_ols = sm.OLS(endog=y_train, exog=X_opt_train).fit()
            if regressor_ols.pvalues[h] == regressor_ols.pvalues.max() and regressor_ols.pvalues[h] > 0.05:
                X_opt_train.drop(X_opt_train.columns[h], axis=1, inplace=True)
                break
        if regressor_ols.pvalues.max() <= 0.05:
            break

    significant_cols = X_opt_train.columns

    X_train_sig = X_train[significant_cols]
    X_test_sig = X_test[significant_cols]
    significant_train_test = [X_train_sig, X_test_sig]

    return significant_train_test
