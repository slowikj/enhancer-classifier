from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import VarianceThreshold, chi2, SelectKBest
from sklearn.metrics import make_scorer, f1_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.pipeline import Pipeline


def train_model(X, y):
    random_state = 123

    random_forest = RandomForestClassifier()
    hyperparams = {"randomForest__n_estimators": list(range(10, 1500, 150)),
                   "randomForest__max_depth": list(range(3, 50, 5)),
                   "kbest__k": list(range(5, 100, 10))}
    inner_cv = StratifiedKFold(n_splits=5, random_state=random_state, shuffle=True)
    outer_cv = StratifiedKFold(n_splits=5, random_state=random_state, shuffle=True)
    pipeline = Pipeline([
        ("variance threshold", VarianceThreshold()),
        ("kbest", SelectKBest(chi2)),
        ("randomForest", random_forest)
    ])
    rs = GridSearchCV(pipeline, hyperparams, verbose=1, cv=inner_cv, scoring=make_scorer(roc_auc_score), n_jobs=8)
    rs.fit(X, y)
    scores = cross_val_score(rs, X, y, cv=outer_cv)
    print(rs.best_score_)
    print(rs.best_params_)
    print(scores)
    return rs
