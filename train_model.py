from sklearn.ensemble import RandomForestClassifier


def train_model(X, y):
    clf = RandomForestClassifier(random_state=123)
    clf.fit(X, y)
    return clf
