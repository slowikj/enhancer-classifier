import numpy as np

from feature_creator import create_features
from frame import Frame


def prepare_features_labels(filename_label_list, alphabet, k):
    feature_list = []
    label_list = []
    for filename, label in filename_label_list:
        frames = read_train_frames(filename)
        label_list += [np.zeros(len(frames)) if label == 0 else np.ones(len(frames))]
        feature_list += [create_features(frames, alphabet=alphabet, k=k)]
    train_features = np.concatenate(feature_list)
    train_labels = np.concatenate(label_list)

    return train_features, train_labels


def read_train_frames(file_path):
    with open(file_path, "r") as f:
        frames = []
        should_read = 0
        for line in f:
            if should_read:
                frames += [Frame(sequence=line[:-1], begin=0)]
            should_read ^= 1
    return frames
