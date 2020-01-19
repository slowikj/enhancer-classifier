import numpy as np

from kmer_counter import KMerCounter
from kmer_space import KMerSpace


def prepare_features_labels(filename_label_list, alphabet, k):
    feature_list = []
    label_list = []
    for filename, label in filename_label_list:
        sequences = read_train_sequences(filename)
        label_list += [np.zeros(len(sequences)) if label == 0 else np.ones(len(sequences))]
        feature_list += [create_features(sequences, alphabet=alphabet, k=k)]
    train_features = np.concatenate(feature_list)
    train_labels = np.concatenate(label_list)

    return train_features, train_labels


def read_train_sequences(file_path):
    with open(file_path, "r") as f:
        sequences = []
        should_read = 0
        for line in f:
            if should_read:
                sequences += [__clean(line)]
            should_read ^= 1
    return sequences


def create_features(sequences, alphabet, k):
    s = tuple((__to_horizontal_vector(create_features_for_seq(seq, alphabet, k)) for seq in sequences))
    return np.concatenate(s, axis=0)


def create_features_for_seq(seq, alphabet, k):
    return KMerCounter(KMerSpace(alphabet=alphabet, k=k)).get_frequencies_numpy(seq=seq)


def __to_horizontal_vector(v):
    col_num = v.shape[0]
    return v.reshape(1, col_num)


def __clean(line):
    clean_line = line.upper()
    return clean_line[:-1]
