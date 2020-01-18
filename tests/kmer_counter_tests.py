import unittest

from Bio.Seq import reverse_complement

from kmer_counter import KmerCounter


class MyTestCase(unittest.TestCase):

    def test_seq_of_one_kmer_gives_count_1_only_for_one_entry(self):
        k = 4
        kmer = "ACTA"
        res = KmerCounter(kmer).get_kmer_counts(k)
        self.assertEqual(len(res), 136)
        self.assertEqual(res[kmer], 1)
        self.assertEqual(len(list(filter(lambda x: x == 0, [res[i] for i in res.keys() if i != kmer]))), 135)

    def test_seq_with_2_different_kmers(self):
        k = 4
        seq = "ACTAA"
        res = KmerCounter(seq).get_kmer_counts(k)
        self.assertEqual(len(res), 136)
        kmer1, kmer2 = "ACTA", "CTAA"
        self.assertEqual(get_value_for_kmer(res, kmer1), 1)
        self.assertEqual(get_value_for_kmer(res, kmer2), 1)

    def test_kmer_frequencies_with_2_different_kmers(self):
        k = 4
        seq = "ACTAA"
        kmer1, kmer2 = "ACTA", "CTAA"
        res = KmerCounter(seq).get_kmer_frequencies(k)
        self.assertEqual(len(res), 136)
        self.assertEqual(get_value_for_kmer(res, kmer1), 1 / len(seq))
        self.assertEqual(get_value_for_kmer(res, kmer2), 1 / len(seq))

    def test_kmer_frequencies_sorted_list(self):
        k = 4
        seq = "ACTAA"
        res = KmerCounter(seq).get_kmer_frequencies_sorted_list(k)
        self.assertEqual(len(res), 136)
        self.assertTrue(is_kmer_list_sorted(res))  # check if sorted


def is_kmer_list_sorted(res):
    return all(res[i][0] < res[i + 1][0] for i in range(len(res) - 1))


def get_value_for_kmer(kmers, kmer):
    if kmer in kmers:
        return kmers[kmer]
    else:
        return kmers[reverse_complement(kmer)]


if __name__ == '__main__':
    unittest.main()


