# from sklearn.linear_model import LogisticRegression
# import numpy as np
# from sklearn.model_selection import GridSearchCV
#
#
# def hyper_parameter_tuning(X, y):
#     model = LogisticRegression()
#
#     param_grid = [{'penalty': ['l1', 'l2', 'elasticnet', 'none'],
#                    'C': np.logspace(-4, 4, 20),
#                    'solver': ['lbfgs', 'newton-cg', 'liblinear', 'sag', 'saga'],
#                    'max_iter': [100, 1000, 2500, 5000]
#                    }]
#
#     clf = GridSearchCV(model, param_grid=param_grid, cv=3, verbose=True, n_jobs=-1)
#     best_clf = clf.fit(X, y)
#     print(best_clf.best_estimator_)
#     print(best_clf.score(X, y))
