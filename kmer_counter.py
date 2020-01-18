from Bio.Seq import reverse_complement


class KmerCounter:

    def __init__(self, seq: str, alphabet=None):
        if alphabet is None:
            alphabet = {"A", "C", "T", "G"}
        self.seq = seq.upper()
        self.alphabet = alphabet

    def get_kmer_frequencies_sorted_list(self, k):
        res_dict = self.get_kmer_frequencies(k)
        return sorted(list(res_dict.items()), key=lambda x: x[0])

    def get_kmer_frequencies(self, k):
        res = self.get_kmer_counts(k)
        for key in res:
            res[key] /= len(self.seq)
        return res

    def get_kmer_counts(self, k):
        kmers = dict()
        self.__update_dict_with_all_kmers(k, kmers)

        for i in range(len(self.seq) - k + 1):
            current_kmer = self.seq[i:(i + k)]
            self.__insert_kmer(current_kmer, kmers)

        return kmers

    def __insert_kmer(self, current_kmer, kmers):
        reversed_complement_kmer = reverse_complement(current_kmer)
        if current_kmer in kmers:
            kmers[current_kmer] += 1
        elif reversed_complement_kmer in kmers:
            kmers[reversed_complement_kmer] += 1
        else:
            kmers[current_kmer] = 1

    def __update_dict_with_all_kmers(self, k, kmer_dict):
        self.__generate_all_kmers_rec(k, "", kmer_dict)

    def __generate_all_kmers_rec(self, k, current_kmer, kmer_dict):
        if len(current_kmer) == k:
            if not (current_kmer in kmer_dict or reverse_complement(current_kmer) in kmer_dict):
                kmer_dict[current_kmer] = 0
            return

        for elem in self.alphabet:
            self.__generate_all_kmers_rec(k, current_kmer + elem, kmer_dict)
