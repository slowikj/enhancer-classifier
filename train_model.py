from sklearn.ensemble import RandomForestClassifier


def train(X, y):
    clf = RandomForestClassifier(max_depth=5, random_state=123)
    clf.fit(X, y)
    return clf
