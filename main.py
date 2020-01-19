from train_data_processor import prepare_features_labels
from train_model import train

alphabet = ["A", "C", "G", "T"]
k = 4

if __name__ == "__main__":
    filenames_labels = (("./data/vista1500", 1), ("./data/randoms1500", 0))
    X_train, y_train = prepare_features_labels(filenames_labels, alphabet=alphabet, k=k)
    train(X_train, y_train)
