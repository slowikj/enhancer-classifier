from sklearn.ensemble import RandomForestClassifier


def train(features, labels):
    clf = RandomForestClassifier(max_depth=5, random_state=123)
    clf.fit(features, labels)
    return clf
