from Bio.Seq import reverse_complement

from kmer_space import KMerSpace


class KMerCounter:

    def __init__(self, kmer_space: KMerSpace):
        self.kmer_space = kmer_space

    def count(self, seq):
        seq = seq.upper()

        k = self.kmer_space.k
        for i in range(len(seq) - k + 1):
            kmer = seq[i:(i + k)]
            self.kmer_space.increase(kmer)

        return self.kmer_space.get_sorted_by_kmer()
