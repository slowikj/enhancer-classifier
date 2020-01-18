import itertools

from Bio.Seq import reverse_complement


class KMerSpace:

    def __init__(self, k, alphabet):
        self.k = k
        self.alphabet = alphabet
        self.kmer_dict = self.__create_kmer_dict(k, alphabet)

    def increase(self, kmer, value=1):
        if kmer in self.kmer_dict:
            self.kmer_dict[kmer] += value
        else:
            self.kmer_dict[reverse_complement(kmer)] += value

    def get_sorted_by_kmer(self):
        return sorted(list(self.kmer_dict.items()),
                      key=lambda x: x[0])

    def get_value(self, kmer):
        return self.kmer_dict[kmer] if kmer in self.kmer_dict \
            else self.kmer_dict[reverse_complement(kmer)]

    @staticmethod
    def __create_kmer_dict(k, alphabet):
        res_dict = dict()
        kmer_keys = list(map(lambda x: "".join(x), itertools.product(alphabet, repeat=k)))
        for kmer_key in kmer_keys:
            if reverse_complement(kmer_key) not in res_dict:
                res_dict[kmer_key] = 0
        return res_dict
