import numpy as np

from kmer_counter import KMerCounter
from kmer_space import KMerSpace


def create_features(frames, alphabet, k):
    s = tuple((__to_horizontal_vector(create_features_for_seq(frame.sequence, alphabet, k)) for frame in frames))
    return np.concatenate(s, axis=0)


def create_features_for_seq(seq, alphabet, k):
    return KMerCounter(KMerSpace(alphabet=alphabet, k=k)).get_frequencies_numpy(seq=seq)


def __to_horizontal_vector(v):
    col_num = v.shape[0]
    return v.reshape(1, col_num)