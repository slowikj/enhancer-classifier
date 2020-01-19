import numpy as np

from kmer_space import KMerSpace


class KMerCounter:

    def __init__(self, kmer_space: KMerSpace):
        self.kmer_space = kmer_space

    def get_frequencies_numpy(self, seq):
        frequencies = self.get_frequencies(seq)
        return np.array(list(map(lambda x: x[1], frequencies)))

    def get_frequencies(self, seq):
        counts = self.count(seq)
        return map(lambda x: (x[0], x[1] / len(seq)), counts)

    def count(self, seq):
        k = self.kmer_space.k
        for i in range(len(seq) - k + 1):
            kmer = seq[i:(i + k)]
            self.kmer_space.increase(kmer)

        return self.kmer_space.get_sorted_by_kmer()
